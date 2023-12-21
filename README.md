## Django / HTMX - Simple Directory

Use Python >= 3.11

Existing database:

    git clone https://github.com/brndnsmth/simple-directory.git
    cd simple-directory
    python -m venv .venv
    source .venv/bin/activate
    (.venv) -> pip install -r requirements.txt
    (.venv) -> python manage.py runserver

Fresh database:

    git clone https://github.com/brndnsmth/simple-directory.git
    cd simple-directory
    python -m venv .venv
    source .venv/bin/activate
    (.venv) -> pip install -r requirements.txt
    (.venv) -> python manage.py makemigrations
    (.venv) -> python manage.py migrate
    (.venv) -> python import-people.py
    (.venv) -> python manage.py runserver

Credit/inspiration: Tom Dekan (https://twitter.com/tomdekan)