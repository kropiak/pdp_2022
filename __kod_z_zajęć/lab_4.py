
def test():
    # instrukcja warunkowa, instrukcje zależne od siebie
    liczba = 0
    if liczba < 10:
        print('To dość mała liczba')
    elif 9 < liczba < 100:  # to jest wersja skrócona warunku
        print('To już całkiem duża liczba')
    else:
        print('To musi być wielka liczba')

    # obiekt typu bool
    imie = 'Ala'
    if isinstance(imie, str):
        print(f'Zmienna imie jest typu str')



if __name__ == '__main__':
    # print("Bezpośrednio")
    # test()

    # for dla listy
    # for i in [4, 5, 6]:
    #     print(i)

    # a = input("Tu jest jakiś komunikat np. Podaj liczbę\n")
    a = input("Wprowadź liczbę całkowitą:\n")
    lista = [a]
    print(lista)

    import sys

    print("Podaj jakiś tekst")
    s = sys.stdin.readline()  # Wczytuje wiersz
    print("Twój tekst to: " + s, end='')
    # Do wydruku można użyć też komendy write np.
    lista.append(s)
    print(lista)
    sys.stdout.write(s)

