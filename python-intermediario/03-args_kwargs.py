def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)

lista = [1,2,3,4,5]
lista2 = [9,6,5,4,7]

func(*lista,*lista2, nome="Josh", sobrenome="Nobre")