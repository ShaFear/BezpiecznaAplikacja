# BezpiecznaAplikacja

UROCHAMIANIE HTTP:
1. Katalog "api" kopiujemy do katalogu www na lenie. (wiec bedzie login@len:~/www/api/)
2. W modules/others/Settings.py zmieniamy login na nasz.
3. Serwer uruchamiamy z katalogu "api" komenda "uwsgi uwsgi.ini"

URUCHAMIANIE HTTPS:
1. jak wyżej
2. jak wyżej
3. Serwer uruchamiamy z katalogu "api" komenda "python https.py"
4. Wklepujemy hasło "admin" (bardzo bezpieczne :P)
5. Gdyby port był zajęty to zmieniamy ręcznie w https.py

Model bazy danych:

Table users
(
  login varchar(16)
  password varchar(64)
)

Kazdy uzytkownik ma wlasna tabele:

Table uzytkownik
(
  note varchar(255)
)
  
link do aplikacji:
http: len.iem.pw.edu.pl/~login/apps/api
https: https://len.iem.pw.edu.pl:21000/~login/apps/api/

Framework: Flask, Baza danych: sqlite3
