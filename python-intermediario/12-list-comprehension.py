l1 = [1,2,3,4,5,6,7,8,9]
l2 = '01234567890123456789012345678901234567890123456789'
# Pego cada elemento da lista l1
ex1 = [variavel for variavel in l2]
print(ex1)

# Pego cada elemento da lista l1 e multiplico por 2
ex2 = [v * 2 for v in l1]
print(ex2)

# O primeiro for itera sobre a lista l1, o segundo itera sobre cada elemento da lista l1
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)


l2 = ['Luiz', 'Mauro', 'Maria']

# Consigo iterar sobre cada elemento, aplicando alguma coisa
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

# Consigo inverter chave e valor
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x,y in tupla]
ex5 = dict(ex5)
print(ex5)

# Faço "v" a cada "v" in "l3" se o modulo de "v" por 2 igual a zero
l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]
print(ex6)

# 
l3 = list(range(100))
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 ==0]
print(ex7)

l3 = list(range(100))
ex8 = [v if v % 3 == 0 and v % 8 ==0 else 'Não é' for v in l3]
print(ex8)