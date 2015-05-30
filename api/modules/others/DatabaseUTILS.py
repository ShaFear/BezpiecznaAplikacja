# coding=utf-8
__author__ = 'shafe_000'

import sqlite3

from modules.others.Settings import database_path


def cur_execute(data, args=()):
    con = sqlite3.connect(database_path)
    with con:
        cur = con.cursor()
        cur.execute(data, args)
        con.commit()
        return cur.fetchall()