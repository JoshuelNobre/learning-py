""" 
Formatando valores com modificadores

:s - Texto (strings) 
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ,ou f)

> - Esquerda
< - Direita
^ - Centro
"""





num_1 = 10
num_2 = 3
divisao = num_1 /  num_2

print ( '{:.2f}'.format (divisao))
print ( f'{divisao:.2f}')


nome = 'Joshuel Nobre'
print (f'{nome:s}')

nome2 = 'Luis Claudio'
nome_formatado = '{:#^50}'.format(nome2)
print(nome_formatado)

nome3 = 'Ronaldo filho do Seu Armando'
nome_formatado2 = '{n:a^50} {n} {n} {n}'.format(n=nome3)
print(nome_formatado2)

nome4 = 'Luis Claudio'
sobrenome = 'Aragão'
nome_formatado3 = '{0} {1} '.format(nome4,sobrenome)
print(nome_formatado3)

