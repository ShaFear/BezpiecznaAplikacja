# coding=utf-8


from flask import session, Blueprint, render_template, request

from modules.others.Settings import prefix, path_root
from modules.others.DatabaseUTILS import cur_execute


sign_in_api = Blueprint('sign_in_api', __name__)


@sign_in_api.route(prefix, methods=["GET"])
def index():
    if 'login' in session:
        return logged()
    else:
        return not_logged()


def logged():
    return render_template("menu.html", user=str(session["login"]), path_root=path_root)


def not_logged():
    return render_template("signIn.html", path_root=path_root)


@sign_in_api.route(prefix + 'signIn', methods=['POST'])
def sign_in():
    login = request.form['login']
    password = request.form['password']
    results = cur_execute("SELECT 1 FROM users WHERE login = ? AND password = ?", (login, password))
    if len(results) > 0:
        session["login"] = login
        return render_template("menu.html", user=str(session["login"]), path_root=path_root)
    else:
        return "nie zalogowano"
