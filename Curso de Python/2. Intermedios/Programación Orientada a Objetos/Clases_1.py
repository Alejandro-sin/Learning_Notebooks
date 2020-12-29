
"""  Puedo inicializar lso objetos mutables dentro del init, para que no se
repartan a través de todas las instancias, y tambien puedo interactuar de manera
directa sobre las variables definidas en el espacio__init__()

"""


class Personajes:
    """Documentación: Uso lo definido en el init()"""
    saludo = "Hola"

    def __init__(self, nombre):
        self.nombre = nombre
        self.poderes = []

    def agregar_poder(self, poder):
        self.poderes.append(poder)


etrx = Personajes("Etrx")
nyna = Personajes("Nyna")

etrx.agregar_poder("inteligencia")
print(etrx.__doc__,etrx.poderes)


