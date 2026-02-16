"""
This module initializes the Flask application and sets up the routes for the Game Grid project.

It imports necessary modules, configures CORS, and defines the home route that renders the index page
with a list of games retrieved from the library manager.

Modules:
    flask: The Flask framework for creating web applications.
    flask_cors: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
    library_manager: A custom module for managing the game library.
    config: Configuration settings for improved game engine support.

Functions:
    home(): Renders the index page with a list of games.
    serve_game_files(filepath): Serves game files with proper headers.
    after_request(response): Adds security and performance headers.

Usage:
    Run this module to start the Flask development server.
"""
import mimetypes
import os
from pathlib import Path

import flask
from flask import render_template, send_from_directory, make_response
from flask_cors import CORS

import library_manager
import config

# Configure additional MIME types for game engines
for extension, mimetype in config.GAME_ENGINE_MIMETYPES.items():
    mimetypes.add_type(mimetype, extension)

app = flask.Flask(__name__)

# Enhanced CORS configuration
CORS(app, resources={
    r"/static/*": {
        "origins": config.CORS_CONFIG['origins'],
        "methods": config.CORS_CONFIG['methods'],
        "allow_headers": config.CORS_CONFIG['allow_headers'],
        "expose_headers": config.CORS_CONFIG['expose_headers'],
        "supports_credentials": config.CORS_CONFIG['supports_credentials'],
        "max_age": config.CORS_CONFIG['max_age']
    }
})


@app.route('/')
def home():
    """Home route that renders the index page with a list of games.

    Returns:
        flask.Response: The rendered template for the index page with the list of games.
    """
    games = library_manager.get_library()
    print(games)
    return render_template('index.jinja2', games=games)

@app.route('/static/games/<path:filepath>')
def serve_game_files(filepath):
    """Serve game files with proper headers for stability.

    This route handles game files separately to ensure proper MIME types,
    caching headers, and CORS headers are set for RPG Maker and other game engines.

    Args:
        filepath: The path to the file within the static/games directory.

    Returns:
        flask.Response: The file with appropriate headers.
    """
    static_games_path = os.path.join(app.root_path, 'static', 'games')

    safe_path = os.path.normpath(os.path.join(static_games_path, filepath))
    if not safe_path.startswith(static_games_path):
        flask.abort(403)

    if not os.path.exists(safe_path):
        flask.abort(404)

    directory = os.path.dirname(safe_path)
    filename = os.path.basename(safe_path)

    response = make_response(send_from_directory(directory, filename))

    file_ext = Path(filename).suffix.lower()
    cache_duration = config.CACHE_DURATIONS['default']

    for category, extensions in config.CACHE_EXTENSIONS.items():
        if file_ext in extensions:
            cache_duration = config.CACHE_DURATIONS.get(category, config.CACHE_DURATIONS['default'])
            break

    response.headers['Cache-Control'] = f'public, max-age={cache_duration}'

    mimetype_from_config = config.GAME_ENGINE_MIMETYPES.get(file_ext)
    if not mimetype_from_config:
        mimetype_from_config, _ = mimetypes.guess_type(filename)
    if mimetype_from_config:
        response.headers['Content-Type'] = mimetype_from_config

    response.headers['Accept-Ranges'] = 'bytes'

    return response

@app.after_request
def after_request(response):
    """Add security and performance headers to all responses.

    Args:
        response: The Flask response object.

    Returns:
        flask.Response: The modified response with additional headers.
    """
    if 'Access-Control-Allow-Origin' not in response.headers:
        response.headers['Access-Control-Allow-Origin'] = config.CORS_CONFIG['origins']

    for header, value in config.SECURITY_HEADERS.items():
        if header not in response.headers:
            response.headers[header] = value

    return response

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
