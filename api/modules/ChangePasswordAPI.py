# coding=utf-8


from flask import Blueprint, render_template, request, session, redirect

from modules.others.DatabaseUTILS import cur_execute
from modules.others.Settings import prefix, path_root
from modules.security import InputValidation
from modules.security.Password import pass_to_key

change_password_api = Blueprint('change_password_api', __name__)


@change_password_api.route(prefix + 'generateNewPassword', methods=['POST'])
def forget_password_api_post():
    if not 'login' or not 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    login = session['login']
    password = request.form['password']
    new_password = request.form['new_password']
    if not InputValidation.verify_password(new_password):
        return "Błędny input"
    password = pass_to_key(password)
    new_password = pass_to_key(new_password)
    results = cur_execute("SELECT login FROM users WHERE login = ? AND password = ?", (login, password))
    if len(results) > 0:
        cur_execute("UPDATE users SET password=(?) where login = (?)", (new_password, login))
        return "Hasło zostało zmienione"
    return "Złe hasło"


@change_password_api.route(prefix + 'newPassword', methods=['GET'])
def forget_password_api_get():
    if not 'login' and 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    return render_template("newPassword.html", path_root=path_root)