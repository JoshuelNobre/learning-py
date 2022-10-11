"""
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""
# Combinação - Ordem não importa
from itertools import combinations
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Joshuel']
for grupo in combinations(pessoas, 2):
    print(grupo)

# Permutação - Ordem importa
from itertools import permutations
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Joshuel']
for grupo in permutations(pessoas, 2):
    print(grupo)

# Produto - Ordem importa e repete valores únicos
from itertools import product
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Joshuel']
for grupo in product(pessoas, repeat=2):
    print(grupo)