"""

Las buenas prácticas de programación orientada a objetos habla que hay que eliminar el if
y usar polimorfismo en su lugar. ara darle un diseño estable y mantenible al código.

La idea es evidenciar que los objetos toman la desición, la descición no etá hardcodeada.
Apraece algo nuveo en el dominio del problema y aparece algo nuevo en mi modelo.
"""
def calculate_local_cost_of(call):
    pass

def calculate_national_cost_of(call):
    pass

def calculate_international_cost_of(call):
    pass



def call_cost_calculate(call):
    cost = 0
    if call.is_local():
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calculate_national_cost_of(call)
    elif call.is_national():
        cost = calculate_international_cost_of(call)

    return cost
"""
# Para eliminar el if, empezamos creando una jerarquía polimórfica con una abstracción por condición.
class ConditionSuperclass(object):
    # Usamos el mismo nombre del mensaje
    def calculate(self):
        raise NotImplementedError("SubClass Responsability")

class ConditionLocal(ConditionSuperclass):
    def calculate(self):
        # Repartimos el código del if en cada abstracción.

class ConditionNational(ConditionSuperclass):
    def calculate(self):
    
    
class ConditionInternational(ConditionSuperclass):
    def calculate(self):
    

"""


#Nombramos las clases.

class CallCostCalculator(object):

    @classmethod
    def to_handle(klass,call):
        # Código que busca el costcalulator correspondiente.
        pass

    def calculate(self):
        raise NotImplementedError("SubClass Responsability")

class Local(CallCostCalculator):
    def calculate(self):
        pass

class National(CallCostCalculator):
    def calculate(self):
        pass

class International(CallCostCalculator):
    def calculate(self):
        pass