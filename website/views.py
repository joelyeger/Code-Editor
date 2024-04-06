from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

views = Blueprint('views', __name__)
variables = {'cur': None, 'first': False}
cur = None


@views.route('/', methods=['GET', 'POST'])

def home():
    if variables["first"] and variables["cur"] is None:
        return redirect(url_for('views.wait'))

    else:
        variables["first"] = True
        print("first connection is here, you must be the teacher")
        return render_template("home.html")


@views.route('/hello', methods=['GET', 'POST'])
def hello():

    variables["cur"] = 'views.hello'
    return render_template("hello.html")


@views.route('/counter', methods=['GET', 'POST'])
def counter():
    variables["cur"] = 'views.counter'

    return render_template("counter.html")


@views.route('/counter2', methods=['GET', 'POST'])
def counter2():
    variables["cur"] = 'views.counter2'

    return render_template("counter2.html")


@views.route('/filter', methods=['GET', 'POST'])
def filter():
    variables["cur"] = 'views.filter'

    return render_template("filter.html")


@views.route('/wait', methods=['GET', 'POST'])
def wait():
    if variables["cur"] is None:
        return render_template("wait.html")
    return redirect(url_for(variables["cur"]))

@views.route('/text', methods=['GET', 'POST'])
def text():
    variables["cur"] = 'views.text'

    return render_template("text.html")
