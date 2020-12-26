# #El porósito de este código es:
# Leer el archivo que se lama DataTestPy, meter cada uno de estos datos en un array, o estructura de datos
# queme permita luego organizarlas en columnas con un format literal string

# Lectura;

# https://docs.python.org/3/library/re.html
# https://regexr.com/
#Debo de abrir el archivo
#Se muestra así mismo, me muestra el código fuente impreso.
# file = "ReadOpenLiterals.py"
# openFile = open(file)
# print(openFile.read())


#Abro el dataset de mi interes.
file = "DataTestPy.txt"
openFile = open(file)
readFile = openFile.read()
directory = {readFile}
print(directory)
print(type(directory))
# Es un set.


# Como recorro un set?, y añado elementos a mi set?
#
# i = 0
# for i in directory:
#     user = i
#     print(f"{user:3f}")




