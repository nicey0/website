from flask import (Blueprint, render_template, request, redirect)
from .db import get_db

bp = Blueprint('main', __name__)

@bp.route('/', methods=('GET', 'DELETE', 'POST'))
@bp.route('/posts', methods=('GET', 'DELETE', 'POST'))
def posts():
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        body: str = request.form['body'].replace('\r\n', 'BREAKLINE')
        db.execute("INSERT INTO posts (title, body) VALUES (?, ?)",
                            (title, body))
        db.commit()
    posts = db.execute("SELECT dt, title, body FROM posts ORDER BY dt DESC").fetchall()
    return render_template('main/posts.html', posts=posts)

@bp.route('/delete', methods=('DELETE',))
def delete():
    db = get_db()
    # dt = request.form['dt']
    title = request.form['title']
    body = request.form['body'].replace('\r\n', 'BREAKLINE')
    # print([dict(r) for r in db.execute("SELECT * FROM posts ORDER BY dt DESC").fetchall()])
    db.execute("DELETE FROM posts WHERE title = ? AND body = ?",
               (title, body))
    db.commit()
    return redirect('posts')

@bp.route('/projects')
def projects():
    return render_template('main/projects.html')

@bp.route('/about')
def about():
    return render_template('main/about.html')

@bp.route('/contact')
def contact():
    return render_template('main/contact.html')
