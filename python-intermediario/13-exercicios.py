
string = '01234567890123456789012345678901234567890123456789'

n = 10
# i para cada i no tamanho de 0 a (tamanho da string), pulando de 10 em 10
contadores = [i for i in range(0, len(string), n)]

# pego minha minha string e fatio de 1- em 10
lista = [string[i:i+n] for i in range (0, len(string), n)]

# uso join pra unir a lista em string, coloco o '.' para ficar separado por '.'
retorno = '.'.join(lista)
print(contadores)
print(lista)
print(retorno)