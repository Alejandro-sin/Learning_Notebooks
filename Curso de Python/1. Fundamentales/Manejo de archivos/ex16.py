
# A continuación se trabajará en las siguientes palabras claves.
# close, read, write,open, truncate, readline, seek, que son cómo las funciones que tiene que ver con la lectura, cierre, busqueda y almacenamineto
# lineal. Es como abrir, cerrar, leer, leer una linea, buscar en el rexto.


from sys import argv
script, fileName = argv

print(f"We're going to erase {fileName}.")
print("Hit CTRL-C si no quieres que suceda")
print("Hitreturn")
input("?")

print("opening the file...")
target = open(fileName,'w')

print("Trucnar el archiv")
target.truncate()
print("Esribe 3 cosas")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# Con esta linea estoy escribiendo en el archivo.
target.write(line1)
target.close()