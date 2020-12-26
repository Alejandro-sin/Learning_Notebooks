from random import randint
from IPython.display import clear_output
guessed = False
number =randint(0,100)
while not guessed:
    ans = int(input(("Try to adivinate my number")))
    guessed =+ 1
    clear_output()
    if ans== number:
        print("Congrats!!!!!!!!!!!!!!".format(guessed))
        print(f'Te tomo {guessed} intentos adivinar')
        break
    elif ans > number:
        print("Your number is to low")
    elif ans< number:
        print("Your number is to high")
