'''

Usar el módulo de pyhton para practicar expresiones regulares y manejo de archivos.

'''

import re

# Carpeta de Assets y el archivo.
PATH = "C:/Logos/Root/Learning_Notebooks/Curso de Expresiones Regulares/Assets/rilke_letter.txt"
read = str(open(PATH,'r', encoding="utf-8").readlines())

'''
La función compile() la usaré para escribir patrones, esta función me permitirá separar nuestros patrones
en una variable y hará más sencillo de reutilizar la variables para hacer otras busquedas.

'''
# Uso de la función compile()

pattern = re.compile(r'a*')

'''
# Asigno una variable llamada matches a una función finditer() y le paso la variable que contiene
# el texto, la función finditer() me devuelve un iterador con todas las busquedas que encaaja.
# span=(9717, 9721) Me devuelve la línea inclsuive donde está.

Si quisiera usar el span dentro de una notación slice, obtendría la linea exacta de esta palabra

'''

matches = pattern.finditer(read)

# Hago un loop para extraer todas las ocurrencias
for match in matches:
    print(match)


# Notación slice lugar exacto.
# print(read[9717:9721])




