"""
Tiene como propósito explorar los diccionarios como estructuras de datos.

"""


my_dict = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
}

for keys in my_dict.keys():
    print(keys)

for keys, values in my_dict.items():
    print(keys + "  _   " + str(values))
