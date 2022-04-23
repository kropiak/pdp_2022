# Wprowadzenie do języka Python - lab 06

## **6. Zarządzanie pakietami**


Właściwie każdy popularny język programowania posiada mechanizm pozwalający na zarządzanie dodatkowymi bibliotekami czy pakietami. Python również posiada swojego menadżera pakietów o nazwie `pip`. W wersji 3.x nie jest konieczne jego ręczne instalowanie gdyż jest już domyślnie dołączany do tych dystrybucji.


Aby korzystać z narzędzia `pip` w wierszu poleceń systemu Windows musimy się najpierw upewnić, że interpreter Pythona (oraz folder `Scripts`) znajduje się w zmiennej środowiskowej `PATH`. Możemy albo wyświetlić zmienną `PATH`, albo po prostu w terminalu wykonać polecenie `python --version`, które zwróci wersję Pythona, z której aktualnie korzystamy lub polecenie nie zostanie rozpoznane.

Jeżeli powyższy warunek jest spełniony możemy uruchomić narzędzie `pip` i np. wyświetlić listę pakietów z aktualnego środowiska Pythona:
```console
python –m pip list
# lub
py -m pip list
# lub
pip list
```

Listę poleceń i skromny help uzyskamy po komendzie:
```console
python –m pip help
```

Index pakietów, które można zainstalować z indexy PyPi znajdziemy pod adresem https://pypi.python.org/pypi, gdzie aktualnie znajduje się ponad 300 000 pakietów…

Jak wynika z helpa komenda służąca do instalacji pakietu to `install nazwa_pakietu`. Zainstalujmy pakiet `requests`.
```console
python –m pip install requests
```

Możliwe jest również wybranie konkretnej wersji pakietu, którą chcemy zainstalować.
Jak nie trudno się domyślić opcja uninstall służy do odinstalowywania pakietów.

Narzędzie `pip` umożliwia również instalowanie pakietów na podstawie pliku wymagań, którego przykładowa postać może wyglądać tak:

```txt
# ####### example-requirements.txt ####### 
# ###### wymagania bez określonej wersji ###### 
nose
nose-cov
beautifulsoup4 

###### wymagania z okresloną wersją ###### 
# zobacz https://www.python.org/dev/peps/pep-0440/#version-specifiers 
docopt == 0.6.1 
# dopasowanie wersji. Musi być 0.6.1 
keyring >= 4.1.1 
# minimalna wersja 4.1.1 
coverage != 3.5 
# wykluczenie wersji. Wszystko poza wersją 3.5 
Mopidy-Dirble ~= 1.1 
# Kompatybilna wersja. Rozumiane jako >= 1.1, == 1.* 
# ###### odwołuje się do innego pliku z wymaganiami ###### 
-r other-requirements.txt 
# 
# 
###### konkretny plik z pakietem np. wcześniej pobrany ###### 
./downloads/numpy-1.9.2-cp34-none-win32.whl http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win_amd64.whl 
# 
###### dodatkowe pakiety bez określania wersji ###### 
# Umieszczone tutaj tylko po to, aby pokazać, że kolejność nie ma znaczenia. 
rejected 
green 
#
```
Komenda uruchamiająca instalację pakietów z pliku requirements.txt:
```console
python –m pip install –r requirements.txt
```

Są to podstawowe i najczęściej wykorzystywane komendy narzędzia PIP. Po bardziej szczegółową dokumentację wraz z przykładami odsyłam pod adres: https://pip.pypa.io/en/stable/.


## **7. Tworzenie wirtualnego środowiska pracy z pakietem virtualenv.**

Virtualenv jest skrótem od _virtual environment_ co oznacza wirtualne środowisko. Narzędzie to pozwala na tworzenie odrębnych środowisk zawierających interpreter Pythona oraz zestaw pakietów, które chcemy wykorzystać w konkretnym projekcie lub przed aktualizacją pakietów w projekcie produkcyjnym chcemy sprawdzić jak aplikacja będzie się zachowywała z nowszymi wersjami pakietów czy interpretera Pythona.

`Virtualenv` jest pakietem Pythona więc aby z niego skorzystać należy upewnić się, że stosowny pakiet jest zainstalowany i ewentualnie go zainstalować.

Aby stworzyć nowe środowisko wirtualne należy wskazać folder, w którym takie środowisko chcemy stworzyć. Następnie wykonanie komendy:

```console
python -m virtualenv nazwa_srodowiska
```

