"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


def fun_saudacao(saudacao,nome):
    print (saudacao, nome)

fun_saudacao("Olá", "Pedro")
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""
def soma_3(a,b,c):
    print (a + b + c)

soma_3(1,2,6)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual.
Retorne o valor do primeiro número somado do aumento do percentual do mesmo
"""
def soma_porcentagem(a,b):
    return a + (a*b/100)

print(soma_porcentagem(10,80))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, 
se o parâmetro da função for divisível por 5, retorne buzz. 
Se o parâmetro da função for divisível por 5 e por 2, retorne FizzBuzz, 
caso contrário, retorne o número enviado.
"""

def FizzBuzz(a):

    if a % 2 == 0  and a %5 == 0:
        return "FizzBuzz"
    if a % 5 == 0:
        return "Buzz"
    if a % 2 == 0:
        return "Fizz"
    return a

print(FizzBuzz(10))

from random import randint

for i in range(20):
    aleatorio = randint(0,100)
    print(FizzBuzz(aleatorio))