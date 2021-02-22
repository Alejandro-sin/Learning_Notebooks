#En este pedazo de código lo que estoy intentando hacer es ver los
# datos crudos por los que pasa un string antes de ser encode.
#Esto es con el propósito de encontrar una forma de diseecionar ls cosas, de repasar el módulo argv
# Y de ver como trabaja el condoging.
# Algo muy interesante es que despues del 0b la b es por bynary. esos numeros 0b00101 son números binarios...
# 0x son hexadecimales





# Importo módulo sys
import sys

# asigno una salida de script, un entrada a ser encoding, y errores. (Puede ser stricto o no?)
script,input_encoding,error =sys.argv

# Defino mi función principal con 3 parámetros al igual que lo que recibe
def main(lenguage_file, encoding, errors):
    # Leo linea
    line = lenguage_file.readline()
    if line: #si hay linea hago...
        print_line(line, encoding, errors)
        # Imprimo una linea con el encodiging y los errors
        return main(lenguage_file, input_encoding, errors)

def print_line(line, encoding, errors):
    next_lang =line.strip()
    # Estas dos lineas me hacen el encode y el decode
    raw_bites=next_lang.encode(encoding,errors=errors)
    cooked_strings=raw_bites.decode(encoding,errors=errors)
    print(raw_bites, "<==>", cooked_strings)

lenguages = open("languages.txt", encoding="utf-8")
main(lenguages,input_encoding, error)

# ■■■■■■■■■■■■■■■■■■■■■■■ Aprendizaje
# # Siempre que tengo raw_bites debo hacer un decode para obtener la string que oculta.
# Cuando necesite manipular estos strings y python me arroje un encode error es òrque no sabe que esta trabajando
# por lo que necesito hacerle un encode() para obtener esos bytes