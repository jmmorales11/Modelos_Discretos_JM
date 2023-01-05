
"""
Encontrar la densidad de un objeto

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
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

def densidad(masa,vol):
    """
    Es una funcion, en la cual calcula el valor de la densidad del objeti
    Parametros:
    ------------
        masa: float
            contiene el valor de la masa del objeto
        vol: float
            contiene el valor del volumen del objeto
    Retorna:
    ------------
        den : float
            contiene el valor de la densidad del objeto
    """
    #Calcula el valor de la densidad 
    den=masa/vol
    #Retorna el valor de la densidad
    return den

if __name__ == '__main__':
    #crea la variable masa e inicializa con 0
    masa=0
    #Crea la variable vol e inicializa con 0
    vol=0
    #Crea la variable val e inicializa con la letra s
    val='s'
    #El ciclo se reptira hast que val sea diferente de s
    while val.lower() =='s':
        #Muestra un mensaje del ingreso de la masa
        print("Ingrese la masa del objeto en g")
        #Ingreso de la masa con la funcion validar
        masa=validar(masa)
        #Muestra un mensaje para el ingreso del vol
        print("Ingrese el volumen del objeto en ml")
        #Ingreso del volumen con la funcion validar
        vol=validar(vol)
        #Muestra la densidad del objeto
        print(densidad(masa,vol)," g/ml")
        #Ingreso para continuar o no con el programa
        val=input("Desea seguir presione s o culaquier tecla para salir: ")