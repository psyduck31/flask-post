from flask import render_template, url_for, redirect
from website import app, db, login_manager
from website.forms import Add, Login
from website.models import User, Posts
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3


@app.route('/')
def home():
    conn = sqlite3.connect('website/site.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    all_rows = c.fetchall()
    return render_template('home.html', all_rows=all_rows)


@app.route('/post/<int:post_id>')
def post(post_id):
    if str(post_id).isdigit():
        conn = sqlite3.connect('website/site.db')
        c = conn.cursor()
        all_rows = c.execute('SELECT * FROM posts WHERE id = ?', str(post_id))
        return render_template('post_id.html', all_rows = all_rows)
    else:
        return 'Пожалуйста, вводите целые числа'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.password == form.password.data:
            login_user(user, remember=True)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/test')
def test():
    return str(current_user.username)


@app.route('/post/add')
def add():
    form = Add()
    if form.validate_on_submit():
        new_post = Posts(title=form.title.data, author_name=current_user.username, text=form.text.data, author_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
    return render_template('add.html', form=form)
