import numpy.random as rn
import random

class node:
    def __init__(self,parent,value):
        self.parent = parent
        self.value = value

    def __repr__(self):
        return f"{self.value}"

class edge:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.suma = x+y
    def __repr__(self):
        return f"{self.x}<->{self.y} - {self.suma}"

rn.seed(4)
A = rn.randint(1,100,25)
A = list(dict.fromkeys(A))
print(sorted(A))
print(len(A))

pares = []
impares = []

for i in sorted(A):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(pares)
print(impares)




vertices_pares = []
vertices_impares = []
lados = []
for i in pares:
    nodo = node(None,i)
    vertices_pares.append(nodo)

for i in impares:
    nodo = node(None,i)
    vertices_impares.append(nodo)

for i in impares:
    for j in pares:
        lado = edge(i,j)
        lados.append(lado)

print(vertices_pares)
print(len(vertices_impares))
print(len(vertices_pares))
print(vertices_impares)
print(len(lados))
print(lados)