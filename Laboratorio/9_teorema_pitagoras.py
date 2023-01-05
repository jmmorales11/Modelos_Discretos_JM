"""
Teorema de pitagoras

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""

#importamos la libreria math para usar pi
import math

def validar(dato):
    """
    Es una funcion, en la cual valida el ingreso de datos de tipo flotante
    Parametros:
    ------------
        dato: float
            variable con el valor de inicializado
    
    Retorna:
    ------------
        dato : float
            contiene el dato ingresado por el usuario 
    """
     #crea y inicializa una variable con tipo boolena con el valor de true(verdadero)
    con=True
    #El ciclo se repetira mientras la variable con sea verdadera
    while con==True:
        #Se ejecuta si existe algun error el except se ejecutara
        try:
            #Ingreso del dato flotante
            dato=float(input("valor: "))
            #Cambio del valor de la variable booleana a False(falso)
            con=False
        #Se ejecuta si existe un tipo de error
        except:
            #Imprime un mensaje de dato invalido 
            print("Dato invalido ")
    #retorna el dato    
    return dato


def validarEntero(dato):
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
            dato=int(input("Ingrese: "))
            #Cambio del valor de la variable booleana a False(falso)
            con=False
        #Se ejecuta si existe un tipo de error
        except:
            #Imprime un mensaje de dato invalido 
            print("Dato invalido ")
    #retorna el dato
    return dato

def teorema(opc):
    """
    Es una funcion, en la cual se realiza los calculos para encontrar la hipotenusa o los catetos
    Parametros:
    ------------
        opc: int
    
    Retorna:
    ------------
        hip : float 
            contiene el valor de la hipotenusa
        a : float 
            contine el valor del cateto
    """
    #Crea una variable hip y la inicializa con cero
    hip=0
    #Crea una variable a y la inicializa con 0
    a=0
    #Crea una variable b y la inicializa con 0
    b=0
    #Con el parametro si la opc es igual a 1 realiza el proceso
    if(opc==1):
        #Imprime el mensaje de ingreso para el cateto 1
        print("Ingrese el cateto 1")
        #Ingresa el valor de a con la funcion validar
        a=validar(a)
        #Imprime el mensaje de ingreso para el cateto 2
        print("Ingrese el cateto 2")
        #Ingresa el valor de b con la funcion validar
        b=validar(b)
        #La variable hip guarda la operacion para encontrar el valor de la hipotenusa 
        hip=math.sqrt(a**2+b**2)
        #Retornamos el valor de hip el cual es el valor de la hipotenusa
        return hip
    #Con el parametro si la opc es igual a 2 realiza el proceso
    if(opc==2):
        #Imprime un mensaje para el ingreso del valor de la hipotenusa
        print("Ingrese la hipotenusa")
        #Ingreso de hip por la funcion validar
        hip=validar(hip)
        #Imprime un mensaje para el ingreso del valor del cateto b
        print("Ingrese el cateto ")
        #Ingreso del cateto b con la funcion validar
        b=validar(b)
        #La variable a guarda la operacion para encontrar el valor del cateto
        a=math.sqrt(hip**2-b**2)
        #Retorna el valor del cateto 
        return a

if __name__ == '__main__':
    #Crea la variable opc y la inicializa con 0
    opc=0
    #Imprime el mensaje de lo que realiza el programa
    print("Teorema de pitagoras")
    #Muestra la opcion
    print("1 HIPOTENUZA")
    #Muestra la segunda opcion
    print("2 Cateto")
    #Ingreso de la opcion con la funcion validar Entero
    opc=validarEntero(opc)
    #Si opc es igual a 1 envia a la funcion teorema para encontrar la hipotenusa
    if opc==1:
        #Imprime el resultado de la hipotenusa
       print(teorema(opc))
    #Si opc es igual a 2 envia a la funcion teorema para encontar el cateto
    elif opc==2:
        #Imprime el valor del cateto
        print(teorema(opc))
    #Si no cumple con las dos condiciones 
    else:
        #Imprime un mensaje de datos no validos
        print("opcion invalida")



