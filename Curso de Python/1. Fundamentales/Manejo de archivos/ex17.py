# En este archivo se hará ejercicios de read para coporar un archivo.
# La idea general en esto es hacer que un archovo se copie de la manera más optima psoible
# Como puedo hacerlo en una sola línea?
from sys import argv

# Retorna verdadero si un archivo existe
from os.path import exists

script,from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


# Cómo hacer esto en una líne
in_file = open(from_file)
print(type(in_file))
indata = in_file.read()
print(type(indata))
#
# file = open(from_file, 'r')
# print(type(file))

# Con echo y cat puedo crear archovos fantasmas... o algo parecido, debo buscar más sobre esto.

# $ # first make a sample file
# $ echo "This is a test file." > test.txt
# $ # then look at it
# $ cat test.txt
# This is a test file.

print(f"Your file exist? {exists(to_file)}")
print(f"The input file is {len(indata)} bytes long")
input()
out_file = open(from_file(to_file, 'w'))
out_file.write(indata)

print("Alright, all done")

out_file.close()
# indata.close()






