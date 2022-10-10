lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x.upper(): y for x,y in lista}
print(d1)

d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2)

