import json
import os
import sys

from flask import render_template, request
from flaskapp import app
from flaskapp.forms import PostForm

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

global todos
path_to_js = os.path.join(APP_STATIC, 'todos.json')


def dump_todos_to_json():
    with open(path_to_js, "w") as f:
        json.dump(todos, f, indent=4)


def load_json():
    try:
        with open(path_to_js, "r") as jsf:
            todos = json.load(jsf)
        return todos
    except FileNotFoundError as e:
        print(f"Datei nicht gefunden!\n{path_to_js}\n{e}")
        sys.exit()
        return None


todos = load_json()


@app.route('/')
@app.route('/open/')
def index():
    # todos = load_json()
    return render_template('index.html', todos=todos, status_to_show='open', comments=False)


@app.route('/closed/')
def closed():
    # todos = load_json()
    return render_template('index.html', todos=todos, status_to_show='closed', comments=False)


@app.route('/open_comments/')
def open_c():
    # todos = load_json()
    return render_template('index.html', todos=todos, status_to_show='open', comments=True)


@app.route('/closed_comments/')
def closed_c():
    # todos = load_json()
    return render_template('index.html', todos=todos, status_to_show='closed', comments=True)


@app.route("/todo/<int:todo_id>/edit")
def edit_todo(todo_id):
    todo_dic = todos["todos"].get(todo_id)
    form = PostForm()
    if form.validate_on_submit():
        todo_dic["title"] = form.title.data
        # post.content = form.content.data
    elif request.method == 'GET':
        form.title.data = todo_dic["title"]
        # form.content.data = post.content

    # return render_template('edit.html', todo=todo_dic)
    return render_template('edit.html', todo=todo_dic)


@app.route("/todo/<int:todo_id>/close")
def close_todo(todo_id):
    todo_id = str(todo_id)
    todos["todos"][todo_id]["status"] = "closed"
    dump_todos_to_json()
    return render_template('index.html', todos=todos, status_to_show='open', comments=False)


@app.route("/todo/<int:todo_id>/reopen")
def reopen_todo(todo_id):
    todo_id = str(todo_id)
    todos["todos"][todo_id]["status"] = "open"
    dump_todos_to_json()
    return render_template('index.html', todos=todos, status_to_show='open', comments=False)


if __name__ == '__main__':
    app.run(debug=True)
