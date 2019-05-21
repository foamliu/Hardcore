# flask_web/app.py

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(config_name, static_url_path="", static_folder="static")
    bootstrap.init_app(app)
    # Bootstrap(app)
    return app


app = create_app(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/math')
def home():
    return render_template('math.html')


@app.route('/alg_top')
def alg_top():
    return render_template('course.html')
