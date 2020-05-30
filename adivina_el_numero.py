nombre = input("Hola invitado, ¿Cómo te llamas?")
print(nombre +""" tienes que adivinar el número en el que estoy pensando del 1 al 10.
Tienes 3 intentos""")

import random
solucion=random.randint(1,10)


for ronda in range(1, 4):
    intento=int(input("Adivina el nº: "))
    if intento > solucion:
        print("El número es menor que " +str(intento) +" prueba de nuevo:")
    elif intento < solucion:
        print("El número es mayor que " +str(intento) +" prueba de nuevo:")
    else:
        break

if intento == solucion:
    print("Enhorabuena " +nombre +" has adivinado el número en el"  +str(ronda)+ "º intento")
else:
    print("Lo siento " +nombre +" el nº que estaba pensando era el " +str(solucion))