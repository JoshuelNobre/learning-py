variavel = "valor"

def func():
    print (variavel)

def func2():
    # Não é boa prática de programção, mas é possivel que variavel local mude variavel global
    global variavel
    variavel = "Outro valor"
    print (variavel)

def func3(arg=None):
    arg = arg.replace("v","c")
    return arg

func()
func2()

outra_coisa = func3(arg=variavel)

print(outra_coisa)
print(variavel)