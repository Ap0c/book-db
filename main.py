# ----- Imports ----- #

from flask import Flask, render_template, abort
import os.path
from db import Database


# ----- Setup ----- #

# The database schema file.
DB_SCHEMA = os.path.join(os.path.dirname(os.path.realpath(__file__)),
	'schema.sql')

# The database file.
DB_FILE = 'books.db'

# The flask app object.
app = Flask(__name__)

# Handles database connections and queries.
db = Database(DB_FILE, DB_SCHEMA)


# ----- Routes ----- #

@app.route('/')
def home():
	return 'Hello world'


@app.route('/<id>')
def book(id):

	book_data = db.query('SELECT * FROM book WHERE id = ?', id)

	if len(book_data) > 0:
		return render_template('book.html', **book_data[0])
	else:
		abort(404)


# ----- Run ----- #

if __name__ == '__main__':
	app.run(debug=True)
