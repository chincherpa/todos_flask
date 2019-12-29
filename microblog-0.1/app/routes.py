from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World!"
    return render_template("index.html")


# from flask import Flask, render_template
# app = Flask(__name__, template_folder="templates")


# @app.route("/")
# def hello():
#     return render_template("index.html")