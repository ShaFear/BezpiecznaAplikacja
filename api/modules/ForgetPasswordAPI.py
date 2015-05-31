# coding=utf-8


from flask import Blueprint, render_template, request, session, redirect

from modules.others.DatabaseUTILS import cur_execute
from modules.others.Settings import prefix, path_root
from modules.security import InputValidation
from modules.security.Password import pass_to_key

forget_password_api = Blueprint('forget_password_api', __name__)


@forget_password_api.route(prefix + 'changePassword', methods=['POST'])
def forget_password_api_post():
    if 'login' and 'ip' in session:
        return redirect(prefix)
    login = request.form['login']
    password = request.form['password']
    mother = request.form['mother']
    city = request.form['city']
    if not (InputValidation.verify_login(login) and InputValidation.verify_password(password)) \
            and InputValidation.verify_secret(city, mother):
        return "Błędny input"
    password = pass_to_key(password)
    secret = mother + city
    secret = secret.encode('ascii', 'xmlcharrefreplace')
    secret = "(u'" + pass_to_key(secret) + "',)"
    res = cur_execute("SELECT login FROM users WHERE login = (?)", (login,))
    if len(res) == 0:
        return "Nie ma takiego użytkownika w bazie"
    real_secret = cur_execute("SELECT secret FROM users WHERE login = (?)", (login,))[0]
    if not str(secret) == str(real_secret):
        return "Złe dane, nie możemy utworzyć nowego hasła"
    cur_execute("UPDATE users SET password=(?) where login = (?)", (password, login))
    session["login"] = login
    return redirect(prefix)


@forget_password_api.route(prefix + 'forgetPassword', methods=['GET'])
def forget_password_api_get():
    if 'login' and 'ip' in session:
        return redirect(prefix)
    return render_template("forgetPassword.html", path_root=path_root)