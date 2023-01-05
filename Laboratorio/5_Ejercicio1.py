"""
Calcular la expresion y=(x^z)/2

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
def validar(dato):
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
            dato=int(input("Ingrese el dato: "))
            #Cambio del valor de la variable booleana a False(falso)
            con=False
        #Se ejecuta si existe un tipo de error
        except:
            #Imprime un mensaje de dato invalido 
            print("Dato invalido ")
    #retorna el dato
    return dato

def expresion(cant):
    """
    Es una funcion en la cual calcula la expresion x^z/2
    Parametros:
    ------------
        cant : int
            contiene la cantidad de veces que quiere ser sumanda la expresion 
    
    Retorna:
    ------------
        res: int
            contiene el valor calculado 
    """
    #Crea una variable base tipo entero inicializado con 0
    base=0
    #Crea una variable exp tipo entero inicializado con 0
    exp=0
    #Crea una variable res tipo entero inicializado con 0
    res=0
    #Ciclo que se repetira hasta que i sea igual a la variable can
    for i in range(cant):
        #Presenta por pantalla El mensaje para que ingrese la base de la expresion
        print("Ingrese la base: ")
        #Ingreso de la base con la funcion validar
        base=validar(base)
        #Presentamos por pantalla el mensaje para ingresar el exponente
        print("Ingrese el exponente: ")
        #Ingreso del exponente de la expresion llamando a la funcion validar
        exp=validar(exp)
        #Calcular el resultado 
        res=res+((base**exp)/2)
    #Retornar el valor de res
    return res

if __name__ == '__main__':
    #Crea la variable cant e inicailizar en cero
    cant=0
    #Imprime un mensaje de la cantidad de veces a realizar la expresion
    print("Cantidad de veces a realizar la expresion  ")
    #Ingreso de la cant con la funcion validar
    cant=validar(cant)
    #Presenta el resultado
    print(expresion(cant))
