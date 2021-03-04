'''
La función eval me permite leer un pedazo de código y ejectuar lo que tiene adentro.permite evaluar arbitrariamente las expresiones de puthon e una cadena o pseudocompilados de pyhon, "code-objects"-
code -objests son retornados por la función built-in compile() o puede ser extraído de otros objetos
     como el atributo __code__Puede ser útil cuando estoy intentando evaluar dinámicamente expresiones de python.

     * El uso inadecuado de esta función puede volver mi código inseguro.

     * Evalo toma la expresión, la parsea, compila a bytecode  y la evalua como una expresión de python.

     sintaxis : eval(expression[, globals[, locals]])

     Argumentos opcionales, glabl y locals-



'''
'''
Caundo llamas a la función eval() el contenido d ela expresión es evaluado como una expresión de pyhton
eval puede acceder globalmnete a a nombres de variables como x
'''
x = 100
print(eval("2**4"), eval("sum([8,16,32])"), eval("x*3"))

'''
Evalo solo funciona con expresiones y no compound statements
https://docs.python.org/3/reference/compound_stmts.html

'''