from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x>5, lista)
print(list(nova_lista))

nova_lista = filter(lambda p: p['preco'] > 50, produtos)
print(list(nova_lista))

for produto in nova_lista:
    print(produto)