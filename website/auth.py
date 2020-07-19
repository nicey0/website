import functools
from flask import (Blueprint, flash, g, redirect, render_template,
                   request, session, url_for)
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

with open('pass.txt', 'r') as pw:
    NICEY_PASS = pw.read()

@bp.before_app_request
def load_logged_user():
    g.nicey = session.get('nicey') is not None

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        password = request.form['password']
        if check_password_hash(NICEY_PASS, password):
            session.clear()
            session['nicey'] = True
            return redirect(url_for('index'))
        flash("incorrect password")
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is False:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
