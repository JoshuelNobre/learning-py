"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

""" lista = [22,'oI','Brunno',3.42]
lista[3] = 'Oi, eu sou Joshuel'
print(lista)

l1 = [1,2,3]
l2 = [4,5,6]
 """
# l2.append('b') # Add 'b' na lista l2
# l2.insert(0, 'banana') #Coloco o índice que quero add e o que quero add
# l2.pop() # Remove o último da lista
""" l3 = [1,2,3,4,5,6,7,8,9]
del(l3[2:5])
print(l3)

l4 = list(range(1,10))
print(l4)

l5 = ['String',True,20,11.6]

for elem in l5:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}') """


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu !')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower() 

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*' # Estu concatenando
    if secreto_temporario == secreto:
        print(f'Que legal você GANHOOOU !!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    
    print(f'Você tem {chances} chances')