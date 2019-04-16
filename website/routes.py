from flask import render_template, url_for
from website import app, db, login_manager
from website.forms import Add, Login
from website.models import User, Posts
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3


@app.route('/')
def home():
    return "Hello!"


@app.route('/post/<int:post_id>')
def post(post_id):
    return str(post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.password == form.password.data:
            login_user(user, remember=True)
    return render_template('login.html', form=form)


@app.route('/test')
def test():
    return str(current_user.username)

"""
@app.route('/post/add')
def add():
    form = Add
"""
