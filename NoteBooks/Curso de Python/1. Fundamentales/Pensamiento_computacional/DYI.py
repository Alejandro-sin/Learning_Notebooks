suma = 3 + 3
resta = 3-2
producto = 3*4
division = 3//3
modulo = 25%5
print(suma, resta, producto, division, modulo)

# Cadenas y entradas

numero = '123'
numero_a = '321' * 3
numero_b = '123' + '321'
numero_c = ('Tupa'*3) + '  ' + 'TUM!! -- - > Alias: PunkFormat'
jaszzSound_a = 'Tiss'
jaszzSound_b = 'Tap'

print(numero, numero_a, numero_b, numero_c)
## msg = f'"{jaszzSound_a} {jaszzSound_b}{jaszzSound_a*2}{jaszzSound_b}" Soy un format String ----> Alias: JazzFormat'
##print(msg)

# #https://www.python.org/dev/peps/pep-0498/


strng = "Alejandro-Sin"
comienzo = 0
final = 9
# pasos =1 Me recorre el string y me devuelve de a  1 caracter
# ---->Alejandro
# pasos =n Me recorre el string y me devuelve de a  n caracter
pasos = 2 #Me recorre el string y me devuelve de a  1 caracter#
# ----> Aeado
print (strng[comienzo:final:pasos])

nombre = "Alejandro-sin"
programa = "DataScience"
nom = nombre[0:9]
prog = programa[:4]
nomprog = nom + prog
bre = nombre[-3:]
rama = programa[-7:]
brerama = bre + rama

##print(f'Soy {nomprog} {brerama}')
print(len(nombre))


