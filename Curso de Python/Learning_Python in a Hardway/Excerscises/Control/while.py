"""
Este programa tiene como propósito evidenciar el uso de las estructuras while.

Lo que hace es que recibe un valor que deseo calcular y eleva al cuadrado el número dado,
lo hace hasta que la condición LIMITE deje de ser verdadera. En este caso operara hasta que encuentre
la potencia de mi numero que es menor a 1000

"""


def run():
    numero = int(input("Escribe el número que deseas calcular: "))
    LIMITE = 1001
    contador = 0
    potencia = numero ** contador
    while potencia < LIMITE:
        print(f'El número {numero} elevado a la 2 es igual a: {potencia}')
        contador = contador + 1
        potencia = numero **contador


if __name__ == '__main__':
    run()