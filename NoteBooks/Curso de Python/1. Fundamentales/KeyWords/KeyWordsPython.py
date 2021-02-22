



# ■■■■■■■■■■■■■■■■■■■■■■■■■■ KEYWORDS■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


a = "Hola"
b = 3.2

# and

# if a == "Hola" and b == 3.2:
#     print("True")
# else:
#     print("False")

# With-as es un manejador contextual.para cuando usamor abrir archivos
# The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks
# Automáticamente cierra el archvo, no necsito close()

#With out with statement:

# file = open("../Data_sets/zen_py.txt")
# data = file.read()
# print(data)
# file.close()


#With statement

# with open("../Data_sets/zen_py.txt") as file:
#     data = file.read()
#     print(data)

#Assert
# El assert se usa para verificar un error si es True or False.

# if not a =="Hol":
#     assert a == "Todo esto es mentira"
# else:
#     assert a == " Esto es un error"


# Break:
# Para el loop inmediatamnete While o For. Deteniene la ejecución.

# contador = 0
# n = 3
# m = 10
# while n < m:
#     print(f"El número {n} es menor que {m}")
#     n = n + contador
#     contador += 1
#     if n > m:
#         break
#     else:
#         continue
#

# Class:
# Class es para crear clases en python.

# class comida:
#     def __init__(self, tipo, sabor):
#         self.tipo = tipo
#         self.sabor = sabor
#
# pizza = comida("Rápida", "Hawiana")
# print(pizza.tipo)


# El keyword del se puede usar para eliminar cosas de objetos, listas, diccionarios, variables.

# del para objetos.
#
# class utencilio:
#     def __init__(self, name, use, value):
#         self.name = name
#         self.use = use
#         self.value = value
#
#
# fork = utencilio("Fork", "Eat", 300)
# print(fork.name, fork.use, fork.value)
#
# # Borro dentro de los ojetos el atributo name
#
# del fork.name
# print(fork.name)
#
# # Borro el objeto
# del utencilio
# print(utencilio)


# lista= [1,2,3,4,5,6]
# print(lista)
# del lista[3::]
# print(lista)

#  TryPermiten probrar un error
#  except se usa juto con try, si no hay un try no hay excepción.
#  finally permite continuar el código sin importar el resultado de try y except
# Puedo poner tantos except necesite para manejar los errores.
# Puedo usar else para darle flfujo
#
# try:
#     print(error)
# except:
#     print("No existe nada con el nombre error")
# finally:
#     print("Estas listo aqui termina el try")
#
# # Raise sirve para arroja errores predeterminado.
#
# x = -1
# # if x < 0:
# #     raise Exception(f"Ha sucedido un error {x} es un númeor menor que 0")
#
# if not type(x) is str:
#     raise Exception("La variable no es un texto")
#


# in
#
# x = 0
# lista = [1,2,3,4,5,5]
# valor= x in lista
# print(valor)



# lambda
# Crea una función anónima, recibe cuatos parametros quiera ero solo una expreison
#
# def suma(a):
#     suma = a +10
#     return suma
#
# print(suma(5))
#
# # => Volvemos lambda function
#
# suma_lambda = lambda a : a + 10
# print(suma_lambda(6))
#
# multiples_parameters = lambda a,b,c :a+b+c
# print(multiples_parameters(2,3,4))

# Usamos lambda para cuando requerimos usar una función corta.

# yield

# lista = [1,2,3,4,5,6,7]
#
# def recorre(lista):
#     for x in lista:
#         yield x
#         print(x)
#
# print(recorre(lista))
# gen = recorre(lista)



