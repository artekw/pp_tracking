# Konsolowy program do śledzenia przesyłek Poczty Polskiej


##Instalacja:

    $ sudo pip install docopt termcolor suds
    $ git clone https://github.com/artekw/pp_tracking
    $ cd pp_tracking
    $ chmod +x pp_tracking.py

##Użycie:

    $ pp_tracking.py <numer przesyłki>

##Działanie:

    $ pp_tracking.py RK376492XXXX
    ---------------------------------------------------------------------
    Przesyłka numer RK376492XXXX została doręczona
    ---------------------------------------------------------------------
    Kraj nadania:           Chiny
    Kraj przeznaczenia:     Polska
    Rodzaj przesyłki:       List polecony ekonomiczny
    ---------------------------------------------------------------------
    2016-07-18 15:49 | Doręczenie UP XXXXXX
    ---------------------------------------------------------------------
    2016-07-18 09:17 | Wydanie doręczycielowi UP XXXXX
    2016-07-18 09:17 | Wprowadzenie do księgi oddawczej UP XXXXX
    2016-07-15 01:48 | Przyjęcie przesyłki w Polsce WER Warszawa
    2016-06-20 16:10 | Wysłanie przesyłki z kraju nadania SHAXXX
    2016-06-12 16:11 | Nadanie 
    ---------------------------------------------------------------------


##TODO:

* śledzenie listy przesyłek z pliku


##Dokumentacja:

* https://fedorahosted.org/suds/wiki/Documentation
* http://www.poczta-polska.pl/webservices/
* http://docopt.org/
* https://pypi.python.org/pypi/termcolor

