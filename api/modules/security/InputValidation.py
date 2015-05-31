# coding=utf-8
__author__ = 'shafe_000'


# login powinien zawierać min. 3 znaki, maksimum 16
# login nie może posiadać innych znaków niż alfabet angielski + cyfry (Bardzo ważne! nic innego nie może przejść!)
# login nie może się nazywać "users" (bo mi zamaże bazę danych ;__; )


def verify_login(login):
    if 2 < len(login) < 17:
        return True
    return False


# hasło powinno zawierać co najmniej 1 cyfrę, 1 małą literę, 1 dużą literę
# hasło powinno zawierać min. 8 znaków, maksimum 16
# hasło powinno składać się tylko z znaków ascii


def verify_password(password):
    if 8 < len(password) < 16:
        return True
    return False


# imię matki i miejsce urodzenia
# łącznie mniej co najwyżej 64 znaki
# tylko polski alfabet i spacje


def verify_secret(city, mother):
    if 1 < len(city) and len(mother) > 1:
        if len(city) + len(mother) < 65:
            return True
    return False


# notatka może mieć maksymalnie 255 znaków, (minimum 1 znak)


def verify_note(note):
    if 0 < len(note) < 256:
        return True
    return False