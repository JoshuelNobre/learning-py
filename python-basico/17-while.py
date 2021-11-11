""" 
utilizado para realizar ações
enquanto uma condição for verdadeira 
"""

x = 0 # coluna
y = 0 # linha
 
""" 
while x < 100:
    print(x)
    x = x + 1 
"""

""" 
while x < 10:
    if x == 3:
        x = x +1
        continue

    print(x)
    x = x + 1 
"""

""" 
while x < 10:
    print (x)
    x += 1 

print ('Acabou!')
"""
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input ('Digite um operador: ')
    sair = input ('Deseja sair? [s]im ou [n]ão')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '-':
        print(num_1 - num_2)
    elif operador == '+':
        print(num_1 + num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)




