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
Acercamiento, se va agenerar 3 clases. Para borrachos para generar abstración corrdenadas, otra clase que em represente el plano


■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
print(about_code)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         Code         ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
code_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Code  

Con este código puedo hacer la simulación del camino aleatorio.
 
"""
# Estoy imporando mis métodos de mis archivos, exploro métod por método
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [40, 12, 0, -12]
    numero_de_intentos = 133
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

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