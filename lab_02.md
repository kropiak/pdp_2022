# Wprowadzenie do języka Python - lab 02

## **1. Podstawowe typy danych**

Zanim przejdziemy do omawiania poszczególnych typów danych warto wiedzieć, że Python jest językiem „typowanym dynamicznie”. Oznacza to, że typ danych jaki zostanie wykorzystany do przechowania wartości przypisanej do zmiennej jest ustalony w momencie jej przypisania (operator '=') co znacznie różni się od sposobu w jaki typy są przypisywane do zmiennych w językach takich jak Java czy C++, gdzie w kodzie źródłowym określamy jaki typ danych (typ obiektu) będzie owa zmienna przechowywała.

Takie rozwiązanie ma zarówno wady jak i zalety. Do wad można zaliczyć to, że pierwotny typ zmiennej może ulec zmianie w dalszej części kodu co wymusza na programiście większą kontrolę tego co dzieje się z tą zmienną i czasami trzeba stosować funkcje, które sprawdzają typ przekazanych danych, jeżeli oczekujemy konkretnego typu. Nie możemy też w żaden sposób wymusić przekazania do metody danych określonego typu lub określić jaki typ danych zostanie zwrócony. Możemy jednak określić typ oczekiwany na etapie pisania kodu począwszy od wersji Pythona 3.5 a cały mechanizm nazywa się **type hinting** (zobacz: https://docs.python.org/3.8/library/typing.html). W późniejszym etapie zajęć zostaną zaprezentowane przykłady jego użycia. 
Zaletą dynamicznego typowania jest większa elastyczność języka i możliwość zmiany typu 'w locie' co eliminuje konieczność jawnego deklarowania nowych zmiennych do przechowywania danych pod postacią innego typu (rzutowanie jawne i niejawne). 

Kolejna istotna informacja jest taka, że Python jest językiem zorientowanym obiektowo i wszystko w Pythonie jest obiektem* o czym świadczy chociażby to, że właściwie wszystkie zmienne posiadają metody, które można na nich wykonać.

\* to stwierdzenie może nie być prawdą, jeżeli porównać definicje obiektu w innych językach programowania, ale z punktu widzenia Pythona i jego twórców jest prawdą. 

### **1.1.	KILKA SŁÓW O OPERATORACH**
Zanim omówione zostaną typy danych warto poznać kilka operatorów, które w powiązaniu ze zmiennymi są często używane.

**Listing 1**
```python
# operatory arytmetyczne

# operator dodawania
print(1 + 2)
# operator odejmowania
print(1 - 2)
# operator mnożenia
print(1 * 2)
# operator dzielenia z resztą
print(1 / 2)
# operator dzielenia bez reszty (dzielenie całkowite)
print(1 // 2)

# pamiętajmy o kolejności operacji arytmetycznych
suma = 1 + 2 * 3 / 4.0

# operatory przypisania
zmienna = "wartość" # przypisanie wartości do zmiennej
# są też skrócone postacie operatorów przypisania w połączeniu z innymi operatorami
suma = 10
suma += 1 
# to samo co
suma = suma + 1
# podobnie możemy używać operatorów -, *, /, //, **, % i operatorów bitowych (zachęcam do poczytania w dokumentacji)


# modulo czyli reszta z dzielenia
reszta = 12 % 5
# operator potęgowania
kwadrat = 5 ** 2
szescian = 5 ** 3

# operacje na zmiennych znakowych (string)
full_name = "Krzysztof" + " " + "Ropiak"

# tak też można
spam = "SPAM " * 10
print(spam)


# operatory porównania
liczba1 = 1
liczba2 = 2
print(liczba1 > liczba2)
print(liczba1 < liczba2)
print(liczba1 <= liczba2)
print(liczba1 >= liczba2)
print(liczba1 == liczba2)
print(liczba1 != liczba2)

# powyższe porównania zwrócą wartości typu bool czyli True lub False

prawda = True
falsz = False

# operatory logiczne
print(prawda and falsz) # koniunkcja logiczna
print(prawda or falsz) # alternatywa logiczba
print(not prawda) # negacja
print(not not prawda) # podwójna negacja
print(bool(prawda or falsz)) # użycie metody bool(), która jest tutaj wywołaniem konstruktora klasy bool (więcej w kolejnych labach)

# operatory tożsamości (identity)
liczba = 1
liczba2 = liczba

print(liczba is liczba2)
print(liczba is not liczba2)

# operatory przynależności (membership)
lista = [1, 2, 3, 4]
print(1 in lista)
print(5 not in lista)
```

Python w bardziej złożonych wyrażeniach wykonuje działania w określonej kolejności:

1.	najpierw **
2.	następnie *, / oraz %
3.	a dopiero na końcu + i -

W Pythonie jako fałsz traktowane są:
* liczba zero (0, 0.0, 0j itp.)
* False
* None
* puste kolekcje ([], (), {}, set() itp.)
* puste łańcuchy znakowe
* w Pythonie 2 – obiekty posiadające metodę __nonzero__(), jeśli zwraca ona False lub 0
* w Pythonie 3 – obiekty posiadające metodę __bool__(), jeśli zwraca ona False

### 1.2. Typy liczbowe.

Dwa główne typy liczbowe Pythona to liczba całkowita oraz rzeczywiste czyli **integer** i **float**. Jest jeszcze typ **complex**, który służy do przechowywania wartości liczb zespolonych, ale zapoznanie się z informacjami na jego temat pozostawiam czytelnikowi.

**Listing 2**
```python
całkowita = 5
rzeczywista = 5.6
rzeczywista = float(56)
# powyższy sposób to rzutowanie - zamiana jednego typu w inny o ile to możliwe
# poniżej kolejny przykład
liczba_str = '123'
liczba = int(liczba_str)
print(type(liczba))

# zmienne można również zadeklarować w jednej linii
a, b = 3, 4
```

W przypadku liczb rzeczywistych można również określić precyzję z jaką zostaną wyświetlone (ale nie przechwywane w pamięci), ale stosowny przykład znajduje się w kolejnym podrozdziale.

### **1.3. Typ tekstowy.**

We fragmentach kodu w poprzednich rozdziałach znalazło się już kilka przykładów deklaracji zmiennej typu string. Dla przypomnienia:

**Listing 3**
```python
artykul = """Recenzja "Władcy Pierścieni"."""
imie = 'Krzysztof'
hobby = "piłka nożna"
```

Powyższy fragment to tylko przykład różnych metod deklaracji, w trakcie zajęć będą stosowane apostrofy.

Ciąg tekstowy w Pythonie to tablica znaków co daje z miejsca wiele możliwości manipulacji i dostępu do składowych tego ciągu. Inna ważna cecha stringów to fakt, że po ich zadeklarowaniu nie możemy zmienić zadeklarowanych znaków ciągu, gdyż zmienne typu string są niemutowalne (ang. immutable). Oczywiście możemy nadpisać zmienną nową wartością czyli zmienić wartość przez przypisanie.
 

**Listing 4**
```python
imie = 'Krzysztof'
nazwisko = 'Ropiak'

# string to tablica znaków więc możemy odwołać się do jej elementów
print(imie[0])

# indeks elementu możemy również określać jako pozycja od końca ciągu
print(imie[-1])

# można również pobrać fragment ciągu (slice) określając jako indeks
# element początkowy i końcowy. Zwróć uwagę na wartość tych indeksów.
print(imie[0] + imie[-2] + imie[4:6])
# można również określic tylko jeden z dwóch indeksów
# co oznacza od elementu o indeksie 3 do końca łańcucha
print(imie + nazwisko[3:])

# ogólna postać slice
# [start:stop:step]
# wartości poszczególnych parametrów slice'a są pomijalne, ale
# musimy zapisywać drukropki, które informują mechanizm o tym
# które parametry zostaną uzyte z ich domyślnymi wartościami
# sprawdź działanie poniższych przykładów
print(imie[::2])
print(imie[-2])
print(imie[:-4:-1])
print(imie[::-1])

# inny sposób złączania ciągów
print(imie + ' ' + nazwisko)

# Elementów ciągu nie można zmieniać więc poniższa instrukcja zwróci błąd.
# nazwisko[0] = "P"

# Potwierdzeniem tego, że ciąg tekstowy jej również obiektem jest możliwość
# wykonania na nim metod dla tego typu zdefiniowanych. Metoda count() zlicza
# ilość wystąpień danego ciągu w wartości przechowywanej przez zmienną.
print(imie.count('z'))
# Co ciekawe w Pythonie możemy wywoływać funkcje dla danego obiektu już podczas deklaracji
# co na pierwszy rzut oka może wyglądać dość egzotycznie.
print('Jesteś szalona!'.count('a'))

# Potwierdzeniem niezmienności zadeklarowanego stringa może być również poniższy kod
print(imie.lower())
print(imie)

# Aby zwrócić długość ciągu tekstowego należy posłużyć się wbudowaną funkcją len()
print(len(nazwisko))
```

Ciągi tekstowe bardzo często są „dekorowane” innymi wartościami przed ich wydrukowaniem na konsolę. Ciąg wyjściowy może być zlepkiem innych ciągów i/lub liczb, ale nie możemy tak po prostu wykonać poniższej operacji:
`print('Ala ma ' + 4 + ' lata')`

Interpreter Pythona zwróci błąd z informacją, że nie może wykonać niejawnej konwersji z typu int na typ string. Poniżej listing z możliwościami jakie mamy do dyspozycji. Dzieje się tak dlatego, że operator ‘+’ w przypadku zmiennych typu string złącza je w jeden ciąg (konkatenacja ciągów) a dla zmiennych numerycznych wykonuje operację sumowania arytmetycznego.

**Listing 5**
```python
# formatowanie znane z Pythona 2.x
wyznanie = 'Lubię %s' % 'Pythona'
print(wyznanie)
wonsz = 'Python'
print('Lubię %sa' % wonsz)

print('Lubię %s oraz %sa' % ('Pythona', wonsz))

# %s oznacza, że w miejsce tego znacznika będzie podstawiany ciąg tekstowy
# %i - to liczba całkowita
# %f - liczba rzeczywista lub inaczej zmiennoprzecinkowa
# %x lub %X - liczba całkowita zapisana w formie szesnastkowej

print('Używamy wersji Python %i' % 3)
print('A dokładniej Python %f' % 3.9)
print('Chociaż lepiej to zapisać jako Python %.1f' % 3.9)
print('A kolejną glówną wersją Pythona może być wersja %.4f' % 3.11111)
print('A może będzie to wersja %.1f ?' % 3.111)
print('A może jednak %.f ?' % 3.12)
wersja = 4
print('A %i w systemie szesnastkowym to %X' % (wersja, wersja))
print('A %i * %i szesnastkowo daje %X' % (wersja, wersja, wersja*wersja))

# Chociaż możliwości przy korzystaniu z mechanizmów powyżej są spore,
# to i kilka wad się również znajdzie. Trzeba pilnować zarówno liczby argumentów jak
# i ich kolejności. Konieczne jest powielanie tej samej zmiennej jeżeli kilka
# razy jest wykorzystywana w formatowanym ciągu. Spójrzmy na inne możliwości.

print('Lubię %(jezyk)s' % {'jezyk': 'Pythona'})
print('Lubię %(jezyk)s a czy Ty lubisz %(jezyk)s ?' % {'jezyk': 'Pythona'})
# wadą jest dość duża ilość dodatkowego kodu do napisania, ale nazwy zmiennych
# w ciągu pozwalają na ich szybką identyfikację i wielokrotne wykorzystanie w
# dowolnej kolejności

# poniżej kolejny sposób
print('Lubię język {1} oraz {0}'.format('Java', 'Python'))

# w nowej wersji języka Python możliwe jest również odwoływanie się do elementów kolekcji
# lub pól klasy
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

kr = Osoba('Krzysztof', 'Ropiak')

print('Tą osobą jest {0.imie} {0.nazwisko}'.format(kr))
```

W wersji 3.6 wprowadzono do języka Python pojęcie **„f-string”**, które nieco upraszcza formatowanie ciągów tekstowych. Jest to obecnie zalecana i szeroko stosowana metoda. Przykład poniżej.

**Listing 6**	
```python
# zapis jest skróconą postacią użycia funkcji .format()
imie = 'Marek'
print(f'Witaj {imie}!')
print(f'Wynik dodawania 33.33 oraz 66.67 to{33.33 + 66.67: .4f}')

```

Po więcej przykładów związanych z formatowaniem łańcuchów można udać się pod poniższe adresy:

1.	https://docs.python.org/3/library/string.html#format-string-syntax
2.	https://pyformat.info/
3.	https://realpython.com/python-f-strings/

---

> **Ćwiczenia**

1.	Pobierz ze strony https://pl.lipsum.com/ tekst akapitu o tytule „Czym jest Lorem Ipsum” i przypisz go do zmiennej.

2. Korzystając ze zmiennej z zadania 1 wyświetl na konsoli tekst postaci:
„W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}” . W miejsca {liczba_liter1} oraz {liczba_liter2} podstaw zmienne, które będą przechowywały liczbę wystąpień danych liter (poszukaj odpowiedniej metody dla typu **str**). Litery, które należy wyszukać to 4-ta litera nazwiska oraz 3-cia litera imienia osoby wykonującej ćwiczenie, np. imie = „Krzysztof”, nazwisko = „Ropiak”, litera_1 = imie[2], litera_2 = nazwisko[3].

3.	Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem, wypełnieniem spacji itp.).

