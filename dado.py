# hacemos una funcion en la cual tengamos 2 dados
# importamos la libreria random para generar numeros al azar

import random #importamos la libreria Random

def dado ():
    lanzamientos = int(input('introduzca la cantidad de veces que desea lanzar los dados:\n\t'))    #El usuerio introduce un numero entero
    for x in range(lanzamientos):print('dado 1: ',random.randrange(1,7)),print('dado 2: ',random.randrange(1,7)),print('--------------')
    #hacemos que se repita la cantidad de veces que selecciono el usuario con el numero solicitado, luego imprimimos los resultados