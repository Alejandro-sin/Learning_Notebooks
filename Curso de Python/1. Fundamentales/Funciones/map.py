'''

La funcion map devuelve un iterable que puede ser muy bueno en el moneto de manejar recursos.


'''

tienda =[34,2,44]
panaderia =[3,4,5]
masbarato = map(min,tienda,panaderia)
print(masbarato)


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# Creo una función que me elimine el nombre, y me deje Dr Aplleido
def split_title_and_name(person):
    # Accedo a solo una parte d ela matriz y aplico split
    title = person.split()[0]

    # Voy al ultimo string
    lastname = person.split()[-1]

    # Imprimo con el formato.
    return '{} {}'.format(title, lastname)


# Uso map para aplciar la función a toda la lista.
a = list(map(split_title_and_name, people))
print(a)
