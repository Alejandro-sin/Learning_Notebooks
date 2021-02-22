import sys
import random

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

Es la abstracción de dónde se encuentra nuestro borracho en el plano.

Implementamos dos métodos.

El metodo de movimeinto y el método de distancia pitgótiroca.

"""

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Estoy diciendole que se  mueva desde mis varibles iniciales x, y hasta + delta_x y delta_y

    def mover(self, delta_x, delta_y):
        return Coordenada(self.x  +  delta_x,  self.y  +  delta_y)
    # Distancia pitagórica en un plano.
    def distancia (self, otraCoordenada):
        delta_x = self.x - otraCoordenada.x
        delta_y = self.y - otraCoordenada.y
        return (delta_x**2 + delta_y**2)**0.5




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