

#Reading files.
# Im going to write to ways of avoid hardcode my readFiles. Hardcodes means that i write directly on my variable
# what are supossed to be a input from the user. Two aproachs, argv and inputs.
#fileName  ex15_sample.txt

from sys import argv
#argv solution
script, fileName = argv
txt = open(fileName)
read = txt.read()
print(f"This is your {fileName} \n")
print(read)

#input solution
print("\n Tell me the name of your file: \n")
i_fileName = input("> ")
i_txt = open(i_fileName)
print(i_txt.read())
i_txt = (i_fileName)

print(f"""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

This would be a brief analysis for latter study:   
    1.The type of variable txt is " {type(txt)} ".
Se crea un objeto de tipo archivo. Ver estos objetos....más de.
    2.The type of variable read is " {type(read)} ".
    3.The type of variable fileName is " {type(fileName)} ".
    4.The type of variable script is " {type(script)} ".
    5.The type of variable argv is " {type(argv)} ".
    6.The type of variable argv is " {type(i_txt)} ".

¿What is this?, Find out
Use only input and try the script that way. Why is one way of getting the filename better than
another?

La diferencia radica en que con argv al ejecutarlo peudo ejecutar cualquier script, si hago ex14.py etc etc...
me trae el otro archivo. Esto me lo está guardando en una lista

Con input solo recibo un str.


Have your script also call close() on the txt and txt_again variables. It’s important to
close files when you are done with them. ?????

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")