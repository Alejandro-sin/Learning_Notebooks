import random
import math

# X mayúscula es la forma de representar un array.
def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)
    # Guaradamos los reusltados de las usmatoria.
    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))

# La relevancia es:
# Al generar funciones auxilaires qu usaré uego, no quiero que ejecute este programa cuando lo importamos a un archivo.
if __name__ == '__main__':
    # Aquí el array entre  n y m.
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {sigma}')