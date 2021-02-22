#Ciclos While
# Se ejecuta hasta ser falso.
print("Selecciona una cantidad numerica para guardar en el arreglo")
n = int(input("> "))
print("Selecciona el intervalo en el que quieres moverte")
a = int(input("> "))
def guardar(a):
    i = 0
    while i < n:
        numbers.append(i)
        i = i + a
        print(numbers)
numbers = []
guardar(a)

numbers_for =[]
#Guardar con for n es la cantidad, a es el intervalo al que irá moviendolse
def guardar_for(n,a):
    for i in range(n,a):
        print(f"Estas contando en {i}")
        numbers_for.append(i)
        print(numbers_for)

guardar_for(n,a)



#Study Drill, como hago para hacer una funcion con el while que lo que me haga es que me meta numeros en un arreglo
# Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6)
# with a variable.
# 2. Use this function to rewrite the script to try different numbers.
# 3. Add another variable to the function arguments that you can pass in that lets you change the
# + 1 on line 8 so you can change how much it increments by.
#
# Rewrite the script again to use this function to see what effect that has.
# 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore?
# What happens if you do not get rid of it?
# If at any time you are doing this it goes crazy (it probably will), just hold down CTRL and press c (CTRL-c)
# and the program will abort.