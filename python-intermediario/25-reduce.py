from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i:i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p:p['preco'] + ac, produtos, 0)
print(soma_precos)