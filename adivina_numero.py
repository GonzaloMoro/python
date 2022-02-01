"""Ejercicio 5.3. Escribir un programa que elija un número al azar, entre 1 y 99, 
y lo mantenga en secreto (utilice la función random.randrange (1,100) del módulo random). 
El programa debe solicitar al usuario que adivine el número. 
Si el número que ingresa el usuario es mayor, el programa debe responder "Incorrecto, mi número es menor"; 
si el número ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". 
En ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. 
Mostrar la cantidad de intentos realizados para adivinar."""

import random

def adivina():
    n = random.randrange(1,100)
    bucle = True
    intentos = 0
    print('"Adivina el numero"\nDel 1 al 99')
    while bucle:    
        a= int(input('introduzca un numero: '))
        if n < a:
            print('Incorrecto, mi número es menor.')
        elif n > a:
            print('Incorrecto, mi número es mayor.')
        elif n == a:
            print('Felicitaciones, acertaste.')
            bucle = False
        intentos = intentos +1
    print('Cantidad de intentos:',intentos)
adivina()