

#Ejercicio-14
# Preguntar al usuario con argv e inputs algo especifico.
# Aquí veo el referrnte de Zork Game, un juego de prints.
# http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq
# https://en.wikipedia.org/wiki/Zork   --> De esto es interesant ever como responde a las preguntas y entiende
# cierto nivel de palabras.



from sys import argv

script, user_name = argv
prompt = '■ '

print("""
    Hello, do you like to answer a lil bit of questions?
    """)
print(f"My name is {user_name} and this is a the script {script}")
print(" What is your age?, Where do you live?, What is your prefer programming Lenguage?")

age = input(prompt)
lives = input(prompt)
lprograming = input(prompt)

print(f"So you have {age} years old, and lives in {lives}, and your choice was {lprograming}, in brief you are the BEST")
