# coding=utf-8


import os

from flask import Flask
from os import environ

from modules.SignInApi import sign_in_api
from modules.SignUpAPI import sign_up_api
from modules.NotesAPI import notes_api
from modules.LogOutApi import log_out_api
from modules.ForgetPasswordAPI import forget_password_api

from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(24)


# dodawanie modułów do aplikacji
app.register_blueprint(sign_in_api)
app.register_blueprint(sign_up_api)
app.register_blueprint(notes_api)
app.register_blueprint(log_out_api)
app.register_blueprint(forget_password_api)


# https://len.iem.pw.edu.pl:21000/~jereczem/apps/api/


if __name__ == '__main__':
    app.run(host='volt.iem.pw.edu.pl',port=environ.get("PORT", 21000), processes=2,
        debug = False/True, ssl_context=context)