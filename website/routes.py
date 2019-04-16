from flask import render_template, url_for
from website import app, db
from website.forms import Add
import sqlite3


@app.route('/')
def home():
    return "Hello!"


@app.route('/post/<int:post_id>')
def post(post_id):
    return str(post_id)

"""
@app.route('/post/add')
def add():
    form = Add
"""
