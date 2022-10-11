nome = 'Luiz Otario'
iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
except:
    pass


print('Cadê meu valores?')  # Já consumi o meu iterador inteiro
for letra in iterador:
    print(letra)

#############################################
nome = 'Luiz Otario'
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o for')
for letra in gerador:
    print(letra)

print('Olha o outro for') # Não tem valores
for letra in gerador:
    print(letra)
