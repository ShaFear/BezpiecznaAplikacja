# coding=utf-8
__author__ = 'shafe_000'


def changeText(s, quote=None):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
    return s