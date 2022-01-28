

def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('a','4')
    print(msg, nome)

saudacao(nome='Zé do gás', msg='Hello')
saudacao('Oi','Carlinhos')
saudacao('Olá','Joseph')

def divisao(n1,n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(8,4)
print(divide)