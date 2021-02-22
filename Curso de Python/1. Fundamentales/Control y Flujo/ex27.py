# If statement

# Creando un arbol de decisiones.


print(""" Estás en una habitació oscura y tienes 3 puertas. Debes escoger solo 1 de las 3. Escoge la 1, 2 o 3""")
choice=input("> ")

if choice =="1":
    print("Te encuentras con un alienigena de 3 metros que se está comiendo un niño, ¿Que haces?")
    print("1. Le gritas al alienigena ")
    print("2. Le gritas robas su cañón laser y le disparas ")
    print("3. Sales de allí sigilosamente ")
    choice_one = input(">> ")
    if choice_one == "1" or "3":
        print("El alien te mira fijamente y salta sobre tu cuello, "
              "te toma en sus garras como si fueses un saco de carne humano a punto de morir")
    else:
        print("Le has disparado a un alienigena ahora debes correr por tu asquerosa vida humana")
elif choice =="2":
    print("Te encuentras con un pozo muy oscuro del que sale el sonido de una persona pidiendo ayuda, ¿Qué haces?")
    print("1. Le arrojas una cuerda y le ayudas a subir")
    print("2. Ignoras la voz y sigues adelante")
    print("3. Le cuentas una historia de amor hasta que se calle")
    choice_two = input(">> ")
    if choice_two == "1" or "2":
        print("Del pozo sale una mujer fantasmagórica que te arranca las tripas y te ve morir")
    else:
        print("Del pozo sale un espíritu que te muestra el camino para salir de allí")
elif  choice=="3":
    print("Te encuentras a una figura que te dice que es dios ¿Que haces?")
    print("1. Le preguntas: ¿Cual es el sentido de la vida?")
    print("2. Le pides que te salve con un milagro")
    print("3. Lo racionalizas y lo haces desaparecer con el pensamiento")
    choice_three= input(">> ")
    if choice_three == "1" or "2":
        print("Te desintegras con el chasquido de sus dedos y orina sobre tus cenizas")
    else:
        print("Encuentras el origen del conocimiento y siguen caminando")
else:
    print("Esto no es un número... aprenda a escribir")
