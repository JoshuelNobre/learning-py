variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

""" for valor in variavel:
    if valor.lower().startswith('J'): # startswith() = pergunta se começa com a letra tal
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor) """

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True
if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J')