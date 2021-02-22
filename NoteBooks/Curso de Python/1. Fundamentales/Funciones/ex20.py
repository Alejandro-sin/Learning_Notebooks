# Ejercicio sobre funciones y archivos
from sys import argv
script, input_file = argv

# Haré 3 funciones

# Una función que me imprima tod.o

def print_all(f):
    read = f.read()
    print(read)

# Una función qme imprima una línea

def line_count(count, f):
    read_line = f.readline()
    print(count, read_line)

# un afunción que me permita hacer un rewind, como al punto cero

def rewind (f):
    f.seek(0)

current = open(input_file)


print_all(current)
print('Viene la función rewind \n')
rewind(current)

print('viene la función contar lineas\n')
for x in range(10):
    current_line = x
    line_count(current_line, current)
