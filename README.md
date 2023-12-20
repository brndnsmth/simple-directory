## Django / HTMX - Simple Directory

Existing database:

    git clone https://github.com/brndnsmth/simple-directory.git
    cd simple-directory
    python3 -m venv .venv
    source .venv/bin/activate
    (.venv) -> pip3 install -r requirements.txt
    (.venv) -> python3 manage.py runserver

Fresh database:

    git clone https://github.com/brndnsmth/simple-directory.git
    cd simple-directory
    python3 -m venv .venv
    source .venv/bin/activate
    (.venv) -> pip3 install -r requirements.txt
    (.venv) -> python3 manage.py makemigrations
    (.venv) -> python3 manage.py migrate
    (.venv) -> python3 import-people.py
    (.venv) -> python3 manage.py runserver

Credit to Tom Dekan (https://twitter.com/tomdekan)