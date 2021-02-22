import sys
import  random

title = """
■■■■■■■■■■■■■■■■■■■■■■■■■■■■ PROPOSE ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Esta serie de documentos tiene como propósito estudiar  los conceptos de programación dinámica
mediante  ejercicios y análisis comentariados con msi apuntes personales.

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
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       Camino de borrachos    ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Existe el mismo porcentaje de posibilidades de ir en cualquier dirección de x,y un 25% por cada paso.

Acercamiento, se v a agenerar 3 clases. Para borrachos para generar abstración corrdenadas, otra clase que em represente el plano


■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
print(about_code)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         Code         ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
code_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Code    

Debo crear la clase borracho     
"""


# Creo la clase con la palabra reservada class, y el nombre con dos puntos
class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre


# Instancio mi clase mediantante la palabra super().__init__ para que me herede de borracho.
class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    # Defino una función para caminar aleatoriamente
    def camina_random(self):
        # Le digo que me devuelva el módulo random y con el metodo choice le paso 4 argumentos de dos ejes, adentro de una lista.
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


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