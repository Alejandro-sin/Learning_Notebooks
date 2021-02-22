import random as r
import math as mt

list_integers = [ x for x in range(0,10)]

def simpleArraySum(ar):
    # Debe devolver la suma del arreglo  de elementos como un entero.
    sum_result = sum(ar)
    return sum_result

    # ar es un arreglo de enteros.
print(simpleArraySum(list_integers))

    # la primera linea contine un entero n denotando el tamaño del arreglo.
    # la segunda linea contiene n enteros espacioados, representando los elementos del array.

    # Limitantes 0<n , ar <1000

    # Formato de salida debe imprimir la suma de los elementos del arreglo como un entero