spowoduje stworzenie nowego folderu o nazwie `nazwa_srodowiska` w bieżącym folderze i skopiuje interpreter Pythona, który jest aktualnie obowiązującym dla uruchomionego modułu `virtualenv`. Dołączone zostaną też skrypty pozwalające m.in. na aktywację i deaktywację środowiska wirtualnego.

Kolejną czynnością, którą trzeba wykonać aby rozpocząć pracę w tym środowisku jest jego aktywacja, która polega na uruchomieniu skryptu z pliku `Scripts\activate` znajdującego się w folderze nowego środowiska. Od teraz aktywnym interpreterem jest ten zawarty w nowym środowisku. Możemy teraz uruchamiać skrypty Pythona, instalować pakiety oraz korzystać z konsoli Python w odniesieniu do tego środowiska.

Na zajęciach na podstawie dokumentacji ze strony https://virtualenv.pypa.io/en/stable/user_guide.html zostanie zaprezentowany sposób konfiguracji i korzystania ze środowiska wirtualnego.


## **8. Obsługa plików.**

> Dokumentacja : https://docs.python.org/3.8/tutorial/inputoutput.html#reading-and-writing-files

Przejdźmy od razu do omówienia kilku przykładów.

```python
uchwyt = open('plik.txt') 
uchwyt = open(r'C:\plik.txt', 'r')
```

Pierwsze polecenie otwiera plik, który znajduje się w folderze, w którym jest uruchamiany plik. Domyślnie plik otwierany jest tylko do odczytu. Drugie polecenie przyjmuje ścieżkę bezwzględną i dodatkowo kolejny parametr przekazuje tryb odczytu pliku, który tutaj również jest tylko do odczytu. Litera `r` poprzedzająca ścieżkę informuje Pythona, że ma potraktować ten ciąg tekstowy jako ciąg surowy (ang. raw) czyli nie będą brane pod uwagę ewentualne wystąpienia znaków specjalnych, które trzeba by poprzedzać znakiem „\”.

Podstawowy odczyt danych z pliku można wykonać tak:

```python
uchwyt = open('plik.txt') 
uchwyt = open(r'C:\plik.txt', 'r') 
dane = uchwyt.read() 
print(dane) 
uchwyt.close()
```

I tutaj możemy zauważyć pierwszy problem, jeżeli w pliku tekstowym znajdowały się polskie ogonki. Możemy temu zaradzić dodając dodatkowy parametr określający jak powinny być kodowane odczytywane znaki. Pamiętajmy również o zamykaniu uchwytu do pliku po odczytaniu danych.

```python
uchwyt = open(r'C:\plik.txt', 'r', , encoding='utf-8'))
```

Typy i nazwy kodowania można znaleźć pod adresem https://docs.python.org/3.7/library/codecs.html#standard-encodings.
Tryby otwarcia pliku przedstawione są w tabelce poniżej.

| Tryb | Opis |
|--|--|
r | Tylko do odczytu. Plik musi istnieć
w | Tylko do zapisu. Jeżeli pliku nie ma to zostanie utworzony a jeżeli jest to jego zawartość zostanie zapisana nową
a | Do dopisywania. Dane dopisuje się na koniec pliku. Jeśli plik nie istnieje to zostanie utworzony
r+ | Do odczytu i zapisu. Plik musi istnieć.
w+ | Do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony
a+ |Do odczytu i zapisu. Jeżeli plik nie istnieje zostanie utworzony.



Możemy również odczytywać plik linia po linii z pomocą pętli:

```python
uchwyt = open('plik.txt', 'r', encoding='utf-8') 

for linia in uchwyt: 
    print(linia) 
uchwyt.close()
```

W tym przypadku może pojawić się sytuacja, gdzie po każdej wyświetlonej linii na wyjściu będzie wypisywana nowa linia. To dlatego, że funkcja print dodaje na końcu znak `\n`, który oznacza nową linię, a jeżeli taki znak został również odczytany z pliku to mamy odpowiedź dlaczego tak się dzieje.

Aby to zmienić można ustalić wartość parametru 'end' funkcji print na inną niż domyślna wartość.


Możemy również określić jakiej wielkości fragmenty pliku wyrażone w bajtach. Tym razem z pomocą pętli while:

```python
uchwyt = open('plik.txt', 'r', encoding='utf-8') 

while True: 
    dane = uchwyt.read(1024) 
    print(dane, end='') 
    if not dane: 
        uchwyt.close() 
        break
```

Teraz kolej na zapisywanie do pliku.
```python
uchwyt = open('plik2.txt', 'w', encoding='utf-8') 
uchwyt.write('Zapisuję do pliku.') 
uchwyt.close()
```

