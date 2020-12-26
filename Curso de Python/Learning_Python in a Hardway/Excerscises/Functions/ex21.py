#Functions Can return Something
from random import randint

def add(a,b):
    print(f"{a}+{b}")
    return a+b

def substract(a,b):
    print(f"{a}-{b}")
    return a-b

def mult(a,b):
    print(f"{a}*{b}")
    return a*b

def div(a,b):
    print(f"{a}/{b}")
    return a/b


a = add(35,5)
h=substract(78,4)
w=mult(90,2)
z=div(100,2)

what=add(a,(substract(h,(mult(w,div(z,2))))))
print(f"This is my what value{what}")

ex = mult(add(a,h) - (z/2)*5, randint(8,10))
print(f"This is my what ex{ex}")
