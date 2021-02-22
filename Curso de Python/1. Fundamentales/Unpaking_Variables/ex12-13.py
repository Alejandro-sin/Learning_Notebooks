

#Estamos estudiando Unpaking, parameters, variables.


from sys import argv

name, first, second, third = argv
#Puedo hacer que despues de correr lso argumentos empacados, el usario me reemplace valores que estaban ahí.
# name = input("Escribe el nombre el script a correr: ")
print("The name of this script is: ", name)
print("The name of this varaible is: ", first)
print("The name of this varaible is: ", second)
print("The name of this varaible is: ", third)




#Ejecución de estos scripts se ahce por temrinal para pasarle a argv los parámetros
# (Alejandro-sin) C:\Users\USUARIO\Alejandro-sin\Data_Science\Python\py_root>python ex12-13.py Primera Segundo 3º
# The name of this script is:  ex12-13.py
# The name of this varaible is:  Primera
# The name of this varaible is:  Segundo
# The name of this varaible is:  3º

