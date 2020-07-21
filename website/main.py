from flask import (Blueprint, render_template, request, redirect)
from .db import get_db

bp = Blueprint('main', __name__)

@bp.route('/', methods=('GET', 'POST'))
@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        body: str = request.form['body'].replace('\r\n', 'BREAKLINE')
        db.execute("INSERT INTO posts (title, body) VALUES (?, ?)",
                            (title, body))
        db.commit()
    posts = db.execute("SELECT pid, dt, title, body FROM posts ORDER BY dt DESC").fetchall()
    return render_template('main/posts.html', posts=posts)

@bp.route('/delete', methods=('POST',))
def delete():
    db = get_db()
    pid = request.form['pid']
    # print([dict(r) for r in db.execute("SELECT * FROM posts ORDER BY dt DESC").fetchall()])
    db.execute("DELETE FROM posts WHERE pid = ?",
               (pid,))
    db.commit()
    return redirect('posts')

@bp.route('/projects')
def projects():
    p = []
    with open('website/data/projects.txt') as f:
        for section in f.read().split("---"):
            top, description = section.strip().split('\n')
            github, name = top.split('::')
            p.append({"github": github, "name": name, "description": description})
    return render_template('main/projects.html', p=p)

@bp.route('/about')
def about():
    abouts = []
    with open('website/data/about.txt') as f:
        for section in f.read().split("---"):
            qna = section.strip().split('\n')
            q = qna[0]
            a = qna[1:]
            abouts.append({"q": q, "a": a})
    return render_template('main/about.html', abouts=abouts)

@bp.route('/contact')
def contact():
    with open('website/data/contact.txt') as f:
        contacts = []
        for c in f.read().strip().split('\n'):
            contacts.append(c.split(': '))
    return render_template('main/contact.html', contacts=contacts)