Istnieje bardziej nowoczesna metoda dostępu do plików, której wykorzystanie zwalnia nas z obowiązku pamiętania o zamknięciu uchwytu do pliku. Ta metoda gwarantuje również zamknięcie uchwytu przy wystąpieniu wyjątku. To zalecane rozwiązanie przy obsłudze plików w Python 3.
```python
with open('plik.txt', 'r', encoding='utf-8') as file_reader: 
    for linia in file_reader:
        print(linia, end='')
```

Na koniec jeszcze przykład z obsługą wyjątków:

```python
try: 
    with open('plik.txt', 'r', encoding='utf-8') as file_reader: 
        for linia in file_reader: 
            print(linia, end='') 
except OSError: 
    print('Wystąpił wyjątek OSError')
```

Więcej informacji o wyjątkach, również związanych z obsługą plików znajdziemy pod adresem https://docs.python.org/3.8/library/exceptions.html#exception-hierarchy.


### **Moduł `json` oraz `csv`**


Obsługa nieustrukturyzowanych plików nie jest najwygodniejszym sposobem utrwalania danych. Jednym z najbardziej popularnych formatów przechowywania struktur danych jest format `json` (ang. JavaScript Object Notation), który pozwala na przechowywanie informacji o całych hierarchieach oiektów. Proces zapisywania nazywa się `serializacją` a odtwarzania struktury z pliku `deserializacją`. 

**Przykład 1**
```python
import json
import random

# lista
lista = [[random.randint(1, 100) for n in range(10)] for k in range(10)]

with open('dane_lista.json', 'w') as plik:
    json.dump(lista, plik)

with open('dane_lista.json', 'r') as plik:
    x = json.load(plik)

print(x)
print(type(x))

# słownik
slownik = {f'student_{x}': x**2 for x in range(1,11)}

with open('dane_slownik.json', 'w') as plik:
    json.dump(slownik, plik)

with open('dane_slownik.json', 'r') as plik:
    x = json.load(plik)

print(x)
print(type(x))

# typy inne niż list i dict nie działają out of the box
# ale można poszukać metod, które pozwalają zapisać inne struktury w
# postaci list lub słowników

class Pracownik:
    pass

p = Pracownik()
p.imie = 'Adam'
p.nazwisko = 'Malinowski'

# print(json.dumps(p)) # nie

# tak !
print(json.dumps(p.__dict__))
```

Format `csv` jest również bardzo popularny i mimo, że można go bez większych problemów obsługiwać za pomocą wbudowanych metod operujących na plikach oraz dzięki metodom `split()` oraz `join()` klasy `str` w dość efektywnie tworzyć i odtwarzać takie pliki mamy do dyspozycji moduł `csv`.

> Dokumentacja: https://docs.python.org/3.8/library/csv.html

**Przykład 2**
```python
import csv


lista = [[random.randint(1, 100) for n in range(10)] for k in range(10)]


# tworzymy plik csv korzystając z metody writerows, która przyjmuje iterowalny
# obiekt jako argument
with open('dane_lista.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lista)

# otwieramy zapisany wcześniej plik linia po linii
with open('dane_lista.csv', newline='') as f:
    reader = csv.reader(f)
    for wiersz in reader:
        print(wiersz)

# parametry pliku csv można dostosować
with open('dane_lista.csv', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for wiersz in reader:
        print(wiersz)

# przykład wykorzystania DictReader oraz DictWriter

# pierwszy wiersz w pliku traktowany jako lista kluczy słownika
# którym jest każdy zwracany wiersz
with open('dane.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for wiersz in reader:
        print(wiersz['Kraj'], wiersz['2006'])
    

# zapis
with open('dane_2.csv', 'w', newline='') as csvfile:
    kolumny = ['Kraj', '2020']
    writer = csv.DictWriter(csvfile, fieldnames=kolumny)

    writer.writeheader()
    writer.writerow({'Kraj': 'Polska', '2020': 37987654})
    writer.writerow({'Kraj': 'USA', '2020': 331002651})
```

## **Zadania**

**Zadanie 1**

Wczytaj plik `zamowienia.csv` i dokonaj w nim kilku przekształceń: 
* pozbądź się znaku `z` (właściwie zł) z kolumny `Utarg`
* zamień separator wartości dziesiętnej w tej samej kolumnie na `'.'`
* pozbądź się spacji jako separatora tysięcy w kolumnie `Utarg`
* zamień format daty w pliku na RRRR-MM-DD
  
Podziel plik na dwie części i zapisz je tak, aby dane dla każdego kraju (polska, Niemcy) znajdowały się w oddzielnych plikach.

**Zadanie 2**

