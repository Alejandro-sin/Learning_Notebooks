'''
Tipo: Concepto, Ejercicio, Pregunta...
Fuente: libro, curso, ...


Este chunk de código tiene como propósito...
Default Mood
Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

Examples
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"
Notes
Check the Resources tab for some helpful information.

'''
def mood_today(mood = None):
    if mood is None:
        a = "Today, I am feeling neutral"
    else:
        a =  "Today, I am feeling {}".format(mood)
    return a

print(mood_today())

'''
Solucipnes alternativas

Le puedo asignar por defecto un valor a la variable
'''
def mood_toda(mood = 'neutral'):
	return 'Today, I am feeling '+ mood