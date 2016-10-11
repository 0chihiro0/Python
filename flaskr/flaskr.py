
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash


# creat our little applicaton
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	"""Open a new database connection if there is none yet for the current application context."""

	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of requete."""
	if hasattr(g, "sqlite_db"):
		g.sqlite_db.close()

def init_db():
	db = get_db()
	with app.open_resourse('schems.sql', mode='r') as f:          # open.resourse() function opens file from the resourse location(flaskr folder) and allows you to read from it.
		db.cursor().executescript(f.read())
	db.commit()

@app.cli.command('initdb')                                # The app.cli.command() decorator registers a new command with the flask script.
def initdb_command():
	"""Initialixzes the database."""
	init_db()
	print('Initialize the database.")

