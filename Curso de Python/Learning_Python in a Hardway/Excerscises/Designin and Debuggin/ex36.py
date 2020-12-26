#Designing and Debuggin

# 1. Tod if debe llevar un else
# 2.No nestear mas de 2 if
# 3.  Tratar los if como parrrafos. donde el if elif else son  juntamos como una serie de sentencias.
# 4. MI LÓGICA BOLEANA ENTRE MÁS SIMPLE DE ENTENDER MEJOR.
# No usar mucho el while-loop,
# El debugger es como un scan entero de una persona enferma, puede que no encuentres infromación útil y específica.
# La mjeor manera de debugguear es con la sentencia print().
# Seguir el principio " Code a litle, run a litle, fix a litle".



#■■■ TO DO LIST ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Cada habitación puede ser una función con una estructura de control diferente para practicar.


#Defino las variables de mi juego.


# La vida del jugador es una variable.
life = 3


def start():
    print("""
        ■■■■■■■■■■■■■■■■■ BIENVENIDO GAREN
        
        El príncipe Malzhar te ha capturado en una dimensión, para que decidas tu suerte...y tu escaza inteligencia
        -El vacío cree puede tragarse al Honor- Pensaste, digno de un guerrero. 
        -No necesariamente de un sabio dijo en voz alta el príncipe Malzahar-. había escuchado tus pensamientos, tenías
        que salir de allí, todos lso secretos de Demacia estaban en riesgo. Garen ve dos portales a lo lejos.
        
        Escoge  el portal A o B para escapar del pensamiento de Malzahar.
        
    """)

    selection = input(">  ")
    return first_choice(selection)


def first_choice(selection):
    if selection == "A" or "a":
        print("""Cuando entras al portal ves las llanuras de Jonia, a lo lejos y una sombra está parada en medio de la nada, y blande las
            hojas plateadas de dos shurikens enormes Zed te mira, y el cielo se tiñe de rojo. Va a haber pelea. ¿Qué haces?

                A. Te arrojas sobre él con tu espada giratoria
                B. Tratas de razonar con Zed
                """)
        selection = input("> ")
        return jonia_room(selection),

    elif selection == "B" or "b":
        print("""Cuando entras al portal ves las montañas negras de Noxus, a lo lejos se alza leviatán la fortaleza móvil de Swain, y está quieta,
                    sin embargo esta situación es mala, si te ven podrían eliminarte con sus cañones cuervo, pero si te infiltras, 
                    podrías tener una oportuniddad, como ningún otra para acabar con Noxus desde su cabeza. ¿Qué haces?

                        A. Te infiltras en la fortaleza escalando sus muros.
                        B. Esperas todo el día para saber qué hacen.
                   """)
        selection = input("> ")
        return jonia_room(selection), life
    else:
        print("Aprende a escribir, Manco!")

def jonia_room(selection):
    if selection == "A" or "a":
        life = 2
        print(f"""Zed es mucho más veloz que tu, y estás en su tierra. Te clava sus cuchillas sombra y pierdes 1 de vida.
            Te quedan {life}  vidas.
            Ves venir al maestro ninja a toda velocidad.¿ Que haces?
        
                A. Esperas pacientemente a que esté cerca y usas tu Ultimate
                B. Te paras en posición defensiva y observas sus sombras.
                """)
        selection = input("> ")
        if selection == "A" or "a" or "B" or "b":
            print("Estabas muerto desde el principio, las sombras te devuelven a la prisión de Malzahar.")
            return start()
        else:
            print("Aprende a escribir!!")
        return life

## Porqué me está guardando la variable selecion como B?



def noxus_room():
    pass

def game_over():
    pass

def win():
    pass



def run():
    start()



if __name__ == '__main__':
    run()