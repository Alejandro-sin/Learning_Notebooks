"""

Una buena práctica es tener una clase abstracta de la que derivan clases concretas.



"""


# Calse abstracta
class CallCalculator:

    def calculate(self):
        raise  NotImplementedError ("Sub Class responsability")


#   Esta es la que hereda de la clase abstracta CallCalcultaor
class LocalCalculator(CallCalculator):
    def calculate(self):
        pass

