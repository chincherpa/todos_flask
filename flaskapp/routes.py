import datetime
import json
import os
import sys

from flask import redirect, render_template, request
from flaskapp import app
from flaskapp.forms import PostForm

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, "static")

global todos
path_to_js = os.path.join(APP_STATIC, "todos.json")


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


@app.route("/")
@app.route("/open")
def index():
    # todos = load_json()
    return render_template("index.html", todos=todos, status_to_show="open", comments=False, id_comments=None)


@app.route("/closed")
def closed():
    # todos = load_json()
    return render_template("index.html", todos=todos, status_to_show="closed", comments=False, id_comments=None)


@app.route("/open_comments")
def open_c():
    # todos = load_json()
    return render_template("index.html", todos=todos, status_to_show="open", comments=True, id_comments=None)


@app.route("/closed_comments")
def closed_c():
    # todos = load_json()
    return render_template("index.html", todos=todos, status_to_show="closed", comments=True, id_comments=None)


@app.route("/one_comments/<status>/<int:todo_id>")
def one_comments(todo_id, status):
    todo_id = str(todo_id)
    return render_template( "index.html", todos=todos, status_to_show=status, comments=False, id_comments=todo_id, )


@app.route("/todo/<int:todo_id>/edit", methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo_id = str(todo_id)
    todo_dic = todos["todos"].get(todo_id)
    print('#####################')
    print('#####################')
    print(todo_dic)
    print('#####################')
    print('#####################')
    form = PostForm()
    if form.validate_on_submit():
        print('*POST* ' * 7)
        print(f'{form.title.data=}')
        todo_dic["title"] = form.title.data
        return redirect('/open')

    elif request.method == "GET":
        print('*GET* ' * 7)
        print(f'{todo_dic["title"]=}')
        form.title.data = todo_dic["title"]

    # return render_template('edit.html', todo=todo_dic)
    return render_template("edit.html", form=form, todo=todo_dic)


@app.route("/todo/<int:todo_id>/close")
def close_todo(todo_id):
    todo_id = str(todo_id)
    todos["todos"][todo_id]["status"] = "closed"
    dump_todos_to_json()
    return redirect('/open')


@app.route("/todo/<int:todo_id>/reopen")
def reopen_todo(todo_id):
    todo_id = str(todo_id)
    todos["todos"][todo_id]["status"] = "open"
    dump_todos_to_json()
    return redirect('/open')


@app.route("/new_todo")
def create_todo():
    today = str(datetime.date.today())

    new_title = request.form['new_todo_title']

    new_tags = request.form['new_todo_tags']
    lnew_tags_temp = new_tags.replace(" ", ",").split(",")
    lnew_tags = list(filter(None, lnew_tags_temp))

    new_todo_reminder = request.form['new_todo_reminder']
    # if not new_todo_reminder:
    #     new_todo_reminder = ""

    todos["ids"] += 1
    new_id = str(todos["ids"])
    todos["todos"][new_id] = {
        "id": new_id,
        "title": new_title,
        "status": "open",
        "comments": [""],
        "tags": lnew_tags,
        "result": "",
        "date_added": today,
        "rem_time": new_todo_reminder,
    }
    # dump_todos_to_json()
    print(todos["todos"][new_id])
    return redirect('/open')


if __name__ == "__main__":
    app.run(debug=True)
