import flask
from flask import render_template
from flask_cors import CORS
import library_manager

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def home():
    games = library_manager.get_library()
    print(games)
    return render_template('index.jinja2', games=games)


if __name__ == '__main__':
    app.run(host="0.0.0.0")