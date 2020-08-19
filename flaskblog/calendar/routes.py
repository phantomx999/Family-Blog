from flask import Blueprint

from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (UpdateAccountForm, RegistrationForm,
                LoginForm, RequestResetForm, ResetPasswordForm)
from flaskblog.users.actions import save_pic, send_reset_email
from flask_login import login_user, current_user, logout_user, login_required

calendar = Blueprint('calendar', __name__)

@calendar.route('/calendar_page',  methods=['GET', 'POST'])
def calendar_page():
    return render_template('calendar/calendar_page.html', title='Calendar')
