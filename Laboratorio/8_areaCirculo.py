"""
Calcular el area de un circulo

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


def circulo(radio):
    """
    Es una funcion, en la cual se calcula el area del circulo
    Parametros:
    ------------
        radio : float
            Contiene el radio del circulo
    
    Retorna:
    ------------
        area : float
            contiene el area del circulo
    """
    #Crea una variable area e inicializa con 0
    area=0
    #En la variable area se guarada el resultado de la operacion
    area= math.pi*radio**2
    #Retorna el valor del area
    return area



if __name__ == '__main__':
    #Crea la variable radio e inicializa con 0
    radio=0
    #Crea una variable tipo string e inicializa con la ltra s para entrar al ciclo
    val='s'
    #El ciclo terminara cuando la variable val sea diferente de s
    while val.lower() =='s':
        #Imprime el mensaje para el ingreso del dato
        print("Radio del circulo")
        #Ingresa el radio del circulo con la funcion validar
        radio=validar(radio)
        #Imprime el valor del area 
        print(circulo(radio))
        #Ingreso de la letra para que el programa siga o no
        val=input("Desea seguir presione s o culaquier tecla para salir: ")