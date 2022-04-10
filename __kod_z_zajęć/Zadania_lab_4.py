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


if __name__ == '__main__':

    # ilosc_spacji = zadanie_1_alternatywnie()
    # print(f"W zdaniu jest {ilosc_spacji} spacji.")

    # zadanie_1()
    # zadanie_2()
    zadanie_3()