Napisz funkcję, która przyjmuje listę plików oraz nazwę nowego pliku jako argumenty wejściowe. Funkcja scala zawartość plików w jeden plik wynikowy o podanej wcześniej nazwie.

### Zadania powtórzeniowe

**Zadanie 3**

Napisz funkcję, która będzie zwracała 3 największe wartości z listy numerycznej. Lista jest parametrem wejściowym funkcji.

**Zadanie 4**

Mając listę mieszana = [1, 2.3, ‘Zbyszek’, 5, ‘Marian’, 3.0] napisz funkcję, która zapisze wartości dla każdego typu do słownika gdzie
pod kluczem równym nazwie typu zmiennej (int, float, str, itp.) wartością będzie lista elementów z listy 'mieszana' danego typu.
Przykład: {‘int’: [1,5], ‘str’: [‘Zbyszek’,’Marian’]} itd.

**Zadanie 5**

Napisz funkcję:
- parametr wejściowy to lista stringów z nazwiskami
- funkcja zapisuje do dwóch oddzielnych plików o nazwach ‘A-M_nazwiska.txt’ oraz ‘N-Ż_nazwiska.txt’ odpowiednie nazwiska zpodanej listy 

**Zadanie 6**

Napisz funkcję, która wyświetla podany tekst odwracając kolejność liter w wyrazach. Np.
„Ala ma kota” wyświetli „alA am atok”

**Zadanie 7**

Napisz funkcję, która:
- jako parametr wejściowy pobiera zdanie wpisywane z klawiatury,
- ponownie z klawiatury pobiera nazwę pliku, w którym zapisany zostanie wynik działania funkcji,
- do pliku zapisywane są unikalne wyrazy ze zdania pisane małymi literami po jednym w linii,
- ze zdania zostaną usunięte ewentualne przecinki i kropki.

**Zadanie 8**

Napisz funkcję, która losuje 5 liczb całkowitych z przedziału <1, 20> dopóki w jednym losowaniu nie wystąpi 1 i 20. Wyświetl ilość
wykonanych losowań po spełnieniu warunku.

**Zadanie 9**

Napisz funkcję, która posiada zaszytą listę 3 nagród [‘samochód’, ‘10000 PLN’, ‘PS 4 Pro’]. Przygotuj plik z 10 imionami i nazwiskami
zapisanymi po 1 w wierszu. Następnie funkcja wczytuje plik, losuje zwycięzcę dla każdej z trzech nagród i zapisuje wyniki w pliku o
nazwie zwycięzcy.txt wpis postaci: Imię nazwisko, nagroda.

**Zadanie 10**

Napisz funkcję, która:
- „rozdaje” karty z talii 52 kart (np. As pik, Dama karo, itd.) dla 4 graczy
- karty rozdawane są bez powtórzeń po 5 dla każdego gracza
- wyświetlana jest informacja jak wygląda „ręka” każdego z graczy, np. Alan [As pik, 9 karo, itd.]

**Zadanie 11**

Napisz funkcję, która wczytuje z pliku zawierającego imiona i nazwiska studentów zapisane po jednym w linii, np.

Marek Markowski
Paweł Budzikowski

Funkcja generuje dla podanej listy adresy e-mail postaci: imie.nazwisko@uwm.edu.pl i zapisuje dane do nowego pliku dopisując przy wcześniejszym nazwisku wygenerowany adres, np.

Marek Markowski, marek.markowski@uwm.edu.pl itd. 

W nazwach e-mail powinny być zastępowane ewentualne polskie znaki (ż,ź
na z, ą na a itd.).

**Zadanie 12**

Przygotuj plik z kilkoma hasłami, które nadają się do gry 'Koło fortuny'. Wczytaj te hasła do listy i losuj jedno z nich. Na ekranie wyświetlaj hasło bez ujawniania poszczególnych liter, np.:`___ _____ ___ __ _______` dla hasła 'Bez pracy nie ma kołaczy'. Nastepnie w pętli pozwalaj uzytkownikowi na podawanie jednej litery, która będzie podstawiana w miejscach gdzie występuje lub wyświetlaj komunikat, że takiej litery nie ma w haśle. Dodaj też funkcjonalność, która pozwala na odgadnięcie (wpisanie) całego hasła.


**Zadanie 13**

Napisz funkcję, która będzie pobierała dwa parametry wejściowe:
* łańcuch znaków
* liczbę całkowitą

Funkcja ma skracać podany łańcuch znaków tak, żeby po dodaniu `...` na końcu jego długość nie była większa niż max (podany jako drugi parametr) i aby tekst nie był urwany w połowie wyrazu. Funkcja zwraca skrócony tekst.