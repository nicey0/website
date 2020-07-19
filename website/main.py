from flask import (Blueprint, render_template, request)
from .db import get_db

bp = Blueprint('main', __name__)

def gen(l: int=64) -> str:
    return "aaaaa "*int(l/5)

@bp.route('/')
@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        db.execute("INSERT INTO posts (title, body) VALUES (?, ?)",
                            (title, body))
        db.commit()
    posts = db.execute("SELECT dt, title, body FROM posts ORDER BY dt DESC").fetchall()
    return render_template('main/posts.html', posts=posts)

@bp.route('/projects')
def projects():
    return render_template('main/projects.html')

@bp.route('/about')
def about():
    return render_template('main/about.html')

@bp.route('/contact')
def contact():
    return render_template('main/contact.html')
