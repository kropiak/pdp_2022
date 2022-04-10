slownik = {}
# slownik = dict([('jeden', 1), ('dwa', 2), ('trzy', 3)])
# slownik = dict(jeden=1, dwa=2, trzy=3)
# slownik = dict({'jeden': 1, 'dwa': 2, 'trzy': 3})
# slownik = {'jeden': 1, 'dwa': 2, 'trzy': 3}

slownik_liczb = {1: 'jeden', 2: 'dwa', 3: 'trzy'}
print(slownik_liczb[1])

# czy jeden jest wśród kluczy słownika
print('jeden' in slownik_liczb)
print('jeden' in slownik_liczb.keys())
print('jeden' in slownik_liczb.values())

slownik_liczb[4] = 'cztery'
print(slownik_liczb.keys())


# jako ciekawostka
# deklaracja klasy Osoba
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


adam = Osoba('Adam', 'Malinowski')
print(adam.__dict__)  # wyświetli wszystkie atrybuty klasy Osoba jako słownik

# zagnieżdżony słownik
slow = {'imiona': {1: 'Adam', 2: 'Alina'}}
print(slow['imiona'][2])  # zwróci tekst Alina

pl = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
}
en = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August'
}
months = {'pl': pl, 'en': en}

print(months['pl'][4])
print(months['en'][4])
# print(en[4])
# akronim SOLID -
# Marcin Aniserowicz

# zadanie 3
imie = 'Marianna'
slow = dict.fromkeys(imie, 1)
print(slow)
# lub
slow2 = {}
slow2 = slow2.fromkeys(imie, 1)
print(slow2)












# Ctrl + /