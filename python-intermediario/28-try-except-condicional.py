def converte_numero(valor):
    try:
        float(valor)
    except ValueError as erro:
        pass

numero = converte_numero(input('Digite um número: '))
print(numero * 5)
