# coding=utf-8


from flask import Blueprint, session, redirect, request

from modules.others.Settings import prefix, path_root


log_out_api = Blueprint('log_out_api', __name__)


@log_out_api.route(prefix + 'logout', methods=['GET'])
def log_out():
    if not 'login' and 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    session.clear()
    return redirect(prefix)