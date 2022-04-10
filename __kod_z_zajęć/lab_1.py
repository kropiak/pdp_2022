# print('Hello world!')
# print("Hello world!")
# print("""Hello world!""")
#
# # komentarz jednowierszowy
# # Ctrl + d - zduplikowanie linii kodu
# # Ctrl + s - zapisanie zmian
# # Ctrl + / - zakomentowanie zaznaczonych linii/lub bieżącej linii
# # int liczba = 5 -> język c
#
# # print(type(5))
# # print(type('Ala'))
# # print(type(5.0))
#
# print(type(1 / 1))  # rzutowanie (zmiana) typu - tu float
# print(type(1 // 1))  # rzutowanie (zmiana) typu - tu int (obcinanie części dziesiętnej)
#
# # import this - easter egg z manifestem Tima Petersa
#
# liczba = 1
# # liczba++ - w językach c-podobnych oznacza post-inkrementację
# liczba += 1
# # równoważne z
# liczba = liczba + 1
#
# # konkatenacją (ang. concatenate) łańcuchów znaków
# full_name = "Krzysztof" + " " + "Ropiak"
# print(full_name)
#
#
# # błąd czasu wykonania - runtime error
# # name_and_age = "Krzysztof" + " " + "Ropiak" + ", wiek:" + 40
#
# class Osoba:
#
#     # przesłanianie metody __str__ z klasy object
#     # w javie nazywa toString(), w C# ToString()
#     def __str__(self):
#         return "Klasa typu Osoba"
#
#
# damian = Osoba()
# print(damian)
# # jeżeli domyślnie to wywołuje __str__ z klasy bazowej object
# # <__main__.Osoba object at 0x000001C73BBD3FD0>
#
# # rzutowanie liczby typu int na obiekt (typ) str -> str(40)
# name_and_age = "Krzysztof" + " " + "Ropiak" + ", wiek:" + str(40)
# wiek = 40
# name_and_age = "Krzysztof" + " " + "Ropiak" + ", wiek:" + str(wiek)
# print(name_and_age)
#
# # spam = "SPAM " * 10
# # print(spam)
# print("SPAM " * 10)  # konkatenacja łańcucha n razy
#
# # liczba_1 = 1
# # liczba_2 = 1
# #
# # if liczba_1 == liczba_2:
# #     print("Liczby są takie same.")
# #
# # # Shift + Tab - usuwa jedno wcięcie w zaznaczonym kodzie
# # if liczba_1 is liczba_2:
# #     print("Liczby są takie same.")
# #
# # print(id(liczba_1))
# # print(id(liczba_2))
# #
# # # teraz nastąpi zmiana
# # liczba_1 = liczba_1 + 1
# # if liczba_1 is liczba_2:
# #     print("Liczby są takie same.")
# #
# # print(id(liczba_1))
# # print(id(liczba_2))
# #
# #
# # liczba_1 = liczba_1 - 1 # znowu wartość 1
# # if liczba_1 is liczba_2:
# #     print("Liczby są takie same.")
# #
# # print(id(liczba_1))
# # print(id(liczba_2))
#
# lista_1 = [1, 2, 3]
# lista_2 = [3, 4, 5]
#
# print(id(lista_1))
# print(id(lista_2))
#
# # przypisanie przez referencję (odwłowanie do pamięci)
# # zamiast przypisania przez wartość
# lista_3 = lista_1
# lista_3.append(4)
# print(lista_3)
# print(lista_1)
#
# # przypisanie kopii listy
# lista_3 = lista_1.copy() # zwracana nowa lista (kopia płytka lista_1)
# lista_3.append(4)
# print(lista_3)
# print(lista_1)
#
# nic = None
# print(nic)
# print(type(nic))
#
# fałsz = False
# print(fałsz)
# print(type(fałsz))
#
# imie = ''
# if imie: # False
#     print("Pusty string")
# if imie == False: # tutaj porównane zostanie czy '' == False, co nie jest prawdą
#     print("Pusty string")
#
# imie = 'Adam'
# # case sensitive (wielkość znaków ma znaczenie)
# print(imie.count(''))
#
# # 3.04.2022
#
#
# artykul = """Recenzja "Władcy Pierścieni"."""
# artykul = r"Recenzja \n 'Władcy Pierścieni'." # r - raw (surowy), ignorowanie znaków specjalnych
# artykul = "Recenzja \"Władcy Pierścieni\"." # użycie znaku ucieczki
osoba = 'Krzysztof'
hobby = "piłka nożna"

print(osoba[0])
print(type(osoba[0]))
print(osoba[-1]) # ostatni element

print(osoba[:6:2]) # stop - exclusive (z wyłączeniem jego wartości)
print(osoba[::-1])

# imie[-1] = '' # typ str jest niemutowalny
osoba = osoba.lower() # wywołanie metody na instancji obiektu typu str
print(osoba)
osoba = 'Krzysztof'
print(osoba)
osoba = str.lower(osoba) # wywołanie klasowe
print(osoba)

cos = osoba.upper # alias do metody
print(cos)
print(cos()) # wywołanie metody upper poprzez alias

# konkatenacja łańcucha znaków
osoba = osoba[0].upper() + 's' + osoba[2::]
print(osoba)

# imie.count('s')
# print(len(imie))
#
#
# name_and_age = "Krzysztof" + " " + "Ropiak" + ", wiek:" + str(40)
# imie.format()

print('Lubię {0} język {0} oraz {0}'.format('Java', 'Python'))
osoba = 'Marek'
print('Witaj {}!'.format(osoba))
print(f'Witaj {osoba}!')
print(f'Wynik dodawania 33.33 oraz 66.67 to {33.33 + 66.67: .4f}')

# print('{:4d}'.format(42))
# print('{:4d}'.format(42))
#
# print('{:.32f}'.format(3.141592653589793))
numer = 100.1234545435
print('{:>8.2f}'.format(numer))
print('{:>8.2f}'.format(23))
print('{:>8.2f}'.format(14.3))
# print('{:06.2f}'.format(numer))
# print('{:07.2f}'.format(numer))

print('Lubię język {1} oraz {0}'.format('Java', 'Python'))
java = 'Java'
python = 'Python'
print('Lubię język ' + java + ' oraz ' + python)
wersja = 3.9
print('Lubię język ' + java + ' oraz ' + python + ' w wersji ' + str(wersja))
# f-string
osoba = 'Basia'
magia = 'abracadabra'

print(f'Lubię język {magia.count(osoba[-1])} oraz {python} w wersji {wersja}')



