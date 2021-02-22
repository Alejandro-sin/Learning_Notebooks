'''

Este script provienve del Learning Python in the hardway
La idea es crear un generador de clases en pseudo código.

Se debe ejecutar con

$ python name.py english

En la actualidad estoy obteneindo este error.

Traceback (most recent call last):
  File "C:\Logos\Root\Workbench\Curso de Python\2. Intermedios\Programación Orientada a Objetos\classes_generator.py", line 108, in <module>
    question, answer = convert(snippet, phrase)
TypeError: cannot unpack non-iterable NoneType object


Traceback (most recent call last):
  File "C:\Logos\Root\Workbench\Curso de Python\2. Intermedios\Programación Orientada a Objetos\classes_generator.py", line 119, in <module>
    question, answer = convert(snippet, phrase)
ValueError: not enough values to unpack (expected 2, got 0)
PS C:\Logos\Root\Workbench\Curso de Python\2. Intermedios\Programación Orientada a Objetos>

The “TypeError: cannot unpack non-iterable NoneType object” error is raised when you try to unpack values from one that is equal to None.

A common cause of this error is when you try to unpack values from a function that does not return a value. To solve this error, make sure the value you are trying to unpack is a sequence, such as a list or a tuple.



'''


import random
from urllib.request import urlopen
import sys

URL = "http://learncodethehardway.org/words.txt"
#words =[]

phrases = {
    "class %%%(%%%):":"Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :"class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":"class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)":"From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}

# ?
'''
El siguiente pedazo de código dice:

Que si el largo de la lsita de argumentos de la línea de comandos es 2 y el tiene como atrubuto english.
Me devuelva una variable frase verdader o falso.



'''
if len(sys.argv) == 2 and sys.argv[1] == "english":
    phrases_first = True
else:
    phrases_first = False



# load the words from the web
# for word in urlopen(URL).readlines():
#     words.append(str(word.strip(), encoding ="utf-8"))

# Refactor a comprehensions.
words = [str(word.strip(), encoding="utf-8") for word in urlopen(URL).readlines()]


# Funciín para convertir

def convert(snippet, phrase):
    '''
    :param snippet:
    :param phrase:
    :return:

    # 1. Tomo una muestra aleatoria de la población words contada por %%%, me retorna la primera letra capitalziada.
    # 2. Hace un muestreo de palabras contando ***
    # 3. Hago un ciclo para recorrer un rango de 0 a la cuenta de arrobas @@@ que se encuentra.
        * Creo una variable "param_count" que contenga eneteros aleatorios del 1 al 3
        * Hago un muestro de palabras de 1 a 3, las junto mediante una , y Guardo las variables en param_names media
    # 4.

    '''
    # 1 Lista
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    # 2 Lista
    other_names = random.sample(words, snippet.count("***"))

    results =[]
    param_names =[]

    # 3
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(words,param_count)))

    # 4
        for sentence in snippet, phrase:
            result = sentence[:]

            # Nombre de clase falsos
            for word in class_names:
                result = result.replace("%%%", word, 1)

            # Fake other names
            for word in other_names:
                result =  result.replace("***",word,1)

            # fake parameter lists
            for word in param_names:
                result = result.replace("@@@", word, 1)

            results.append(result)
    return results
try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrases_first:
                question, answer = answer, question
            print(question)
            input("> ")
            print(f"Answer: {answer}\n\n")
except EOFError:
    print("Bye")