# coding=utf-8


from flask import Blueprint, session, redirect, request

from modules.others.Settings import prefix, path_root


log_out_api = Blueprint('log_out_api', __name__)


@log_out_api.route(prefix + 'logout', methods=['GET'])
def log_out():
    session.clear()
    return redirect(prefix)