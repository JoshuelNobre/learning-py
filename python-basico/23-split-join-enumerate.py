""" 
Split, Join, Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista #iteráveis 
"""
from typing import _SpecialForm


string = 'O Brasil é o o o o o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')
""" print(lista2)

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.') """

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

algo = 'Josué é um cara bem legal'
agora_lista = algo.split(' ')
algo_novo = ' '.join(agora_lista)

print(algo)
print(agora_lista)
print(algo_novo)

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

lista3 = [
    
    ['Luiz', 'João', 'Maria'],
    ['Claudio', 'Pedro', 'Gleidson'],
    ['Kat', 'Amanda', 'Jose'],
]

for v in enumerate(lista3):
    v1, v2 = v
    a, b , c = v2
    print(v)

print(a,b,c)


