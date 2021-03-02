'''
Estudio de al función ennumerate()

Cuando necesito tratar con iteradores y también llevar la cuenta de las iteraciones puedo usar esta función.
Esta función me devuelve una tupla conel índice y el valor.
Puedo usarla para crear diccionarios.

enumerate añade un contador a un iterable y lo devuelve como un objeto enumerado. Este puede ser usado directamente en un loop
o convertido a una lista

'''



lista = ["Pepe", "Anny", "Alejandro"]

for n in enumerate(lista):
    print(n)


# Creo un diccionario.
dict_test = { val: idx +1 for idx, val in enumerate(lista)}

# Obtengo a cantidd de valores que hay en el diccionario.
print(dict_test.values())
dict_test.keys()

print(dict_test)