'''

Este ejercicio es para modelar empleados de una fábrica de isótopos


'''

class Person(object):
    def __init__(self, name, age, employee, _id):
        self.name = name,
        self.age = age,
        self._id = _id,
        self.employee = employee

    def employ_status(self):
        if self.employee:
            return print(f"El empleado {self.name} se encuentra activo")
        else:
            return print(f"El empleado {self.name} ya no encuentra activo")
    


maria = Person("Maria","30", True, 10101011)
maria.employ_status
