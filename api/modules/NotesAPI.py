# coding=utf-8


from flask import Blueprint, request, session, redirect
from modules.others.Settings import prefix
from modules.others.DatabaseUTILS import cur_execute
import modules.security.Injection as Injection
import modules.security.InputValidation as InputValidation


notes_api = Blueprint('notes_api', __name__)


@notes_api.route(prefix + 'addNote', methods=['POST'])
def new_note():
    if not 'login' or not 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    note = request.form['newnote']
    note = Injection.changeText(note, False)
    if not InputValidation.verify_note(note):
        return "Błędny input"
    cur_execute("INSERT INTO " + session['login'] + " VALUES(?)", (note, ))
    return redirect(prefix)


@notes_api.route(prefix + 'myNotes', methods=['GET'])
def my_notes():
    if not 'login' or not 'ip' in session:
        return redirect(prefix)
    if not session["ip"] == str(request.remote_addr):
        return redirect(prefix)
    result = u""
    i = 0
    for note in cur_execute("SELECT * FROM " + session['login']):
        i += 1
        result += u"<b>Notatka numer: " + str(i) + "</b>"
        result += u"</br>"
        result += note[0]
        result += u"</br></br>"
    return result


