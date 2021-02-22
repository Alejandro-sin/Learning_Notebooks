'''
Override Explcitily

Anular una función heredad implicitamente.




'''



class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()

'''
El resultado, aunque Child(Parent) es decir , aunque child derive de parent, sobreescribirá la función
PARENT override()
CHILD override()

'''