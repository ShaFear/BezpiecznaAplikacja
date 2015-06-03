# coding=utf-8
__author__ = 'shafe_000'

import re


# login powinien zawierać min. 3 znaki, maksimum 16
# login nie może posiadać innych znaków niż alfabet angielski + cyfry (Bardzo ważne! nic innego nie może przejść!)
# login nie może się nazywać "users" (bo mi zamaże bazę danych ;__; )


def verify_login(login):

	if 2 < len(login) < 17:
		if re.search('users',login):
			return False
		elif re.search('[a-z]',login):
			if re.search('[A-Z]',login):
				if re.search('\d+',login):
					return True
				return True
			return True
        return False


#sprawdzenie bialych znakow jak sa false
#kolejno sprawdza dlugosc male litery duze litery i na koniec cyfry
#haslo min 9 max 15 znakow musi zawierac mala i duza litere oraz cyfre

def verify_password(password):

    if re.search('\s+', password):
        return False
    if 8 < len(password) < 16 and re.search('[a-z]',password) and re.search('[A-Z]',password) and re.search('\d+',password):
        return True
    return False


# imię matki i miejsce urodzenia
# łącznie mniej co najwyżej 64 znaki
# tylko polski alfabet i spacje


def verify_secret(city, mother):
    if 1 < len(city) and len(mother) > 1:
        if len(city) + len(mother) < 65:
		if re.search('[a-z]',city) and re.search('[a-z]',mother):
			if re.search('[A-Z]',city) and re.search('[A-Z]',mother):
				if re.search('\s+',city) and re.search('\s+',mother):
					return True
				return True
			return True
            
    return False


# notatka może mieć maksymalnie 255 znaków, (minimum 1 znak)

def verify_note(note):
    if 0 < len(note) < 256:
        return True
    return False