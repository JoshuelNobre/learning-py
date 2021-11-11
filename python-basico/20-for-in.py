texto = 'Python'
nova_string = ''

for n, letra in enumerate(texto):
    print(n, letra)

print('--------------------------------')

for numero in range(10):
    print(numero) 

print('--------------------------------')

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra

print(nova_string)