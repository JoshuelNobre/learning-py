num1 = input('Digite um núumero inteiro: ')

if num1.isdigit():
    num1 = int(num1)
    if (num1 % 2) == 0:
        print(f'{num1} é um número par')

    else:
        print(f'{num1} é um número ímpar')
else:
    print('Isso não é um inteiro')








