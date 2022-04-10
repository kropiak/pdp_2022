# pakowanie krotki
krotka = 1, 2, 3, 4
print(type(krotka))
print(krotka)
krotka2 = (1, 2, 3, 4)

# to też jest krotka
krotka3 = 1,
print(type(krotka3))
print(len(krotka3))
print(len(krotka2))
print(krotka3)

# możemy również rzutować typy krotka - lista
lista = [1, 2, 'Ala', 'też', 'ma']
krotka_z_listy = tuple(lista)
print(krotka_z_listy)
# krotka_z_listy[0] = 3  błąd
nowa_krotka = 1, lista
print(nowa_krotka)
# to jest odwołanie do listy, więc jest mutowalna
nowa_krotka[1][0] = 3
print(nowa_krotka)

t = 5, 6, 7
print(t)
x, y, z = t
print(x, y, z)

imie, nazwisko, wiek = ('Adam', 'Malinowski', 34)
print(imie, nazwisko, wiek)

for elem in ['Adam', 'Malinowski', 34]:
    print(elem)


# przykład rozapkowania krotki z użyciem pętli for i enumerate
# enumerate zwraca krotke postaci (indeks zwaracanego elementu, kolejny element)
# możemy jej nie rozpakowywać
for elem in enumerate(['Adam', 'Malinowski', 34]):
    print(f'element {elem[0]+1} to {elem[1]}')

# lub ją rozpakować
for index, value in enumerate(['Adam', 'Malinowski', 34]):
    print(f'element {index+1} to {value}')

# ######################################################################
# zbiory (ang. set)

# inicjalizacja zbiorów
klasa = {'Marek', 'Janek', 'Ania', 'Ewa', 'Marek', 'Ania'}
print(klasa)  # duplikatów już nie ma

# a teraz zbiór znaków ze stringa
czar = set('czabunagunga')
print(czar)
inny_czar = set('abrakadabra')
print(inny_czar)
