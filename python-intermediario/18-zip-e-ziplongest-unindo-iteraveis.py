"""
Zip - Unindo iteráveis - Recomendável caso não saiba a quantidade de valores
Zip_longest - Itertools
"""

cidades = ['São Paulo', 'Maranguape', 'Salvador', 'Rio de Janeiro']
estados = ['SP', 'CE', 'BA', 'RJ']
cidades_estados = zip(estados, cidades)

# for valor in cidades_estados:
#     print(valor)

print(list(cidades_estados))

##################

from itertools import zip_longest
cidades = ['São Paulo', 'Maranguape', 'Salvador', 'Rio de Janeiro', 'Fortaleza']
estados = ['SP', 'CE', 'BA', 'RJ']
cidades_estados = zip_longest(estados, cidades, fillvalue=0)

# for valor in cidades_estados:
#     print(valor)

print(list(cidades_estados))

####################

from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Maranguape', 'Salvador', 'Rio de Janeiro', 'Fortaleza']
estados = ['SP', 'CE', 'BA', 'RJ']
cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)