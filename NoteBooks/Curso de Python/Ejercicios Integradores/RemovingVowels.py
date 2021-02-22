'''

Tipo:  Ejercicio
Fuente: CodeWars

Este chunk de código tiene como propósito remover las vocales de un string cualquiera


'''

# Primera solución:

def disenvowels(s):
    vowels = ["a","e","i","o","u"]
    for letra in s:
        if letra in vowels:
            letra.replace(letra,"-")
        else:
            print(letra , end ="")

disenvowels("Murcielago")



# Usando el método translate:
'''

El método translate recibe un diccionario para reemplazar elementos.

'''
# ASCII vocals la A y a:
vowels_dict = {65:"",
               97:"",
               }

string = "Zanhaoria"
print(string.translate(vowels_dict))

