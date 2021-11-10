num1 = input('Digite um número: ')
num2 = input('Dgite outro número: ')

""" if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print (num1 + num2)
else:
    print('Não pude converter os números para realizar contas.') """

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('ERROR')