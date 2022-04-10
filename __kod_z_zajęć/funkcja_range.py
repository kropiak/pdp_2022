# metoda range

print(type(range(5)))
print(range(5))  # [0:5] -> 0,1,2,3,4

# print(list(range(0, 100, 2)))

sekwencja = range(1, 11)

sek_iter = iter(sekwencja)
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))
print(next(sek_iter))

# to samo poniżej
for elem in sekwencja:
    print(elem)

print(0.1 + 0.2 == 0.3)

print(0.1 + 0.2, 0.3)
# kiedy wyświetlimy liczby z większą precyzją to widać, że jest to ich przybliżenie
# tak jak liczba 3.333(3) jest przybliżeniem
print(f'{0.1:.32f}')
print(f'{0.2:.32f}')
print(f'{0.3:.32f}')

from decimal import *

print(0.1 + 0.2 == 0.3)  # kto by się spodziewał ?
print(round(0.1 + 0.2, 2) == round(0.3, 2))  # teraz lepiej
print((Decimal(0.1) + Decimal(0.2)) == Decimal(0.3))  # nie właściwe użycie klasy Decimal
print((Decimal('0.1') + Decimal('0.2')) == Decimal('0.3'))  # teraz już dobrze

# bardzo często w zależności od rozwiązywanego problemu
# wykorzystywane jest parametryzowanie funkcji range
n = 3
print(list(range(0, 16, n)))
n = 2
print(list(range(0, 16, n)))
