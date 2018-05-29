from flask import render_template

from . import main

@main.route('/')
def my_todos():
    return render_template('index.html')