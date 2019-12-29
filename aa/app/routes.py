import json

from flask import render_template
from app import app

global todos


def load_json():
    try:
        with open('./app/todos.json', "r") as jsf:
            todos = json.load(jsf)
        return todos
    except IndexError as e:
        print(f"Something is wrong!\n{e}")
        return None


@app.route('/')
@app.route('/open/')
def index():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='open')


@app.route('/finished/')
def show_finished():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='finished')


@app.route('#')