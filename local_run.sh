#!/bin/sh
set -eu

if [ -x ".env/bin/python" ]; then
    VENV_PYTHON=".env/bin/python"
elif [ -x ".env/Scripts/python.exe" ]; then
    VENV_PYTHON=".env/Scripts/python.exe"
else
    echo "No usable .env virtual environment found. Run ./local_setup.sh first." >&2
    exit 1
fi

export ENV=development

# Start the server first, then open the page once it is accepting requests.
"$VENV_PYTHON" main.py &
APP_PID=$!

"$VENV_PYTHON" -c 'import time, urllib.error, urllib.request, webbrowser
url = "http://127.0.0.1:8080/"
deadline = time.monotonic() + 60
while time.monotonic() < deadline:
    try:
        urllib.request.urlopen(url, timeout=1)
        webbrowser.open(url)
        break
    except urllib.error.HTTPError:
        webbrowser.open(url)
        break
    except Exception:
        time.sleep(0.5)' &
BROWSER_PID=$!

cleanup() {
    kill "$BROWSER_PID" 2>/dev/null || true
    kill "$APP_PID" 2>/dev/null || true
}
trap cleanup INT TERM

if wait "$APP_PID"; then
    STATUS=0
else
    STATUS=$?
fi
kill "$BROWSER_PID" 2>/dev/null || true
exit "$STATUS"
