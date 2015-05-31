# BezpiecznaAplikacja

<h4>UROCHAMIANIE HTTP:</h4>
<p>1. Katalog "api" kopiujemy do katalogu www na lenie. (wiec bedzie login@len:~/www/api/)</p>
<p>2. W modules/others/Settings.py zmieniamy login na nasz.</p>
<p>3. Serwer uruchamiamy z katalogu "api" komenda "uwsgi uwsgi.ini"</p>

<h4>URUCHAMIANIE HTTPS:</h4>
<p>1. jak wyżej</p>
<p>2. jak wyżej</p>
<p>3. Serwer uruchamiamy z katalogu "api" komenda "python https.py"</p>
<p>4. Wklepujemy hasło "admin" (bardzo bezpieczne :P)</p>
<p>5. Gdyby port był zajęty to zmieniamy ręcznie w https.py</p>
<p>6. Zaleznie czy jest sie na lenie/volcie trzeba zmienic adres w https.py</p>
  
<h4>link do aplikacji:</h4>
<p>http: len.iem.pw.edu.pl/~login/apps/api</p>
<p>https: https://len.iem.pw.edu.pl:21000/~login/apps/api/ </p>
<p>https: https://volt.iem.pw.edu.pl:21000/~login/apps/api/ </p>

<p>Framework: Flask, Baza danych: sqlite3</p>

<h3> Zadania dla Ciebie :-) </h3>
<p> Napisanie funkcji weryfikujacych input wedle wytycznych w komentarzach</p>
<a href="https://github.com/ShaFear/BezpiecznaAplikacja/blob/master/api/modules/security/InputValidation.py">InputValidation.py</a><p> Napisanie funkcji, ktora policzy entropie (calculate_entropy) w js </p>
<a href="https://github.com/ShaFear/BezpiecznaAplikacja/blob/master/api/templates/signUp.html">signUp.html</a>
