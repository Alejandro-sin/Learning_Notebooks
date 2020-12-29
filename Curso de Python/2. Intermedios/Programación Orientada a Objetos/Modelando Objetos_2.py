"""

Ejercicio para operación entre currencies

"""


""" Representación del currency"""

class Curency:
    def __init__(self, name, symbol, factor):
        self.name = name
        self.symbol = symbol
        self.factor = factor


# No me queda muy claro el uso de esta función, sirve para mostrar puntualmente qué?
#     def __repr__(self):
#         info  = self.name
#         info2 = self.symbol
        # return info, info2


euro = Curency("Euro","EU","3.2")
print(euro)

