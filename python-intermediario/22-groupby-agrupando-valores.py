import imp
from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Leticia', 'nota':'B'},
    {'nome': 'Fabio', 'nota':'B'},
    {'nome': 'Carlos', 'nota':'A'},
    {'nome': 'Raimundo', 'nota':'D'},
    {'nome': 'Zé', 'nota':'C'},
    {'nome': 'Carmen', 'nota':'D'},
    {'nome': 'Joshuel', 'nota':'A'},
    {'nome': 'Josue', 'nota':'B'},
    {'nome': 'Jonathan', 'nota':'B'},
]

ordena = lambda item: item['nota']

alunos.sort(key= ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados) # Faz uma cópia de valores_agrupados, va1=cópia1 e va2=cópia2

    print(f' Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()