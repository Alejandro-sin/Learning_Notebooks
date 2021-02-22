# Usamos simulacioens de montecarlo.


import random
import collections

# Generamos nuestras bajara.
PALOS = ['espada', 'corazon', 'rombo', 'trebol']
# Generamos los valores. Cuando está mayuscula por convencion son constantes.
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

# Función para generar la baraja.
def crear_baraja():
    # Guardo las barajas aquí, o las cartas.
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    # Rndom sample, obtienen en una colección obtiene una muestra sin reperitr el meustro  rnel la misma meustra
    # en dos ocasiones distinas
    mano = random.sample(barajas, tamano_mano)

    return mano


def main(tamano_mano, intentos):

    barajas = crear_baraja()
    # Va a guardar las manos que obtengo en la simulación
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    # Con esto calculamos la propaildiad de sacar pares.
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            # El valro es el índice 1 en la tupla palo, valor
            valores.append(carta[1])

        # Counter viene de collection. Y me permite contar las ocurrencias/frecuencia de un valor.
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)