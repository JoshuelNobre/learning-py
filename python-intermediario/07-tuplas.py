t1 = (1,2,'Joshuel', 'a', 5 )
print(t1[4])
for v in t1:
    print (v)

t2 = 1,2,3,4,5,6,7
t3 = t1 + t2
print (t3)

n1, n2, n3, *_ = t3
print(n3)

# Posso fazer repetições

t5 = (22,'Josuel',35,26) * 10
print (t5)

# Tupla é imutável

t6 = (1,2,3,4,5)
t6 = list(t6)
t6[2] = 3000
t6 = tuple(t6)
print(t6)