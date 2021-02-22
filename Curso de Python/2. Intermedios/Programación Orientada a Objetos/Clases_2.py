"""


Los métodos pueden llamar a otros métodos de la instancia usando
el argumento self.

Una clase nunca se usa como un ámbito global.

No usar datos globales en un método. Solo los módulos aplican aquí.

Mejor que los métodos hagan referencia a su propia clase.



"""


class Bolsa:

    def __init__(self):
        self.datos =[]


    def agregar(self, name):
        self.datos.append(name)

    def usar_otrafuncion(self, name):
        self.agregar(name)
        self.agregar(name)

""" Me devuelve el tipo de clase que tengo."""
print(Bolsa.__class__)

