# coding=utf-8


import os

from flask import Flask

from modules.SignInApi import sign_in_api
from modules.SignUpAPI import sign_up_api
from modules.NotesAPI import notes_api
from modules.LogOutApi import log_out_api


app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(24)


# dodawanie modułów do aplikacji
app.register_blueprint(sign_in_api)
app.register_blueprint(sign_up_api)
app.register_blueprint(notes_api)
app.register_blueprint(log_out_api)


if __name__ == '__main__':
    app.run()