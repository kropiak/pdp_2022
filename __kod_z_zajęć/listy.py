import copy

lista = []
lista2 = list()
lista3 = [1, 2, 3]
lista4 = ['a', 5, 'Python', 7.8]

print(lista4.__len__()) # metoda magiczna - nie powinniśmy jej jawnie wywoływać
print(len(lista4))

# funkcja dir wyświetli wszystkie metody, których można uzyc dla podanego typu obiektu
print(dir('Ala'))
lista_liter = list('Ala')
print(lista_liter)
lista_liter[0] = 'O'
print(lista_liter)
print('Ala ma kota'.split())
print(','.join('Ala ma kota'.split()))
lista_liter.append('k')
print(lista_liter)

lista = []
lista.append([1, 2, 3])
lista.append(['a', 5, 'Python', 7.8])

print(lista)

lista = []
lista.extend([1, 2, 3])
lista.extend(['a', 5, 'Python', 7.8])
print(lista)

lista = []
lista = [1, 2, 3] + ['a', 5, 'Python', 7.8]
print(lista)

lista7 = [5, [9, 8, 2], 3, 1]
kopia_lista7 = lista7.copy() # shallow copy - kopia płytka

kopia_lista7 = copy.deepcopy(lista7) # kopia głęboka
# kopia_lista7 = copy.copy(lista7) # też kopia płytka
lista7[1][0] = 10
print(lista7)
print(kopia_lista7)
lista7[0] = 10
# lista7.sort() # in-place - zamienia postać listy na posortowaną
print(lista7)
print(kopia_lista7)

lista = [7, 9, 8, 2, 3, 1]
lista.sort()
print(lista)
lista.reverse()
print(lista)

# print(lista[6])
lista[6:] = [7]
print(lista)

lista[:3] = [12, 13, 14] # zamiana wartości wycinka listy
lista[:3] = [12, 13] # zmiana rozmiaru oryginalnej listy
print(lista)

nowa_lista = [0] + lista # działa jak extend
# czyli to samo co
# [0].extend(lista)


imie_lista = list('Adam')
# co da nam imie_lista = ['A', 'd', 'a', 'm']
# możemy teraz postawić pod dany element nowy string
imie_lista[0] = imie_lista[0].lower() # lub upper, capitalize, cokolwiek
# metoda join, zwraca obiekt typu str scalając (konkatenując) wszystkie elementy obiektu iterowalnego -  tu listy powielając za każdym razem string, na którym join użyliśmy
# przykład
print('|'.join(imie_lista))