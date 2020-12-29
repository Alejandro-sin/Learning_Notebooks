
# Ejercicio 5
# en esta seire ecribiré todos los ejercicios de print que tenga que hacer.

name = "Alejandro"
codeName = "Etrx"
edad = 29
bondadoso = True

print(f"Mi nombre es {name}")

# Ejercicio 6 y 7
print("Mary had a litle lamb.")
print("Its fleece whas white as {}".format('snow'))
print("And everywhre that Maray Went.")
print("."*10)

e1 = "C"
e2 = "h"
e3 = "e"
e4 = "S"
e5 = "e"

#La terminación ,end= ' ' me pone los resultados horizontalmente, con la línea inmediatamente debajo
print(e1+ e2 +e3 +e4 +e5, end =' ')
print(e1+ e2 +e3 +e4 +e5)
print(e1+ e2 +e3 +e4 +e5)

# Ejercicio 8
# Queda recordar mañana que estaba pasando aquí.
# Las variables parecieran tener funciones, o métodos asocaidos. COmo si los objetos tuvieran funcioenes predeterminadas.
# Este ejercicio solo funciona con {}, Con ningún otra string, pareciera que {} posee una definición de "espacio" en el que
# inserto variables, ¿los argumentos de las funciones son otros espacios en memoria?

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■ Errando de gusto.
# formatter = "xxxx"
# <class 'str'>
# xxxx
# <class 'str'>
# xxxx
# xxxx
# xxxx
# xxxx
#
# Process finished with exit code 0
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# formatter = f"{}{}{}{}"
# SyntaxError: f-string: empty expression not allowed
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


formatter = "{}{}{}{}"
print(type(formatter))
print(formatter.format(1,2,3,4))
#  print(formatter.format(1,2,3))
# IndexError: Replacement index 3 out of range for positional args tuple
# print(formatter.format(1,2,3,5,6))■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ PREGUNTA.
# Si le doy más argumentos de los que orginialmente tiene no ocurre nada. Simplemente imprime hasta donde
# le he asignado las cosas.



print(type(formatter.format(1,2,3,4)))
print(formatter.format("one","two","three","four"))
print(formatter.format(False,True,False,True))
# Pareciera que tan es así, que puedo usarlo por su mismo valor, "recursivamente"
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Erase una ve el amor pero tuve que matarlo,lo desangré en abandono, en soledad, en distancia \n",
                       "Renuncias a la felicidad por una causa buena para ser moralmente correcto \n",
                       "Pero pasas una vida arrepintiendote de nunca haber sido feliz, \n",
                       "es un reproche infeliz de los años \n"))

# Qué puedo concluir?
# Los strings usados como slots de memoria? Slots que no tienen el format...
#In this exercise I’m using something called a function to turn the formatter variable into other strings.
# When you see me write formatter.format(...) I’m telling python to do the following:
# 1. Take the formatter string defined on line 1.
# 2. Call its format function, which is similar to telling it to do a command line command named
# format.
# 3. Pass to format four arguments, which match up with the four {}s in the formatter variable.
# This is like passing arguments to the command line command format.
# 4. The result of calling format on formatter is a new string that has the {} replaced with the
# four variables. This is what print is now printing out.

#


