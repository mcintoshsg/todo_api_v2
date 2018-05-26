from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def my_todos():
    return render_template('index.html')