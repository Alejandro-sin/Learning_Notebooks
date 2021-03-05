contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1
        # contador_interno += 1 --> Si eliminamos esto, habrá un bucle infinito de ceros porque el contador nunca avanza,
        # y es el contador interno el que define el externo.

        if contador_interno >= 3:
            break  # Esto es un break statement qu eme dice que cuando mi contador interno sea 3, pare.
            # Solo debe parar el contador interno, pues el externo tiene un contador por si mismo y seguirá la ejecución

    contador_externo += 1
    # contador_externo += 1 --> Si elimino esto, al ser el contador externo siempre 0, le estoy diciendo que vaya hasta infinito, y el código interno
    # se seguirá ejecutando de 0 a 5 indefinidamente
    contador_interno = 0
    # contador_interno=0  --->Eliminar este implica que contador_interno solo tendrá la oportunidad de ejecutarse de 0 a 5.

# El código en general tiene dos mecanismos uno interior que hace ciclos cortos, y uno exterior que envuelve los ciclos.
# Son estructuras de control anidadas.

# Tengo una función llamada iter, que me permite manipular los objetos iterables, es decir aquellos objetos que puedo
# repetir n veces, a las repeticiones es lo que denominamos iteración, y sus resultados son los puntos de partida para la siguiente.


