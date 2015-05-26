# coding=utf-8


from flask import Blueprint, request, session, render_template
from modules.others.Settings import path_root
from modules.others.Settings import prefix
from modules.others.DatabaseUTILS import cur_execute


notes_api = Blueprint('notes_api', __name__)


@notes_api.route(prefix + 'addNote', methods=['POST'])
def new_note():
    note = request.form['newnote']
    cur_execute("INSERT INTO " + session["login"] + " VALUES(?)", (note, ))
    return render_template("menu.html", user=str(session["login"]), path_root=path_root)


@notes_api.route(prefix + 'myNotes', methods=['GET'])
def my_notes():
    result = u""
    i = 0
    for note in cur_execute("SELECT * FROM " + session["login"]):
        i += 1
        result += u"<b>Notatka numer: " + str(i) + "</b>"
        result += u"</br>"
        result += note[0]
        result += u"</br></br>"
    return result


