"""

Este programa tiene como propósito mostrar el funcionamiento de  break y continue en python para los ciclos for.

"""
def run():
    break_f()
    continue_f()
    break_w()
    continue_w()


# Lo que hace este código es contar hasta que sea 7 y se detiene
def break_f():
    for contador in range(10):
        print(contador)
        if contador == 7:
            break

# En este código quiero ver el funcionamiento de continue.

def continue_f():
    for contador in "continue":
        print(contador)
        if contador == "u":
            print("Encontraste la u")
            continue


def break_w():
    MAX = 10
    contador = 0
    number = 1
    while number < MAX:
        print(number)
        if number == 3:
            break
        contador +=1
        number += 1

def continue_w():
    MAX = 10
    contador = 0
    number = 1
    while number < MAX:
        print(number)
        if number == 3:
            print("Encontraste el 3")
            continue
        contador +=1
        number += contador

if __name__ == '__main__':
    run()