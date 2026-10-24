# Local Setup
- Clone the project.
- Install Python 3.8 or newer and make `python3` or `python` available on your PATH.
- Run `./local_setup.sh` from a POSIX-compatible shell (Linux/macOS terminal, WSL, or Git Bash on Windows). This creates `.env` and installs the packages in `requirements.txt`.

# Local Development Run
- Run `./local_run.sh` to start the Flask app in development mode and open it in your default browser. On Windows, use Git Bash or WSL.
- Use the default username and password as "test".
- Note: Audio files, lyrics and images have been omitted. These have to be added back for the best experience `:)`

# Folder Structure
- `application/` contains the Flask application modules.
- `db_directory/` contains the SQLite database used by the app.
- `static/` contains the profile image, favicon, logo, and default song cover.
- `templates/` contains the HTML templates.
- `local_setup.sh` creates the local virtual environment and installs dependencies.
- `local_run.sh` starts the development server and opens it in a browser.

```
.
|-- .gitignore
|-- application/
|   |-- __init__.py
|   |-- api.py
|   |-- config.py
|   |-- controllers.py
|   |-- database.py
|   `-- models.py
|-- db_directory/
|   `-- quaver_data.sqlite3
|-- local_run.sh
|-- local_setup.sh
|-- main.py
|-- readme.md
|-- requirements.txt
|-- static/
|   |-- default_pfp.png
|   |-- favicon.ico
|   |-- quaver_logo_bg_removed.png
|   `-- song_cover_default.png
`-- templates/
    |-- home.html
    |-- lyrics.html
    |-- new_user.html
    |-- profile.html
    |-- search_results.html
    |-- signup.html
    `-- welcome.html
```
