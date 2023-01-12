"""
Encontrar el primer numero que no se repite

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""

import big_o
import random
import string
import time
def validar(dato, men):
    """
    Es una funcion, en la cual valida el ingreso de datos de tipo entero
    Parametros:
    ------------
        dato: int
    
    Retorna:
    ------------
        dato : int 
            contiene el dato ingresado por el usuario 
    """
    #crea y inicializa una variable con tipo boolena con el valor de true(verdadero)
    con=True
    #El ciclo se repetira mientras la variable con sea verdadera
    while con==True:
        #Se ejecuta si existe algun error el except se ejecutara
        try:
            #Ingreso del dato entero 
            dato=int(input(men))
            #Cambio del valor de la variable booleana a False(falso)
            con=False
        #Se ejecuta si existe un tipo de error
        except:
            #Imprime un mensaje de dato invalido 
            print("Dato invalido ")
    #retorna el dato
    return dato

def cadenaRep(cadena, tam, inicia , repite):
    """
    Proceso recursivo retorna la letra que no se repite
    Parametros:
    ------------
        cadena: list
        tam: int
        inicia: int
        repite: int
    Retorna:
    ------------
        no retorna ningun valor
        
    """
    #Rrecorremos la lista
    try:
        for i in range(tam):
            #Compara si el valor de la lista es igual 
            if cadena[inicia]==cadena[i]:
                #Suma un numero a la variable repetir
                repite+=1
        #Si la variable repetir es mayor 1 llama nuvamente a la funcion
        if repite>1:
            #Llamado a la funcion y cambia el valor de inicio a mas 1
            cadenaRep(cadena,tam,inicia+1,0)
        else:
            #Imprime la primera letra que no se repite
            print(cadena[inicia])
    except:
        print(-1)


if __name__ == '__main__':
    #Inicia la vaiable en 0
    inicia=0
    #Inicia la variable en 0
    repite=0
    #Inicia la variable en 0
    valor=0
    #Inicia la variable cadena
    numeros=0
    #Crea una lista con la cadena hecha
    lis=[]
    #ingreso de la cantidad de palbras a generar 
    valor=validar(valor,"Ingrese la cantidad de numeros a insertar ")
    #Generar la cantidad de palabras deseadas por el usuario
    for i in range(valor):
        #en la variable se guarda las palabras generadas en la funcion palabraG
        numeros=validar(numeros,"Ingrese el valor a insertar ")
        lis.append(numeros)
    inicio= time.time()
    #Tamaño de la cadena
    tam= len(lis)
    #Mostramos la cadena generada
    print(lis)
    #Llamado de la funcion cadenaRep
    cadenaRep(lis, tam, inicia , repite)
    fin= time.time()
    #Muestra la complejidad en tiempo
    print("time ",fin-inicio)
    