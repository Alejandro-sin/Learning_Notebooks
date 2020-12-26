

"""

Estoy probando la forma de hacer doctrings en pyhton para usarlos en mi aplicación  de Master Dojo.

"""

class Rockets:
    """
    Así se ven los comentarios cuando los uso.

    """
    def __init__(self, name):
        self.name = name

    """
    
    No hace nada especial o si?
    
    """
    def sum(self):
        return 1+1


print(help(Rockets))