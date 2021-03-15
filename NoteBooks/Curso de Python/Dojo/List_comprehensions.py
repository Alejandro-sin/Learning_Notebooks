"""https://www.hackerrank.com/challenges/list-comprehensions/problem.

Tengo un cubo de x,y,z lados y una suma n que reustla de sumar cada lado del cubo.

Debo imprimir  una función que me retorne toddas las permutaciones y me excluya los que tienen una suma con n =3.

Ejemplo de lo que debe devol    ver;

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2] ....] Estos excuyen con n = 2


*
* decirle que meta x,y,z en una lista
* que sume la lista y que evalue su igualad con n
* Si es igual excluyalo
"""



""" 
def list_generator(x,y,z):
    # Genero un 4 inputs
    x,y,z,n = (int(input()) for _ in range(4))
    a =  [i for i in range(0, x+1)]
    b =  [j for j in range(0, y+1)]
    c =  [k for k in range(0, z+1)]
    return [a,b,c]


print(list_generator(1,2,3)) """

x = 1
y =  1
z =  1
a = [i for i in range (0,x+1)]
b = [j for j in range (0,y+1)]
c = [k for k in range (0,z+1)]

print(a, b,c)


""" 

Podemos usar el método iter tools para generar permutaciones

Y ver tutorial de lsitcomprehensions

 """