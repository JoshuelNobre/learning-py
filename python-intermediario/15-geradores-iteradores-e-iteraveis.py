lista = [1,2,3,4,5,6]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))


######################
import sys

lista = list(range(1000))
print(sys.getsizeof(lista))

#######################
import sys 
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)
g = gera()
for v in g:   
    print(v)
#########################
import sys 
import time

def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'

g = gera()
print(next(g))
print(next(g))
##########################
import sys 
import time

l1 = [x for x in range(1000000)]
l2 = (x for x in range(1000000))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

