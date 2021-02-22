# Para definir clases trabajo:

# class myClass:
#     elemento ="Materia"
#
# p1 = myClass()
# print(p1.elemento)


# __init__() Function
# Todas las cases tienen una función llamada init(), la cual siempre es ejecutada cuando
# la clase está siendo inicializada
# usar init() asignar valores a porpiedades de objetos u otras operaciones que sosn necesarias
# para cuando un objeto está siendo creado


# el parámetro self: es una referencia a la instancia de la clase, y es usado como variables de accesos
# pertenecientes a la clase. No tiene que llamarse self, puede llamarse como quiera.
# pero es el primero parámetro de la función

# Create a class named Person, use the __init__() function to assign values for name and age:
# Note: The __init__() function is called automatically every time the class is being used to create a new object
class person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

#Objetos tienen métodos asociados, los métodos son funciones que pertenenec a un objeto.
    def myfunc(self):
        print("Hola " + self.name)


p1 = person(29, "Etrx")
p1.myfunc()
print(p1.name, f"tiene {p1.age} años")


class car:

    def __init__(car, brand, speed, value):
        car.brand = brand
        car.speed = speed
        car.value = value

    def functions(car):
        print("Arrancar")

mycar = car("Toyota",120,30000)
print(mycar.brand, mycar.speed, mycar.value)



