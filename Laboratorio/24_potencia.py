"""
Potencia de cualquier numero

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

def potencia(base, exp):
    """
    Es una funcion en la calcula la el resultado de la potencia 
    ------------
        base: float
            variable con el valor de la base
        exp : float
            variable con el valor del exponente de la base
    
    Retorna:
    ------------
        el resultado de la base elevada al exp
    """
    #Retorna el valor de la operacion
    return base**exp

if __name__ == '__main__':  
    #crea una variable base e inicializa con cero
    base=0
    #crea una variable exp e inicializa con cero
    exp=0
    #Crea una variable val e inicializa con s para igresar al ciclo
    val='s'
    #El ciclo se repetira mientras val sea igual a s
    while val.lower() =='s':
        #Muestra el mensaje de ingreso
        print("Ingresar la base:  ")
        #Ingreso de la vase con la funcion validar
        base=validar(base)
        #Muestra un mensaje para ingresar el exponente
        print("Ingresar el exponente:  ")
        #Ingreso del exp con la funcion validar
        exp=validar(exp)
        #Imprime el valor de retorno de la funcion potencia
        print(potencia(base,exp))
        #Ingreso del usuario si desea seguir en el programa
        val=input("Desea seguir presione s o culaquier tecla para salir: ")