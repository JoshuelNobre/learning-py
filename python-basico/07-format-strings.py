nome = 'Josué'
idade = 25
altura = 1.82
peso = 94
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # .2f para formatar a quantidades de casas float

print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))

print('{0} {1} tem {1} anos {0} e seu {2} imc é {1}'.format(nome, idade, imc))

print('{n} {n} tem {i} anos {im} e seu {i} imc é {n}'.format(n=nome, i=idade, im=imc))