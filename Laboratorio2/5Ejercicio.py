"""
Escriba una solución de función que, dados dos números enteros A y B, devuelva una cadena
 que contenga exactamente A letras ' a ' y exactamente B letras ' b ' sin tres letras
  consecutivas iguales (en otras palabras, ni " aaa " ni " bbb " puede aparecer en la cadena devuelta).
Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
#Importa ramdom para mezclar la lista
import random
#Importa big_o para calcular la complejidad
import big_o
def buscar(cadena):
    """
    Es una funcion, Busca una cadena que cumpla con los parametro de no estar repetid mas de 3 veces una letra
    Parametros:
    ------------
        cadena= string    
    Retorna:
    ------------
        cadena= string  
    """
    #Creacion de la variable booleana
    val=True
    #Creacion de la lista con l cadena del parametro
    lis=list(cadena)
    #Seguira hasta que val sea falso
    while(val==True):
        #Mezcla la cadena
        random.shuffle(lis)
        #Convierte la lista en string
        aux="".join(lis)
        #Busca si existe aaa y bbb en la cadena
        if(aux.find('aaa')>=0 or aux.find('bbb')>=0):
            #cambia el valor a verdadero
            val=True
        else:
            #cambia el valor a falso
            val=False
    #Retorna una cadena 
    return aux

def cadenaAB(a,b):
    """
    Es una funcion, crea una cadena 
    Parametros:
    ------------
        a: int
        b: int   
    Retorna:
    ------------
        cadena= string  
    """
    #crea la variable cadena
    cadena=""
    #crea la variable val
    val=0
    #Se añade a la cadena la letra a las A veces
    for i in range(a):
        cadena= cadena+"a"
    #Se añade a la cadena la letra b las B veces
    for i in range(b):
        cadena= cadena+"b"
    #retorna la cadena
    return cadena 

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
    #Crea las varibles
    a,b=0,0
    #Ingreso de los datos validados
    a=validar(a,"Ingrese el primer numero ")
    b=validar(b,"Ingrese el segundo numero")
    #si la resta en valor absoluto es menor a 4 hace el proceso
    if(abs(a-b)<4):
        #Llama ala funcion cadena la cual retorna una caden, y se envia a la funcion buscar e imprime el valor de retorno
        print(buscar(cadenaAB(a,b)))
    else:
        #Los valores no son permitido
        print("valores no permitidos")
    #Calcular la complejidad del programa
    string_ejemplo= lambda ejemplo:cadenaAB(a,b)
    best, otros= big_o.big_o(buscar,string_ejemplo) 
    #muestra la complejidad
    print(best)   
        