# BezpiecznaAplikacja

1. Katalog "api" kopiujemy do katalogu www na lenie. (wiec bedzie login@len:~/www/api/)
2. W modules/others/Settings.py zmieniamy login na nasz.
3. Serwer uruchamiamy z katalogu "api" komenda "uwsgi uwsgi.ini"

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
len.iem.pw.edu.pl/~login/apps/api
