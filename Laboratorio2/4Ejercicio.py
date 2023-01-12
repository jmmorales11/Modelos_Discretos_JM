"""
Se da un entero positivo N. El objetivo es encontrar la potencia más alta de 2 que divide a N. En otras palabras, tenemos que encontrar el K máximo para el cual N módulo 2^K es 0.

Por ejemplo, dado el número entero N = 24, la respuesta es 3, porque 2 ^ 3 = 8 es la potencia más alta de 2 que divide a N.

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
import big_o
def solucion(N):
    """
    Funcion que calcula el grado mayor 
    Parametros:
    ------------
        N: int 
    Retorna:
    ------------
        grado: int
        
    """
    #Crecion de las variables grado y potencia
    grado=0
    potencia=0
    #Ciclo seguira hasta que la potencia sea menor a N
    while (potencia<N):
        #Sumamos en uno al grado
        grado+=1
        #Calculamos la potencia
        potencia= 2**grado   
    #El ciclo seguira hasta que el residuo de N/potencia sea diferente de 0
    while( N%potencia!=0):
        #Resta al grado menos 1
        grado-=1
        #calcular la potencia
        potencia= 2**grado  
    #Retornamos el grado
    return grado
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
if __name__ == '__main__':
    #Creacion de la variable N 
    N=0
    #Ingreso del numero entero
    N= validar(N,"Ingrese el numero:  ")
    #Llama a la funcion Solucion y muestra el valor de retorno
    print(solucion(N))
    #Uso de la funcion lambda
    numero_ejemplo= lambda ejemplo:N
    #Calcular la complejidad
    best, otros= big_o.big_o(solucion,numero_ejemplo) 
    #Muestra la complejidad
    print(best)   
        