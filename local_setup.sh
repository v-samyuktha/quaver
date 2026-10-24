#!/bin/sh
set -eu

echo "Setting up the local Python virtual environment."
PYTHON=""
for candidate in python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then
        if "$candidate" -c 'import sys; raise SystemExit(sys.version_info < (3, 8))' >/dev/null 2>&1; then
            PYTHON="$candidate"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "Error: Python 3.8 or newer is required (Python 3.12 is recommended)." >&2
    echo "Install Python and ensure 'python3' or 'python' is on your PATH." >&2
    exit 1
fi

if [ ! -d ".env" ]; then
    echo "Creating .env with $PYTHON ($($PYTHON --version 2>&1))."
    "$PYTHON" -m venv .env
else
    echo "Using existing .env virtual environment."
fi

if [ -x ".env/bin/python" ]; then
    VENV_PYTHON=".env/bin/python"
elif [ -x ".env/Scripts/python.exe" ]; then
    VENV_PYTHON=".env/Scripts/python.exe"
else
    echo "Error: .env exists but has no recognizable Python executable." >&2
    echo "Remove .env and rerun this script to recreate it." >&2
    exit 1
fi

"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install -r requirements.txt
echo "Setup complete. Run ./local_run.sh to start the app."
