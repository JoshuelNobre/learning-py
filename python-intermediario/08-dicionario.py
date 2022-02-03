# Criando dicionário
d1 = {"nome da chave": "valor da chave"}
print (d1)
# Adicionar novos elementos
d1["nova_chave"] = 'Valor da nova chave'
print (d1)
print(d1['nome da chave'])

# Outro modo de criar um dicionário
d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(d2)

# Chave preccisa ser única
d3 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}

#Adiconar ooisas do dicionario
d3.update({'nova_chave':'novo valor'})
# Buscar valor através da chave no dicionário
print(d3.get('str'))
print(d3)
# Deletar chave do dicionário
# del d3['str']
# print(d3)
# Buscar valores 
print('str' in d3)
print('valor' in d3.keys())
print('valor' in d3.values())

# Iterando sobre dicionário
d5 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'outro do outro valor',
}

for k in d5.items():
    print(k)

for k, v in d5.items():
    print(k, v)

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Miranda',
    },
    'cliente2' : {
        'nome' : 'João',
        'sobrenome' : 'Moreira',
    },
    'cliente3' : {
        'nome' : 'Joshuel',
        'sobrenome' : 'Nobre',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


d7 = {1:'a',2:'b',3:'c'}
#Cópia rasa
v = d7.copy()
v[1] = 'Joshuel'

print(d7)
print(v)

import copy
# Agora são dicionários indepentes
v = copy.deepcopy(d7)

# Convertendo lista em dicionário
lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3],
]
d1 = dict(lista)
print(d1)

# Eliminar a alguma chave
d1.pop('c3')
print(d1)

# Concatenar dois dicionários
d2 = {
    'a':'b',
    'c':'d',
}

d1.update(d2)
print(d1)
