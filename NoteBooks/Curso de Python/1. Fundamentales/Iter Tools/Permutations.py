"""https://www.geeksforgeeks.org/permutation-and-combination-in-python/

Puedo encotnrar con python m�todos que permiten hallar permutaciones y
compbinaciones de una secuencia.
"""



#Permutations
'''
El método permutations recibe una lista como onput y retorna una lista de tuplas eu contiene todas las 
permutaciones en forma de lista

'''
from itertools import permutations

p =[1,2,3]
perm = permutations(p)

for i in list(perm):
    print(i)