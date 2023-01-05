"""
Encontrar el angulo faltante en un triangulo

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

def angulo(pAngulo, sAngulo):
    """
    Es una funcion, en la cual calcula el valor del angulo faltante
    Parametros:
    ------------
        pAngulo: float
            contiene el valor del primer angulo
        sAngulo: float
            contiene el valor del segundo angulo
    Retorna:
    ------------
        retorn el valor del angulo faltante
    """
    #La variable tAngulo guarda la suma de los dos angulos
    tAngulo=pAngulo+sAngulo
    #Si cumple ser menor a 180
    if(tAngulo<180):
        #retorna el valor del angulo faltante
        return 180-tAngulo
    else:
        #La suma de los angulos es incorrecto
        print("Los agulos no son correctos")
        return 0

if __name__ == '__main__':
    #Crea la variable pAngulo e inicializa con -1 para entrar al ciclo
    pAngulo=-1
    #Crea la variable sAngulo e inicializa con -1 para entrar al ciclo
    sAngulo=-1
    #Ciclo se repetira hasta que el valor sea menor mayor a 0
    while int(pAngulo)<=0:
        #mensaje para ingresar el primer angulo
        print("Ingrese el primer angulo")
        #ingreso del primer angulo con la funcion validar
        pAngulo=validar(pAngulo)   
    #Ciclo se repetira hasta que el valor sea menor mayor a 0 
    while  int(sAngulo)<=0:
        #mensaje para ingresar el segundo angulo
        print("Ingrese el segundo angulo")
        #ingreso del segundo angulo con la funcion validar
        sAngulo=validar(sAngulo)
    #Muestra el valor del angulo faltante
    print(angulo(pAngulo,sAngulo))