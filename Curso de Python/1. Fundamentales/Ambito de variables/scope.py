'''

Este programa tiene como propósito explroar el ámbito de las variabels en pyhton
con global y nonlocal.

'''
def prueba_ambitos():
    def local():
        algo = "ALGO LOCAL"
        print(algo)

    def non_local():
        nonlocal algo
        algo ="ALGO NO LOCAL"
        print(algo)

    def hacer_global():
        global algo
        algo ="ALGO GLOBAL"
        print(algo)

    def error():
        '''
        Aquí me devuelve lo que la vairable algo, pero de la def non local.
        '''
        print(algo)

    algo= "algo prueba"
    local()
    non_local()
    hacer_global()
    error()

prueba_ambitos()

