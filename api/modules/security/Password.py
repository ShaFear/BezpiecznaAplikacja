# coding=utf-8
__author__ = 'shafe_000'


import hashlib


def pass_to_key(password):
    for i in range(256):
        salt = str(hashlib.md5("losowa_sol:" + str(i)).hexdigest())
        password = str(hashlib.sha256(password + salt).hexdigest())
    return password
