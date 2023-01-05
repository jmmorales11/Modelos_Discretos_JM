"""
Transformar de libras a kilos y gramos

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

def kilos(libra):
    """
    Es una funcion, transforma de libras a kilos
    Parametros:
    ------------
        libra: float
            variable con el valor en libras
    
    Retorna:
    ------------
        valor en kilos
    """
    #Retorna las libras transformadas en kilos
    return libra*(1/2.2046)

def gramos(libra):
    """
    Es una funcion, transforma de libras a gramos
    Parametros:
    ------------
        libra: float
            variable con el valor en libras
    
    Retorna:
    ------------
        valor en gramos
    """
    #Retorna las libras transformadas en gramos
    return libra *453.59

if __name__ == '__main__':
    #Crea una variable libra y la inicializa con 0
    libra=0
    #Imprime el mensaje para el ingreso en libras
    print("Ingrese los datos en libras")
    #Ingreso de la variable libras llamando la funcion validar
    libra=validar(libra)
    #Imprime las libras trasformaas a kilos
    print("Kilos ",kilos(libra))
    #Imprime las libras transformadas a gramos
    print("Gramos ",gramos(libra))


