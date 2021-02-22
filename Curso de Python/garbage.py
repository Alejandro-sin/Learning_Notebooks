



'''




'''



words = ['Alberto', 'Sue' , 'Beto']
skills =['DS','Front-Desing-Unicorn','Fullstack']

# Primera forma de obtener una lista con tuplas,
ziped = zip(words, skills)
print(list(ziped))

# Si queremos iterar
for name, skill in zip(words, skills):
    print(name,skill)

# Puedes usar zip para mapear cosas:
mapped = zip(words, skills)
# Desempaquetar
nombres, talentos = zip(*mapped)
print(nombres,talentos)
