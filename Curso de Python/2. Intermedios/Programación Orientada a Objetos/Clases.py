class clase_elemental:
    """Simple clase de ejemplo """

    i =1234 # variable de clase compartida por todas las instancias
    def prueba(self): # función de clase compartida por todas las instancias
        return "Hola"

    def __init__(self, nombre): # variable de instancia única para la instancia
        self.nombre = nombre





n ="Este texto no se usará por la clase"
print(clase_elemental.i, clase_elemental.prueba(n))

""" Para tener la doumentación de la clase se usa .__doc__  y no tomará este string de explicación,
porque no está dentro del ámbito."""
print(clase_elemental.__doc__)


""" Init() existe para inicializar con ciertos atributos la clase

NOTA 1: No usar objetos mutables para las variables fuera de init() , ya que trae comportamientos indeseados.


"""
class Perro:
    Tipo = "Caninus"
    def __init__(self, nombre):
        self.nombre = nombre

dog_a = Perro("Menfis")
dog_b = Perro("Kira")

""" La calse Perro comparte para todas sus instancias el Tipo, pero no el nombre del perro"""

print(dog_a.Tipo," ", dog_b.Tipo)
print(dog_a.nombre," ", dog_b.nombre)




