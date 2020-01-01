import json

from flask import Flask, render_template
# from app import app

app = Flask(__name__)

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
# @app.route('/open/')
def index():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='open', comments=False)


@app.route('/finished/')
def finished():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='finished', comments=False)


@app.route('/open_comments/')
def open_c():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='open', comments=True)


@app.route('/finished_comments/')
def finished_c():
    todos = load_json()
    return render_template('index.html', title='Lutz Todos', todos=todos, status_to_show='finished', comments=True)


# @app.route('#')


if __name__ == '__main__':
    app.run(debug=True)