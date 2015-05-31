# coding=utf-8


from flask import Blueprint, request, session, redirect
from modules.others.Settings import prefix
from modules.others.DatabaseUTILS import cur_execute


new_connections_api = Blueprint('new_connections_api', __name__)


@new_connections_api.route(prefix + 'newConnections', methods=['GET'])
def new_connections():
    if not 'login' or not 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    result = u""
    i = 0
    for note in cur_execute("SELECT * FROM " + session['login'] + "_ip"):
        i += 1
        result += note[0]
        result += u"</br>"
    return result


