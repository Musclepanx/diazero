nombre = input("Hola invitado, ¿Cómo te llamas?")
print(nombre +""" tienes que adivinar el número en el que estoy pensando del 1 al 10.
Tienes 3 intentos""")

import random
solucion=random.randint(1,10)

primer_intento = input("Primer intento:")

if primer_intento==solucion:
    print("Enhorabuena " +nombre+ "has adivinado el nº a la primera!")
else:
    input("Lo siento " +nombre+ " inténtalo de nuevo: ")

#en proceso...