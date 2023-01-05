"""
Encontrar el volumen de una esfera

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
#Importar la librea math para usar pi
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

def volumen(rad):
    """
    Es una funcion, en la cual calcula el valor del volumen de la esfera
    Parametros:
    ------------
        rad : float
            contiene el valor del radio de la esfera
    
    Retorna:
    ------------
        vol : float
            Contiene el valor del volumen de la esfera
    """
    #Crea la variable vol
    vol=0
    #Calcula el valor de la variable vol
    vol=(4/3)*math.pi*rad**3
    #Retorna el valor de la variable vol
    return vol

if __name__ == '__main__':
    #Crea la varibale rad e inicialia con 0
    rad=0
    #Crea la variable val e inicializa con la letra s
    val='s'
    #El ciclo se reptira hast que val sea diferente de s
    while val.lower() =='s':
        #Muestra un mensaje del valor a ingresar
        print("Valor del radio de la esfera")
        #ingreso de la variable rad con la funcion validar
        rad=validar(rad)
        #Muestra el volumen de la esfera
        print(volumen(rad)," cm^3")
        #Ingreso para continuar o no con el programa
        val=input("Desea seguir presione s o culaquier tecla para salir: ")
