"""
Operador ternário em Python
"""

logged_user = False

msg = 'Usuáro logado.' if logged_user else 'Usuário precisa logar'

print (msg)


idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Você precisa digitart apenas números')
else:
    e_de_maior = (int(idade) >= 18)
    msg2 = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg2)

