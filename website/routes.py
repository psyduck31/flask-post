from flask import render_template, url_for, redirect, flash
from website import app, db, login_manager
from website.forms import Add, Login, Registration
from website.models import User, Posts
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3, time


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/')
def home():
    conn = sqlite3.connect('website/site.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    all_rows = c.fetchall()
    return render_template('home.html', all_rows=all_rows)


@app.route('/post/<int:post_id>')
def post(post_id):
    conn = sqlite3.connect('website/site.db')
    c = conn.cursor()
    all_rows = c.execute('SELECT * FROM posts WHERE id = ?', str(post_id)).fetchall()
    if all_rows == []:
        return render_template('404.html')
    else:
        return render_template('post_id.html', all_rows = all_rows)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=True)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/post/add', methods=['GET', 'POST'])
@login_required
def add():
    form = Add()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        new_post = Posts(title=title, author_name=current_user.username, text=text, author_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
    return render_template('add.html', form=form)


@app.route('/registration', methods=["GET", "POST"])
def registration():
    form = Registration()
    if form.validate_on_submit():
        if not form.username.data.isalnum():
            flash('В логине можно использовать только английские буквы и цифры', 'error')
        else:
            if User.query.filter_by(username=form.username.data).first():
                flash('Пользователь с таким логином уже сущесвует', 'error')
            else:
                if form.password.data == form.confirm_password.data:
                    new_user = User(username=form.username.data, password=form.password.data)
                    db.session.add(new_user)
                    db.session.commit()
                else:
                    flash('Введенные пароли не совпадают', 'error')
    return render_template('registration.html', form=form)
