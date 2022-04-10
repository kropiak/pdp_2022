# Zadanie 1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji input).
def zadanie_1():
    zdanie = input('Wpisz jakieś zdanie.\n')
    print(f"W zdaniu jest {zdanie.count(' ')} spacji.")


def zadanie_1_alternatywnie():
    zdanie = input('Wpisz jakieś zdanie.\n')

    return zdanie.count(' ')


def zadanie_2():
    import sys

    print("Wprowadź pierwszą liczbę:")
    # metoda readline dodaje \n (znak nowego wiersza) na końcu każdej pobranej linii
    liczba_1 = sys.stdin.readline()
    print("Wprowadź drugą liczbę:")
    liczba_2 = sys.stdin.readline()

    wynik = int(liczba_1.strip()) * int(liczba_2.strip())
    # metoda write oczekuje obiektu typu str na wejściu (print rzutuje automatycznie, write nie)
    sys.stdout.write(str(wynik))

def zadanie_3():
    liczby = input('Podaj trzy liczby oddzielone spacją\n')  # obiekt typu str
    liczby = liczby.split(' ')  # obiekt typu list
    a = int(liczby[0])
    b = int(liczby[1])
    c = int(liczby[2])

    # przykład
    # a = 7
    # b = 6
    # c = 7

    if a > 0 and a <= 10 and (a > b or b > c):  # True and True and (True) -> True
        print('Wszystkie warunki spełnione')
    else:
        print('Warunki nie są spełnione')


def zadanie_4():
    # case 1
    for x in range(0, 50):
        if x % 5 == 0:
            print(x)

    # case 2
    for x in range(0, 50, 5):
        print(x)


def zadanie_5():
    while True:
        liczby = input('Podaj liczby oddzielone spacją\n')
        # warunek stopu funkcji
        if len(liczby) == 0:
            break

        liczby = liczby.split(' ')

        for index, elem in enumerate(liczby):
            liczby[index] = int(elem)

        # wyświetlamy kwadraty tych liczb
        for liczba in liczby:
            print(f'kwadrat liczby {liczba} to {liczba**2}')

def zadanie_6():
    lista = []
    while True:
        wejscie = input('Podaj liczbę\n')
        # warunek stopu

        if wejscie == 'stop':
            break
        if wejscie.isnumeric():
            lista.append(int(wejscie))

    return lista


def zadanie_7():
    wejscie = input('Podaj liczbę\n')
    suma = 0

    for znak in wejscie:
        if znak.isdigit():
            suma = suma + int(znak)

    print(f'Suma cyfr z {wejscie} to {suma}')


def zadanie_8():
    poziom_wiezy = int(input())
    # pętla dla linii
    for linia in range(1, poziom_wiezy+1):
        # pętla dla znaków w linii
        for litera in range(linia):
            print('A', end='')
        print()


def zadanie_8_bardziej_optymalnie():
    poziom_wiezy = int(input('Podaj wysokość drzewka\n'))
    znak = input('Podaj znak dla drzewka\n')
    # pętla dla linii
    for linia in range(1, poziom_wiezy+1):
        print(znak * linia)


# type hints - podpowiadanie typu, sugerowanie typu
def zadanie_8_bardziej_optymalnie_2(wysokosc: int, znak: str) -> None:
    # poziom_wiezy = int(input('Podaj wysokość drzewka\n'))
    # znak = input('Podaj znak dla drzewka\n')
    # pętla dla linii
    for linia in range(1, wysokosc+1):
        print(znak * linia)


# dodanie parametru tabliczki
def zadanie_9(n=10):
    # krok 1 - wypisanie etykiet kolumn
    for etykieta in range(0, n+1):
        if etykieta == 0:
            print("    ", end=' ')
        else:
            print(f'{etykieta:>4}', end=' ')
    print()
    # krok 2 - wypisujemy jedną etykietę wiersza i wszystkie wartości w danym wierszu
    for wiersz in range(1, n+1):
        print(f'{wiersz:>4}', end=' ')
        for kolumna in range(1, n+1):
            print(f'{wiersz * kolumna:>4}', end=' ')
        print()


if __name__ == '__main__':

    # ilosc_spacji = zadanie_1_alternatywnie()
    # print(f"W zdaniu jest {ilosc_spacji} spacji.")

    # zadanie_1()
    # zadanie_2()
    # zadanie_3()
    # zadanie_5()
    # print(zadanie_6())
    # zadanie_7()
    # zadanie_8()
    # zadanie_8_bardziej_optymalnie_2(5, '#')
    # zadanie_8_bardziej_optymalnie_2(3, 'E')
    # zadanie_8_bardziej_optymalnie_2(znak='.', wysokosc=5)
    # zadanie_8_bardziej_optymalnie_2(4)
    # zadanie_8_bardziej_optymalnie_2(znak='#')
    zadanie_9()
    zadanie_9(12)
    zadanie_9(100)




