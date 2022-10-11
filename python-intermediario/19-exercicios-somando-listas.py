"""
lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]
-------------------------
resultado = [2,4,6,8]
"""

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]
nova_lista = [x+y for x,y in zip(lista1, lista2)]
print(nova_lista)
