"""

La idea de este ejercicio es modelar  una cantidad de dinero.

a - Debo representar una cantidad de dinero en diferentes divisas-> Estas serán las instancias del objeto.
b - Debo agragar funciones de operaciones aritméticas específcas.


"""

class Currency:

    """ En esta inicialización le digo que siempre me devuelva el nombre"""
    def __init__(self,  cantidad, name):
        self.name = name
        self.cantidad = cantidad

    def sum(self):
        cantidad_1 = int(input(f"Ingrese la cantidad que desea sumar en {self.name} > "))
        cantidad_2 = int(input(f"Ingrese la cantidad que desea sumar en {self.name} > "))
        return print("Tienes ",cantidad_1 +cantidad_2, self.name)

    def rest(self):
        cantidad_1 = int(input(f"Ingrese la cantidad que desea restar en {self.name} > "))
        cantidad_2 = int(input(f"Ingrese la cantidad que desea restar en {self.name} > "))
        return print("Tienes ",cantidad_1 +cantidad_2, self.name)

    def mult(self):
        c = int(input(f"Digite la cantidad por la que desea multiplicar sus {self.name}> "))
        return print("Tienes", c* int(self.cantidad))

    def div(self):
        try:
            c = int(input(f"Digite la cantidad por la que desea dividir sus {self.name}> "))
            return  print("Tienes ", int(self.cantidad)/c)
        except ValueError as e:
            print("No puedes dividir sobre cero")


# Instancio mi clase.
if '__main__' == __name__:
    entry = input("Digite la cantidad de dinero que desea operar >")
    dollar = Currency( entry, "US$")
    dollar.sum()
    dollar.div()
    dollar.rest()
    dollar.mult()

