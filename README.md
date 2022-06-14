# Simple_Auth_Todo_App

This small pet-project was created to show what can I create with [flask](https://flask.palletsprojects.com/en/2.1.x/).

## Installation

Use [pip](https://pip.pypa.io/en/stable/) package manager to install all requirements.

```bash
python3.9 -m venv env

source env/bin/activate

pip install -r requirements.txt
```

Simple_Auth_Todo_App requires [postgres](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04) to be installed and configured.

So we need to do some things before running the app.

```bash
sudo -u postgres psql

create database flask_app;

create user flask with encrypted password '1111';

grant all privileges on database flask_app to flask;

\q
```

Back to your environment. 

```bash
export FLASK_APP=src

flask db migrate

flask db upgrade

flask run
```

## Usage

Make todos for your day/evening.

Enjoy!
