import random

title = """
■■■■■■■■■■■■■■■■■■■■■■■■■■■■ PROPOSE ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Este docuemnto tiene como propósito ayudarme a estudiar, es el primer docuemnto de mi
proyecto  acerca de métodos automáticos para implementar neuroapreendizaje enfocado a código.

El documento sirve para a meida que voy aprendiendo genero un log de mi proceso.
¿Como debería funcionar?
Este docuemtno debería generarse cuando 
■■■■■■■■■■■■■■■■■■■■■■■■■■■■  NOTES  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Realiza este loop cuando estés estudiando programación.

* Habla en voz alta lo que estás haciendo. Como narrando los pasos que te llevan através de tu pensamiento. No importa 
  si es es voz baja.
* Comentar las líneas
* Jugar con el código  significa experimentar, romper, reparar.
    Experimentar siginifca poner código y tratar de enteder que estás haciendo y luego de entender encontrarás un para qué.


"""
print(title)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       About_Code     ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
about_code = """
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       Simulaciones    ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
El propósito de este código es generar la simulación de tirar dados en n veces.

1. Entradas
1.1. Queremos saber el número de tiradas? x
    1.2. Cuantas veces corremos la simulación? x
     => A mayor muestras de una población más cercano vamos a estar en los valores correctos de una población.
2. Creo una función main que me reciba numero de tiradas.?   
3. Requerimos guardar los resultados, lo hacemos en un arreglo tiros.  x?
4. Quiero que haga un ciclo for para recorrer el número de intentos de la simulación.
    4.1  Genero una función interna que me tier los dados (numer de tiros.1) y la almaceno en una variable
    4.2  Añado esta secuencia anterior mediante append(4.1)

5. La función creada con anterioridad dentro de for no existe, hay que crearla.
    5.1 Uso una variabel auxiliar que voy a vovler un arreglo vac{io.
    5.2 Hago un ciclo for que me reciba el número de tiros.
        cada tiro es un random.choice ([1,2...
    5.3 Hago un append de los tiros en mi arreglo secuencia vacío
        
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
print(about_code)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         Code         ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
code_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Code         

"""

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')



if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)


















print(code_literal)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■        Errors        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
error_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Error         

"""
print(error_literal)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  Learn and visualize ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
learnV_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Learn and visualize         

"""
print(learnV_literal)