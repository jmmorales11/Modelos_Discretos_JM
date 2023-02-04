def leerVias():
    """
    Este metodo nos 
    Parametros
    -----------
        No contiene parametros
    Returns:
        via: Contiene a la via elejida.
    """
    #Inicializar la variable via 
    via=""
    #Validar el ingreso de las vias disponibles en el sistema 
    while via!="Pifo" and via!="Tumbaco" and via!="Cumbaya" and via!="Sangolqui" and via!="s":
        #Ingreso de la via por el usuario 
        via=input(">>Introduzca la via: ")
    #Retornar la via escogida 
    return via

def leerEstado():
    """
    La funcion permite el ingreso del estado de la via 
    Parametros
    -----------
        No contiene parametros
    Returns:
        estado : Contiene el valor del estado de la via.
    """
    
    #Inicia el estado de la via para ingresar al ciclo
    estado= -1
    #Inicia el estado del val 
    val=True
    #Ingresa al ciclo 
    while val==True:
        #Nos permite validar el error para que el programa no caiga
        try:
            #Nos valida el estado permitido
            while estado!=0 and estado!=1:
                #Ingreso del estado de la via
                estado=int(input(">>Introduzca el estado de la via: ") )
            #Cambio del val para salir del bucle 
            val=False
        except:
            #Sigue en el ciclo
            val=True
            #Muestra el mensaje del valor invalido
            print("Valor invalido")
    #Retorna el estado de la funcion
    return estado

def agenteSistema():
    """
    Proceso del agente inteligente de un sistema de vias con trafico o 
    despejadas, el objetivo es tener las calles libres.
    Parametros
    -----------
        No contiene parametros
    Returns:
        No contiene valores de retorno
    """
    #Creacion de un Diccionario con las cuatro calles para el agente inteligente
    objetivo = {'Pifo': '0', 'Tumbaco': '0', 'Cumbaya':'0','Sangolqui':'0'}
    #Inicia la variable de costo
    costo=0
    #Inicia la variable val con verdadero para ingresar al ciclo
    val=True
    while val==True:
        #Imprime el mensaje de las calles disponibles para el agnte 
        print("Ingrese las vias disponibles\nvias : Pifo, Tumbaco, Cumbaya y Sangolqui ingrese una de las 4 vias ")
        #Si el usuario desea salir del programa dee ingresar la letra s
        print("Si desea salir del sistema presione s")
        #Llamado de la funcion leerVias para el ingreso de las 4 vias dispobles en el sistema 
        via=leerVias()
        #Si el valor de la via es igual a s, la ejecucion termina
        if via=='s':
            #Salida del ciclo
            break
        #Muestra los estados disponibles para cada via
        print("Estado 0=sin trafico   1=trafico")
        #Lee los estados disponibles
        estado=leerEstado()
        #Si la via ingresada es igual a Pifo se ejecutaran las instruciones dentro del condicional 
        if via=='Pifo':
            #Muestra la via ingresada
            print(via)
            #Compara los estados 
            if estado==0:
                #Muestra el mensaje, que la via esta libre
                print("La via esta libre")
                #Muestra el costo el cual no aumenta 
                print("Costo ", costo)
            else:
                #Muestra el mensaje que la via tiene trafico
                print("La via tiene trafico")
                #El costo aumenta
                costo+=1
                #Cambia el objetivo de la via
                objetivo['Pifo']='0'
                #Imprime el costo actual
                print("Costo ", costo)
                #Muestra el mensaje que la via esta libre
                print("Via libre")
        #Si la via ingresada es igual a Tumbaco se ejecutaran las instruciones dentro del condicional 
        if via=='Tumbaco':
            #Muestra la via 
            print(via)
            if estado==0:
                #Muestra el mensaje que la via esta libre
                print("La via esta libre")
                #Se imprime el costo actual
                print("Costo ", costo)
            else:
                #Muestra el mensaje que la via tiene trafico
                print("La via tiene trafico")
                #Aumenta el costo 
                costo+=1
                #Cambia el objetivo de la via
                objetivo['Tumbaco']='0'
                #Imprime el costo actual
                print("Costo ", costo)
                #Muestra el mensaje que la via esta libre
                print("Via libre")
        #Si la via ingresada es igual a Cumbaya se ejecutaran las instruciones dentro del condicional 
        if via=='Cumbaya':
            #Imprime el mensaje De la via 
            print(via)
            if estado==0:
                #Muestra el mensaje de la via libre
                print("La via esta libre")
                #Muestra el costo actual sin aumentar 
                print("Costo ", costo)
            else:
                #Muestra el mensaje que la via tiene trafico
                print("La via tiene trafico")
                #Aumenta el costo 
                costo+=1
                #Cambia el objetivo de la via
                objetivo['Cumbaya']='0'
                #Imprime el costo actual
                print("Costo ", costo)
                #Muestra el mensaje que la via esta libre
                print("Via libre")
        #Si la via ingresada es igual a Cumbaya se ejecutaran las instruciones dentro del condicional 
        if via=='Sangolqui':
            #Muestra el mensaje de la via
            print(via)
            if estado==0:
                #Muestra el mensaje de la via libre
                print("La via esta libre")
                #Muestra el costo actual sin aumentar 
                print("Costo ", costo)
            else:
                #Muestra el mensaje que la via tiene trafico
                print("La via tiene trafico")
                #Aumenta el costo 
                costo+=1
                #Cambia el objetivo de la via
                objetivo['Sangolqui']='0'
                #Imprime el costo actual
                print("Costo ", costo)
                #Muestra el mensaje que la via esta libre
                print("Via libre")
        


if __name__ == '__main__':
    #Llamado al proceso del agente inteligente 
    agenteSistema()