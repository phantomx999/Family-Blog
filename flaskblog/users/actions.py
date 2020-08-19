import os, secrets
from flask import current_app
from flask import url_for
from flaskblog import mail
from flask_mail import Message
from PIL import Image


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no change will occur
'''
    mail.send(msg)

def save_pic(form_pic):
    pic_resize = (120, 120)
    _, file_ext = os.path.splitext(form_pic.filename)
    random = secrets.token_hex(8)
    picture_filename = random + file_ext
    profile_pics = os.path.join(current_app.root_path, 'static/profile_pics/', picture_filename)
    new_size_pic = Image.open(form_pic)
    new_size_pic.thumbnail(pic_resize)
    new_size_pic.save(profile_pics)
    return picture_filename
