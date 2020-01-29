import datetime
import json
import os
import sys

from flask import redirect, render_template, request, send_from_directory, url_for
from flaskapp import app
from flaskapp.forms import PostForm

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, "static")

global todos
path_to_js = os.path.join(APP_STATIC, "todos.json")


@app.route("/favicon.ico")
def favicon():
  return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")


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


def get_ids_to_remind():
  lto_remind = []
  now = datetime.datetime.now()
  dateformat = "%Y-%m-%d"

  for id_key, todo in todos["todos"].items():
    if todo["status"] == "open":
      rem_time = todo.get("rem_time", "")
      if len(rem_time) > 0:
        rem_time_dt = datetime.datetime.strptime(rem_time, dateformat)
        rest = rem_time_dt - now
        if rest.days < 2:
          lto_remind.append(id_key)
  return lto_remind


def get_used_tags():
  num_of_tags = {}

  for _, todo in todos["todos"].items():
    if todo["status"] == "open":
      for tag in todo["tags"]:
        if tag:
          if tag in num_of_tags.keys():
            num_of_tags[tag] += 1
          else:
            num_of_tags[tag] = 1

  lused_tags1 = list(num_of_tags.keys())
  lused_tags2 = []
  lused_tags1.sort(key=str.casefold)

  if len(lused_tags1) >= 15:
    lused_tags2 = lused_tags1[len(lused_tags1) // 2:]
    lused_tags1 = lused_tags1[:len(lused_tags1) // 2]

  return lused_tags1, lused_tags2


@app.route("/")
@app.route("/open")
def index():
  lto_remind = get_ids_to_remind()
  lused_tags1, lused_tags2 = get_used_tags()
  return render_template("index.html", todos=todos, status_to_show="open", comments=False, id_comments=None, ids_to_remind=lto_remind, used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=None, )


# Route for handling the login page logic
@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'].lower() != 'lulef' or request.form['password'] != 'yxasqw12':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route("/closed")
def closed():
  lused_tags1, lused_tags2 = get_used_tags()
  return render_template("index.html", todos=todos, status_to_show="closed", comments=False, id_comments=None, ids_to_remind=[], used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=None, )


@app.route("/open_comments")
def open_c():
  lto_remind = get_ids_to_remind()
  lused_tags1, lused_tags2 = get_used_tags()
  return render_template("index.html", todos=todos, status_to_show="open", comments=True, id_comments=None, ids_to_remind=lto_remind, used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=None)


@app.route("/closed_comments")
def closed_c():
  lused_tags1, lused_tags2 = get_used_tags()
  return render_template("index.html", todos=todos, status_to_show="closed", comments=True, id_comments=None, ids_to_remind=[], used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=None)


@app.route("/<status>/one_comments/<int:todo_id>")
def one_comments(todo_id, status):
  lto_remind = get_ids_to_remind()
  lused_tags1, lused_tags2 = get_used_tags()
  todo_id = str(todo_id)
  return render_template("index.html", todos=todos, status_to_show=status, comments=False, id_comments=todo_id, ids_to_remind=lto_remind, used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=None, )


@app.route("/todo/edit/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
  todo_id = str(todo_id)
  todo_dic = todos["todos"].get(todo_id)
  form = PostForm()
  if request.method == "POST":
    today = str(datetime.date.today())

    todos["todos"][todo_id]["title"] = form.title.data

    if form.comment_1.data:
      todos["todos"][todo_id]["comments"][0][0] = form.comment_1.data
    if form.comment_2.data:
      todos["todos"][todo_id]["comments"][1][0] = form.comment_2.data
    if form.comment_3.data:
      todos["todos"][todo_id]["comments"][2][0] = form.comment_3.data
    if form.comment_4.data:
      todos["todos"][todo_id]["comments"][3][0] = form.comment_4.data
    if form.comment_5.data:
      todos["todos"][todo_id]["comments"][4][0] = form.comment_5.data
    if form.comment_6.data:
      todos["todos"][todo_id]["comments"][5][0] = form.comment_6.data
    if form.comment_7.data:
      todos["todos"][todo_id]["comments"][6][0] = form.comment_7.data
    if form.comment_8.data:
      todos["todos"][todo_id]["comments"][7][0] = form.comment_8.data
    if form.comment_9.data:
      todos["todos"][todo_id]["comments"][8][0] = form.comment_9.data
    if form.comment_10.data:
      todos["todos"][todo_id]["comments"][9][0] = form.comment_10.data
    if form.comment_11.data:
      todos["todos"][todo_id]["comments"][10][0] = form.comment_11.data
    if form.comment_12.data:
      todos["todos"][todo_id]["comments"][11][0] = form.comment_12.data
    if form.comment_13.data:
      todos["todos"][todo_id]["comments"][12][0] = form.comment_13.data
    if form.comment_14.data:
      todos["todos"][todo_id]["comments"][13][0] = form.comment_14.data
    if form.comment_15.data:
      todos["todos"][todo_id]["comments"][14][0] = form.comment_15.data
    if form.comment_16.data:
      todos["todos"][todo_id]["comments"][15][0] = form.comment_16.data
    if form.comment_17.data:
      todos["todos"][todo_id]["comments"][16][0] = form.comment_17.data
    if form.comment_18.data:
      todos["todos"][todo_id]["comments"][17][0] = form.comment_18.data
    if form.comment_19.data:
      todos["todos"][todo_id]["comments"][18][0] = form.comment_19.data
    if form.comment_20.data:
      todos["todos"][todo_id]["comments"][19][0] = form.comment_20.data

    # new_comment
    if form.new_comment.data:
      todos["todos"][todo_id]["comments"].append([form.new_comment.data, today])

    # reminder
    if form.reminder.data:
      todos["todos"][todo_id]["rem_time"] = str(form.reminder.data)

    new_tags = form.tags.data
    lnew_tags_temp = new_tags.replace(" ", ",").split(",")
    lnew_tags = list(filter(None, lnew_tags_temp))
    todos["todos"][todo_id]["tags"] = lnew_tags

    dump_todos_to_json()
    return redirect("/open")

  return render_template("edit.html", form=form, todo=todo_dic)


@app.route("/todo/close/<int:todo_id>", methods=["GET", "POST"])
def close_todo(todo_id):
  todo_id = str(todo_id)
  todo_dic = todos["todos"].get(todo_id)
  form = PostForm()
  if request.method == "POST":
    today = str(datetime.date.today())

    # result
    if form.result.data:
      todos["todos"][todo_id]["result"] = [form.result.data, today]

    todos["todos"][todo_id]["status"] = "closed"

    dump_todos_to_json()
    return redirect("/open")

  return render_template("close.html", form=form, todo=todo_dic)


@app.route("/todo/reopen/<int:todo_id>")
def reopen_todo(todo_id):
  todo_id = str(todo_id)
  todos["todos"][todo_id]["status"] = "open"
  dump_todos_to_json()
  return redirect("/open")


@app.route("/new_todo", methods=["POST"])
def create_todo():
  today = str(datetime.date.today())

  new_title = request.form["new_todo_title"]

  new_tags = request.form["new_todo_tags"]
  lnew_tags_temp = new_tags.replace(" ", ",").split(",")
  lnew_tags = list(filter(None, lnew_tags_temp))

  new_todo_reminder = request.form["new_todo_reminder"]

  todos["ids"] += 1
  new_id = str(todos["ids"])
  todos["todos"][new_id] = {
      "id": new_id,
      "title": new_title,
      "status": "open",
      "comments": [],
      "tags": lnew_tags,
      "result": "",
      "date_added": today,
      "rem_time": new_todo_reminder,
  }
  dump_todos_to_json()
  return redirect("/open")


@app.route("/tag/<tag>")
def filter_by_tag(tag, comments=False):
  lto_remind = get_ids_to_remind()
  lused_tags1, lused_tags2 = get_used_tags()
  return render_template("tag.html", todos=todos, comments=comments, id_comments=None, ids_to_remind=lto_remind, used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=tag, )


@app.route("/<tag>/<int:todo_id>")
def one_comments_tag(tag, todo_id):
  lto_remind = get_ids_to_remind()
  lused_tags1, lused_tags2 = get_used_tags()
  todo_id = str(todo_id)
  return render_template("tag.html", todos=todos, comments=False, id_comments=todo_id, ids_to_remind=lto_remind, used_tags1=lused_tags1, used_tags2=lused_tags2, tag_filter=tag, )


# @app.route("/tag/<tag>/<int:todo_id>/<status>")
# def change_status_todo_tag(tag, todo_id, status):
#   todo_id = str(todo_id)
#   todos["todos"][todo_id]["status"] = status
#   dump_todos_to_json()
#   return redirect("/tag/" + tag)
