import sys


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


Campo en su constructor no recibe nada, pero define un diccionario para las coordenas d elos borrachos.
define un diccionario vacio para guardar coordenadas de borrachso.

1. Tiene método añadir borracho. Recibe un borracho y una coordenada
2. Mover el borracho. El borracho al caminar regresa uan tupla.

"""
# Deino mi clase campo
class Campo:
    # Le paso un constructor vacío porque no va a recibir parámetros pero si tendrá métodos, lo único que hará será almacenar
    # en un diccionario
    def __init__(self):
        # Diccionario para guardar las coordenadas de borracho
        self.coordenadas_de_borracho ={}

    # Creo el méotod añadir borracho, me recibe un borracho y una cordenada.
    def anadir_borracho(self, borracho, coordenada):

        # Le estamos diciendo que me acceda con el keyvalue "borracho" a ese espacio en memoria para ser
        # almacenado en el diccionario.
        self.coordenadas_de_borracho[borracho] = coordenada

    # Método para mover al borracho
    def mover_borracho (self, borracho):

        delta_x, delta_y = borracho.camina_random()
        coordenada_actual =self.coordenadas_de_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borracho[borracho]= nueva_coordenada

    def obtener_coordenada (self, borracho):
        return self. coordenadas_de_borracho[borracho]





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