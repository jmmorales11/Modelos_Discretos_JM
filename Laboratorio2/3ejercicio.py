"""
Calcular el pago del parqueadero de un vehiculos

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
#Importamos la libreria de datetime para hacer operaciones con el tiempo
import datetime
#Importar la libreria time pra la complejidad del tiempo
import time

#@profile
def  leerHora(dato, men):
    """
    Funcion que valida la entrada de la hora 
    Parametros:
    ------------
        dato: string
        men: string
    Retorna:
    ------------
        dato: string
        booleano
        
    """
    #Ingreso del string
    dato= input(men)
    #comparacion del tamaño de la cadena
    if (len(dato)==5):
        #Comparacion de la mitad de la cadena si estan los :
        if(dato[2]==":"):
            #Compara si lo anterior a la miata es mayor a y menor a 23 
            #Compara si lo consiguiente de la mitad es mayor a 0 y menor a 59
            if(int(dato[:2])>=0 and int(dato[:2])<=23 and int(dato[3:])>=0 and int(dato[3:])<=59 ):
                #retorna un booleano y el dato
                return True,dato
            else:
                #La hora ingresada es incorrecta
                print("Hora incorrecta")
                #Retorna un booleano y un dato
                return False,dato
        else:
            #El formato ingresado es incorrecto
            print("Formato incorrecto")
            #Retorna un booleano y el dato
            return False,dato
    else:
        #No se ingresa una hora valida
        print("Hora incorrecta")
        return(False),dato

def solucion (E,L):
    """
    Proceso, en el que se calcula el precio del parquedero
    Parametros:
    ------------
        E: string
        L: string
    Retorna:
    ------------
        No retorna 
    """
    #Variables se guardan los valores del string en enteros para la hora de ingreso
    H1,M1=int(E[:2]),int(E[3:])
    #Variables se guardan los valores del string en enteros para la hora de salida
    H2,M2=int(L[:2]),int(L[3:])
    #Calcula el tiempo de diferencia entre la hora de ingreso y salida
    hora=datetime.timedelta(hours= H2 , minutes=M2)-datetime.timedelta(hours= H1 , minutes=M1)
    #Inicia el preci en 2 ya que el ingreso tiene un valor de 2
    precio=2
    #Comparamos si estuvo en el parquedero solo una hora
    if (int(str(hora)[:1])==1 and (int(str(hora)[2:4])==0 )):
        #Calcula el precio del parqueadero
        precio=precio+3
    else:
        #Comparamos si el valor despues de los : es igual a 0
        if ( int(str(hora)[2:4])==0 ):
            #calcula el precio 
            precio=precio+3+(((int(str(hora)[:1]))-1)*4)
        else:
            #calcula el precio
            precio=precio+3+((int(str(hora)[:1]))*4)
    #Mostramos el precio resultante
    print(precio)
if __name__ == '__main__':
    #Creacion de una variable booleana
    val=False
    #Creacion de ls variables E y L
    E=""
    L="0"
    print("-------------PRECIO PARQUEADERO----------------")
    #Ciclo seguira hasta que la variable boolena sea verdadera
    while( val==False):
        #Ingreso de la hora
        val,E= leerHora(E,"Ingrese la hora de entrada formato HH:MM  ")
    #cambio del valor de la variable
    val=False
    while( val==False or int(L[:2])<int(E[:2])):
        #ingreso validado de la hora
        val,L= leerHora(L,"Ingrese la hora de salida formato HH:MM  ")
    #Llamado a la funcion 
    inicio= time.time()
    solucion(E,L)
    fin= time.time()
    #Muestra la complejidad en tiempo
    print("time ",fin-inicio)