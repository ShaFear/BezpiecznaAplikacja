# coding=utf-8
__author__ = 'shafe_000'


import hashlib


def pass_to_key(password):
    salt = str(hashlib.md5("losowasol").hexdigest())
    for i in range(256):
        password = str(hashlib.sha256(password + salt).hexdigest())
    return password