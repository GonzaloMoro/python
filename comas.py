# crear una funcion en la cual cuente los puntos y comas de un texto

def puntoYcoma ():
    #iniciamos acumuladores en cero para contar los puntos y comas
    acump=0
    acumc=0
    #le solicitamos al usuario que ingrese un texto
    texto= input('introduzca un texto a continuacion respetando puntos y comas:\n\t')
    #recorremos el texto caracter por caracter
    for x in texto:
        if x== '.': #si encuentra un punto sumamos 1 a "acump"
            acump = acump +1
        elif x== ',': #si encuentra un punto sumamos 1 a "acumc"
            acumc = acumc +1
         
    print('su texto tiene ',acump,' puntos y ',acumc,' comas')  #imprimimos por pantalla la cantidad de puntos y comas