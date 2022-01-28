"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada
"""
# def func2():
#     return "Aaaaaa, deu bom!"

# def func1(funcao):
#     return funcao()

# executando = func1(func2)
# print (executando)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos
"""

def func_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = func_mestre(fala_oi, "Luiz")
executando2 = func_mestre(saudacao, "Joshuel", "Bom dia!")

print(executando)
print(executando2)
