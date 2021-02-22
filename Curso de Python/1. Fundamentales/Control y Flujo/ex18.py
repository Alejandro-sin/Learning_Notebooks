# reto:
# Hacer un programa que me permita guardar n cantidad de números y que me retnorne le reusltado de su
# suma, que cuando se le meta una letra me arroje un error. Pero cuando se escriba la palabra suma
# me ejecute la funcion suma Esto podría solucionarse mejor con un Whileloop., proque mientras una x condición se de,
# haga esto.

# Repensar este ejericio

lista =[]
def evaluador():
    if option == 'S':
       print('Ingrese un número para la suma acumulada')
       num = input('> ')
       lista.append(num)
       return suma()
    elif option == 'N':
        print('Has dejado de ingresar números')
        return  suma()
    else:
        print('Ingrese un valor apropiado')

def suma():
    for x in lista:
        resultado_suma= (x+x)
        print(resultado_suma)
    return resultado_suma

if__name__='__main__'
print('Ingrese un número para la suma acumulada')
num = input('> ')
num = int(num)
lista.append(num)
print('Desea segir añadiendo numeros? (S/N)')
option=input('> ')
evaluador()

