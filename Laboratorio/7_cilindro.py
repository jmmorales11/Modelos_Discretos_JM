"""
Calcular el area de un cilindro

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

def areaCilindro():
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
    #Inicializa y crea el variable area 
    area=0
    #Inicializa y crea la variable radio
    radio=0
    #Inicializa y crea la variable altura
    altura=0
    #Imprime el mensaje para el ingreso del radio
    print("Ingrese el radio ")
    #Ingreso del radio llamando a la funcion validar
    radio=validar(radio)
    #Imprime el mensaje para el ingreso de la altura
    print("Ingrese la altura ")
    #Ingreso de la altura con la funcion validar
    altura=validar(altura)  
    #En la variable area se gurada el resultado del area del cilindro
    area=2*math.pi*radio*(altura+radio)
    #Retornamos el valor del area
    return area


if __name__ == '__main__':
    #Crea la variable e inicializa con la letra s para entrar en el bucle
    val='S'
    #Entra al ciclo 
    while val.lower() =='s':
        #Imprime el mensaje de presentacion del programa
        print("Area de un cilindro  ")
        #Imprime el valor de retorno de la funcion areaCilindro()
        print(areaCilindro())
        #Ingreso del usuario para seguir o no en el programa
        val=input("Desea seguir presione s o culaquier tecla para salir: ")