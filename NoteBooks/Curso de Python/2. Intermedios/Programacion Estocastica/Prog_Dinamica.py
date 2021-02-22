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
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       Fibonacci    ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
El propósito de esto código es estudiar como se optimiza el algoritmo recursivo de Fibonacci.

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
print(about_code)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         Code         ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
code_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Code         
"""
# Defino mi función fibonacci recursivo.
# La definicón de fibonaccii es:
#    Fn = F(n-1)   +  F(n-2)
def fibonacci_recursivo (n):
    # Le digo que  si el número n que voy recibir es 0 o es 1, me devuelva 1, esto sucede para:
    # 1. Establecer el caso base, el caso de inicio en que arranca mi función
    # Si reemplazo 0 y 1 por definición obtendría números negativos:
    #              F(0) = -1-2 ==> Fn = -3
    #              F(1) = 0-1 ==> Fn = -1
    #              F(2) = 1 + 0 ==> Fn = 0
    if n == 0 or n ==1:
        # Al establecer que no me sirven estos enteros negativos le digo que cada vez que encuentre un 0 y un 1 como input
        # que siempre me retorne 1 y me lo guarde en memoria.
        return 1
    for i in range(n):
       iteracion = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
       print(iteracion)
    return iteracion

# **********Para optimizar este algrotimo debo guardar todos los resultdaos de los cómputos que hao una y otra vez
# Los problemas que sean empalmados son los que nos van a permitir  ejecutar un problema recursivo.

# Defino mi función fibonacci dinamico, le paso n para calcularlo y le paso memo como una lista donde almacenaré mis
# resultados de cómputo
def fibonacci_dinamico(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = resultado

        return resultado


if __name__=="__main__":
    print(code_literal)
    # Para cambiar el límite de recursividad
    sys.setrecursionlimit(10002)
    n = int(input('Digita el número fibonacci a calcular:  '))
    # resultado = fibonacci_recursivo(n)
    resultado_d = fibonacci_dinamico(n)
    # print(f'El número fibonacci recursivo de {n} es {resultado} \n')
    print(f'El número fibonacci dinamico de {n} es {resultado_d} \n')

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■        Errors        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
error_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Error         

Pregunta: No entiendo como funciona a nivel matemático lo que estoy ejectuando.

"""
print(error_literal)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  Learn and visualize ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
learnV_literal ="""
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ . . . Learn and visualize         
https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
"""
print(learnV_literal)