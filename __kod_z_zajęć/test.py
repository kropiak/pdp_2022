"""
często używany do dokumentowania kodu - docstring
Sphinx
to jest skrypt ...
"""

# Pytania:

# 1. Dlaczego w 1 przypadku zwróciło "False",
# zamiast "True False", zaś w drugim wybrało True?

prawda = True
falsz = False
print(prawda and falsz) # wynik False - prawda tylko gdy True and True
print(prawda or falsz) # wynik True

# 2. Slice ma start:stop:step więc powinien zatrzymać się na "z",
# a potem wyświetlać co -1.
# wynik: fot Dlaczego "fot" zamiast "fotsyzrK" ??
imie = 'Krzysztof'
print(imie[:-4:-1])  # ten slice określa indeksy [-1, -2, -3]
