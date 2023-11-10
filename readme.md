# Local Setup
- Clone the project
- Run `setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

# Folder Structure
- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- `setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `static` - default `static` files folder. It serves at '/static' path. More about it is [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/static/).
- `templates` - Default flask templates folder


```
├── .gitignore
├── application
│   ├── config.py
│   ├── api.py
│   ├── controllers.py
│   ├── database.py
│   ├── __init__.py
│   ├── models.py
├── db_directory
│   └── quaver_data.sqlite3
├── local_run.sh
├── local_setup.sh
├── main.py
├── readme.md
├── requirements.txt
├── static
│   ├── favicon.ico
|   └── quaver_logo_bg_removed.png
└── templates
    ├── home.html
    ├── new_user.html
    ├── signup.html
    └── welcome.html
```