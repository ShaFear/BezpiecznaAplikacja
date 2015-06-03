# coding=utf-8


import os
from os import environ

from flask import Flask

from modules.SignInApi import sign_in_api
from modules.SignUpAPI import sign_up_api
from modules.NotesAPI import notes_api
from modules.LogOutApi import log_out_api
from modules.ForgetPasswordAPI import forget_password_api
from modules.newConnections import new_connections_api
from modules.ChangePasswordAPI import change_password_api

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(24)


# dodawanie modułów do aplikacji
app.register_blueprint(sign_in_api)
app.register_blueprint(sign_up_api)
app.register_blueprint(notes_api)
app.register_blueprint(log_out_api)
app.register_blueprint(forget_password_api)
app.register_blueprint(new_connections_api)
app.register_blueprint(change_password_api)


if __name__ == '__main__':
    app.run(host='192.168.1.9',port=environ.get("PORT", 80))