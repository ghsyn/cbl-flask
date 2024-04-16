from flask import render_template, jsonify, request, Blueprint
from flask_login import LoginManager

user = Blueprint('user', __name__, url_prefix='/user')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return ''


@user.route('/')
def view_page():
    print('user view call...')
    return render_template('views/users/user.html')
