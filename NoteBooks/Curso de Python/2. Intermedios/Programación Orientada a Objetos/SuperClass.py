"""

ALTER AFTER OR BEFORE


La palabra reservada super me permtie acceder a la clase padre desde el cuerpo del hijo
y así poder modificar el comportamiento.

"""

class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD , BEFORE PARENT altered ()")
        super(Child, self).altered()
        print("CHILD , AFTER PARENT altered ()")

# instancio
dad = Parent()
son = Child()


# pruebo
dad.altered()
son.altered()