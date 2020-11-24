from flask import Blueprint, flash, g, redirect, render_template, request

from app.forms.register import RegisterForm

#bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None


    return render_template('auth/register.html', form=form)