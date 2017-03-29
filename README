# Bottle-Boilerplate

Bottle-Boilerplate is a minimal setup for using python bottle web framework with a sqlite3 db via sqlalchemy.

Basic useful feature list:

 * alembi db schema migration
 * boilerplate code example of using tornado server, auto-reload
 * boilerplate code example of models built with sqlalchemy


# Quickstart

To get started, first we need to setup the virtualenv.

```bash
$ git clone https://github.com/zhouzhuojie/bottle_boilerplate.git
$ cd bottle_boilerplate
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

Setup database

```bash
# sqlite3 is the basic db we want to support at the beginning
$ mkdir localdb

# actually it will create the db and a todos table
$ alembic upgrade head  
```

Run the server

```
$ python main.py
```
