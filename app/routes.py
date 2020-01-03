import json

from flask import Flask, render_template
# from app import app

app = Flask(__name__)

global todos
path_to_js = './app/todos.json'


def dump_todos_to_json():
    with open(path_to_js, "w") as f:
        json.dump(todos, f, indent=4)


def load_json():
    try:
        with open(path_to_js, "r") as jsf:
            todos = json.load(jsf)
        return todos
    except IndexError as e:
        print(f"Something is wrong!\n{e}")
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


@app.route("/todo/<int:todo_id>/edit", methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo_dic = todos["todos"].get(todo_id)
    return render_template('edit.html', todo=todo_dic)


@app.route("/todo/<int:todo_id>/close", methods=['GET'])
def close_todo(todo_id):
    todo_id = str(todo_id)
    todos["todos"][todo_id]["status"] = "closed"
    dump_todos_to_json()
    return render_template('index.html', todos=todos, status_to_show='open', comments=False)


if __name__ == '__main__':
    app.run(debug=True)
