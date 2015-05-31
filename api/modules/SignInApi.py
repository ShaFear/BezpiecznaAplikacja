# coding=utf-8


from flask import session, Blueprint, render_template, request, redirect
import time, datetime

from modules.others.Settings import prefix, path_root
from modules.others.DatabaseUTILS import cur_execute
from modules.security.Password import pass_to_key

sign_in_api = Blueprint('sign_in_api', __name__)


@sign_in_api.route(prefix, methods=["GET"])
def index():
    if 'login' and 'ip' in session:
        if session["ip"] == str(request.remote_addr):
            return logged()
        return not_logged()
    else:
        return not_logged()


def logged():
    return render_template("menu.html", user=str(session["login"]), path_root=path_root)


def not_logged():
    return render_template("signIn.html", path_root=path_root)


@sign_in_api.route(prefix + 'signIn', methods=['POST'])
def sign_in():
    if "wrongPasswordCount" in session:
        if session["wrongPasswordCount"] == 3:
            return render_template("forgetPassword.html", path_root=path_root,
                                   info=u'Wpisałeś błędne hasło 3 razy, możliwość logowania została zablokowana')
    login = request.form['login']
    password = request.form['password']
    password = pass_to_key(password)
    results = cur_execute("SELECT login FROM users WHERE login = ? AND password = ?", (login, password))
    time.sleep(3)
    if len(results) > 0:
        session["login"] = login
        session["ip"] = str(request.remote_addr)
        cur_execute("INSERT INTO " + session['login'] + "_ip" + " VALUES(?)", (str(datetime.datetime.now()) + ": " +
                                                                               str(request.remote_addr), ))
        return redirect(prefix)
    else:
        if not "wrongPasswordCount" in session:
            session["wrongPasswordCount"] = 1
        else:
            session["wrongPasswordCount"] = int(session["wrongPasswordCount"]) + 1
        return "nie zalogowano"
