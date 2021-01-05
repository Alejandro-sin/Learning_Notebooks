player_one = []
player_two = []
board = {"a":"_","b":"_","c":"_",
         "d":"_","e":"_","f":"_",
         "g":"_","h":"_","i":"_"}


def register_players():
    pone = input("Please write the name of player one: ")
    ptwo = input("Please write the name of player two: ")
    player_one.append(pone)
    player_two.append(ptwo)


def instructions():
    '''
    Muestro las instrucciones  de cómo jugar Ta te Ti  y confirmo que entendieron
    s/n para continuar y ejectuo start.
    '''
    pass



def start():
    f''' La función start:
          1. Muestra el tablero que recibe de Draw()
          2. Pregunta al jugador 1 la posición que desea poner su marca
          3. Hace el update al diccionario  
          4. Devuelve el loop y pregunta por el jugador 2 
        Por par e impar, si es impar el turno del jugador 1 , par del jugador 2.

        ¿Esta dinámica la manejo hasta que el largo
        de los valores del diccionario sea 9?

        * Cuando sea 9 le digo que me termine el juego.


        '''
    instructions()
    register_players()
    draw_board()

    position = input("Selecciona una posición del tablero >  ")
    playerOption = input("Selecciona tu marca > ")

    ## Busco usar un for para recorrer el diccionario y decir qué posiciones están ocupadas.
    
    for values in board.values():
        if values != "_":
            new = input("Esta posición está ocupada selecciona otra > ")
            position = new
            return position
        elif values =="_":
            positioner(position, playerOption)





def positioner(position, playerOption):

    if position not in ["a","b","c","d","e","f","g","h","i"] and playerOption not in ["X","x","O","o"]:
        print("Por favor selecciona una posición/marca válida")
        return positioner()
    elif position =="a":
        board["a"] = playerOption
        draw_board()
    elif position =="b":
        board["b"] = playerOption
        draw_board()
    elif position =="c":
        board["c"] = playerOption
        draw_board()
    elif position =="d":
        board["d"] = playerOption
        draw_board()
    elif position =="e":
        board["e"] = playerOption
        draw_board()
    elif position =="f":
        board["f"] = playerOption
        draw_board()
    elif position =="g":
        board["g"] = playerOption
        draw_board()
    elif position =="h":
        board["h"] = playerOption
        draw_board()
    elif position =="i":
        board["i"] = playerOption
        draw_board()



# Función para dibujar tablero.

def draw_board():
    '''
    Esta función debería dibujar siempre el tablero con los valores actualizados de mi diccionario.
    '''
    board_draw = '''
                                |{a}|{b}|{c}|

                                |{d}|{e}|{f}|

                                |{g}|{h}|{i}|
                                
    '''.format(a=board["a"], b=board["b"], c=board["c"],
               d=board["d"], e=board["e"], f=board["f"],
               g=board["g"], h=board["h"], i=board["i"])
    print(board_draw)







# Terminar el juego
def end_game():
    '''
    Me permite mostrar el resultado al finalizar el juego con un mensaje al ganador
    y me pregunta si quiero jugar de nuevo o cerrar el programa.
    '''

    pass


def run():
    start()



if __name__ == '__main__':
    run()

