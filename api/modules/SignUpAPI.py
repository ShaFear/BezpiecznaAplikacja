# coding=utf-8


from flask import Blueprint, render_template, request, session, redirect

from modules.others.DatabaseUTILS import cur_execute
from modules.others.Settings import prefix, path_root
from modules.security import InputValidation
from modules.security.Password import pass_to_key

sign_up_api = Blueprint('sign_up_api', __name__)


@sign_up_api.route(prefix + 'signUp', methods=['POST'])
def sign_up_post():
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
    secret = pass_to_key(secret)
    res = cur_execute("SELECT login FROM users WHERE login = (?)", (login,))
    if len(res) > 0:
        return "Wybrany login już istnieje :-("
    cur_execute("INSERT INTO users VALUES(?, ?, ?)", (login, password, secret))
    cur_execute("CREATE TABLE " + login + " ( note charset(255) )")
    cur_execute("CREATE TABLE " + login + "_ip" + " ( note charset(64) )")
    session["login"] = login
    return redirect(prefix)


@sign_up_api.route(prefix + 'signUp', methods=['GET'])
def sign_up_get():
    if 'login' and 'ip' in session:
        return redirect(prefix)
    return render_template("signUp.html", path_root=path_root)