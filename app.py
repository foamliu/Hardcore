# flask_web/app.py
import json

from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
with open('courses.json', 'r') as file:
    courses = json.load(file)


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
def math():
    return render_template('math.html')


@app.route('/alg_top')
def alg_top():
    course = [c for c in courses if c['key'] == 'AlgTop'][0]
    # print(course)
    return render_template('catalog.html', course=course)


@app.route('/course')
def course():
    youku_id = request.args.get('youku_id')
    # print(course)
    return render_template('course.html', youku_id=youku_id)
