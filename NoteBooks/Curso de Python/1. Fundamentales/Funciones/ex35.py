#Branches and Functions

from sys import exit


def gold_room(input):
    if "0" in choice or "1" in choice:
        print("Haz tomado muy poco, está bien")
        amount = int(choice)
    else:
        print("Aprende a escribir un número")

    if amount < 50:
        print("Bien no eres avaro")
    else:
        print("Muere maldito loco")

def bear_room():
    print("Te encuentras un oso sentado en la puerta y necesitas moverlo, ¿Qué haces?")
    bear_moved = False
    while True:
        choice =input("> ")
        if choice == "Tomar miel":
            dead("El osos de ataca")
        elif choice == "Hacerle un taunt al oso" and not bear_moved:
            print("El oso se ha movido de la puerta, peudes seguir")
        elif choice == "Hacerle un taunt al oso" and bear_moved:
            dead("El osos se enoja y te arranca las piernas")
        elif choice =="open door" and bear_moved:
            gold_room()
        else:
            print("No se que quieres decir")

def cthulhu_room():
    print("Te encuentras al inobrable cthuluy te vuelves loco con mirarlo, escapar o comer cabeza")
    choice =input("> ")
    if "Escapar" in choice:
        start()
    elif "cabeza" in choice:
        dead("Estaba rico")
    else:
        cthulhu_room()

def start():
    print("Estas en una habitación oscura toma las puerta de la izzquierda o la derecha?")
    choice = input("> ")
    if  choice ==" izquierda":
        bear_room()
    elif choice =="derecha":
        cthulhu_room()
    else:
        dead("Te mueres de hambre en la habitación")


def dead(why):
    print(why,"Buen trabajo!")
    exit(0)


start()


