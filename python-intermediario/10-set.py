# add (adiciona) , update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_diffrence ^ ( elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5}
s1.add(22)
s1.update([2,24,56,2,1,5])

for v in s1:
    print(v)


# Posso usar o "set" para transformar excluir elementos duplicados
# Ex: 

l1 = [1,2,3,3,3,3,3,3,3,5,5,66,4,4,3,7,'Joshuel','Joshuel']
l1 = set(l1)
l1 = list(l1)
print(l1) 


# Union

s2 = {1,2,3,4,5}
s3 = {1,3,4,6,7,8}
s4 = s2 | s3
print (s4)

# Intersection

s2 = {1,2,3,4,5}
s3 = {1,3,4,6,7,8}
s4 = s2 & s3
print (s4)

# difference

s2 = {1,2,3,4,5}
s3 = {1,2,3,4,6,7,8}
s4 = s2 - s3
print (s4)

# symmetric_diffrence

s2 = {1,2,3,4,5}
s3 = {1,2,3,4,6,7,8}
s4 = s2 ^ s3
print (s4)

# Posso usar o "set" para isso

l1 = ['Luiz', 'Joao', 'Maria']
l2 = ['Luiz', 'Joao', 'Maria', 'Luiz', 'Joao', 'Maria']

l1 = set(l1)
l2 = set(l2)

print (l1 == l2)
