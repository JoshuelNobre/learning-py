try:
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
else:
    print('Seu código foi executado.')
finally:
    print('Sou executado de todo jeito')