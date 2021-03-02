'''
Tipo: Concepto, Ejercicio, Pregunta...
Fuente: libro, curso, ...


Este chunk de código tiene como propósito...

Radians to Degrees
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8
Notes
The number π can be loaded from the math module with from math import pi

'''

from math import pi


# 1rad* 180/pi

def rad_to_deg(rad_value):
    return  round(rad_value * (180/pi),1)

print(rad_to_deg(1))