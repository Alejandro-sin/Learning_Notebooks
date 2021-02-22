"""

Este programa tiene como proósito servir de prueba práctica de lo aprendido hasta ahora.
Un videojuego que se trate de adivinar un númeor aleatorio que arroje la computadora.

"""

import random as r

def run ():
    randomNumber = r.randint(1,100)
    numberChoice = int(input("Escribe el  número que crees que tu PC pensó  entre 1 y 100 >  "))
    lifes = 5
    while numberChoice != randomNumber:
        if numberChoice < randomNumber:
            print("El número que buscas es menor")
            lifes -=1
            numberChoice = int(input("Escribe el  número que crees que tu PC pensó  entre 1 y 100 >  "))
        elif numberChoice > randomNumber:
            print("El número que buscas es mayor")
            lifes -= 1
            numberChoice = int(input("Escribe el  número que crees que tu PC pensó  entre 1 y 100 >  "))
        print(f'Tienes {lifes} vidas')

        if lifes == 0:
            print("GAME OVER")
            break

        if numberChoice == randomNumber:
            print("GANASTE!!!!")
if __name__ == '__main__':
    run()



## Queda pendiente revisar esta ejecución del rpograma.

