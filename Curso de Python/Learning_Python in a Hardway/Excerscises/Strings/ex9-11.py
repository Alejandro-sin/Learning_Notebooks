
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days\n", days)
print("Here are the months \n", months)
print("\tEspacio tabulador")
print("Separar\\linea, aquí quiero escapar la comilla simple \'")
print("Separando las \"comillas dobles \" ")
print("Que es ASCII bell (BEL):? \a   Es como un simbolo")
print("Es un back \bspace...")
print("Esto se llama formfeed FF \f")

# Aquí podemos ver y entender los demás escapes pare crear textos de mejro formato. Revisarlo al detalle.

print('''
Haré una lista:
\t■ Entender que puedo escapar con '' Dentro de un string
\t■ Entender que puedo hacer tabular con t con n, un salto de línea 
\t■ Entender que backslah me escapa 
''')

#Otra forma de hacer un print.

print("How old are u?", end=' ')
age = input()
print(f'Your age is {age} years old')
