"""
count - Itertools
"""

from itertools import count

contador = count(start=5, step=2)

for valor in contador:
    print(round(valor, 2))

    if valor >=10:
        break

##########################################

from itertools import count

contador = count()
lista = ['Luiz', 'João', 'Maria']
lista = zip(contador, lista)
print(list(lista))