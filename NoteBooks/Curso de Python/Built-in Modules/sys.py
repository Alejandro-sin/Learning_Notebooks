'''
https://docs.python.org/3/library/sys.html

Este módulo provee acceso a algunas variables usadas o mantenidas por el interprete y funciones que interactúan con el interprete de python
El modulo sys provee funciones y variables usadas para manipualr diferentes partes el embiente de ejecución
de pyhton.
Da acceso a algunas variabes o son mantenidas por el interprete

'''


'''
sys.argv es un arreglo para argumentos de líneas de comandos.

Argumentos de línea de comando, son aquellos valores que son pasados durante las llamadas del program a lo largo
de la llamada del estamento.
Es decir arg. Es una lista de argumentos..

El primer elemento del arreglo sys.arv() es el nombre del programa en si mismo


'''
import sys
'''
Cabe resaltar que las funcioesn sys se ejcutan es en consola para ver los tersultados.

'''
print("This return the name of the file:", sys.argv[0])
print("This return list of arguments:", str(sys.argv))

print("This is the name of the program:",
      sys.argv[0])
print("Number of elements including the name of the program:",
      len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv) - 1))
print("Argument List:",
      str(sys.argv))