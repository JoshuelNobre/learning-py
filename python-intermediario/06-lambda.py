from errno import EBUSY


def funcao (arg1,  arg2):
    return arg1 * arg2

var = funcao(2,2)
print(var)

a = lambda x,y: x*y
print(a(2,2))

lista = [
    ['P1',13],
    ['P2',45],
    ['P3',6],
    ['P4',11],
    ['P5',24],
]

print(lista)

# Essa função pode ser substituida por uma função lambda que mostro a seguir
# def func(item):
#     return item [1]

# Com lambda posso criar a função em 1 linha.
lista.sort(key=lambda item:item[1], reverse=True) 
#reverse = True para mostrar do mais caro para o mais barato.
#sort = ordena uma lista
print(lista)
