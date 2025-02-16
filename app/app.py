"""
This module initializes the Flask application and sets up the routes for the Game Grid project.

It imports necessary modules, configures CORS, and defines the home route that renders the index page
with a list of games retrieved from the library manager.

Modules:
    flask: The Flask framework for creating web applications.
    flask_cors: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
    library_manager: A custom module for managing the game library.

Functions:
    home(): Renders the index page with a list of games.

Usage:
    Run this module to start the Flask development server.
"""
import flask
from flask import render_template
from flask_cors import CORS

import library_manager

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Home route that renders the index page with a list of games.

    Returns:
        flask.Response: The rendered template for the index page with the list of games.
    """
    games = library_manager.get_library()
    print(games)
    return render_template('index.jinja2', games=games)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
