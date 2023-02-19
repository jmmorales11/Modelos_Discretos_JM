"""
Agente Inteligente de un sistema para autoservicio

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.2
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def imagenes(opc):
    """
    
    Parametros
    -----------
        opc: int
            contiene la opcion para usar en el proceso
    Returns:
        No retorna nada 
    """
    #Comparar si la opcion es igual a 1
    if (opc==1):
        #Mostramos la imagen de ingreso del automovil al autoservicio
        img = mpimg.imread('Entrando.jpg')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        #Mostramos la imagen de realizando el pedido 
        img = mpimg.imread('atendiendo.jpg')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        #Mostramos la imagen de salida del automovil
        img = mpimg.imread('Salida.jpg')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    #Si la opcion es igual a 0
    if(opc==0):
        #Muestra una imagen que no contiene vehiculo y todo esta cerrado
        img = mpimg.imread('Vacio.JPG')
        plt.imshow(img)
        plt.axis('off')
        plt.show()


def leerEstado():
    """
    Esta funcion nos retorna el estado escogido o la opcion s en mayuscula o minuscula para ser utilizada en el programa. 
    Parametros
    -----------
        No contiene parametros
    Returns:
        estado: string 
            guarda el valor ingresado por el usuario valiadado 
    """
    #Inicializar una variable con un valor booleano
    val=True
    #El ciclo terminara si el val es falso
    while val==True:
        #Para salatar algun error 
        try:
            #El ciclo continuara hasta que el val sea falso
            while val==True:
                #Ingreso del estado 
                estado=input(">> ")
                #comparar los valores se encunetran dentro del rango
                if estado=='0' or estado=='1' or estado=='s' or estado=='S':
                    #Cambiar el valor de val
                    val=False
        except:
            #Mensaje por panatalla
            print("Dato erroneo")
    #retorna el mensaje
    return estado
def apagar():
    """
    Funcion que permite ingresar el valor de Si o No a la pregunta de si desea salir del prigrama.
    Parametros
    -----------
        No contiene parametros
    Returns:
        apg: string 
            guarda el valor ingresado por el usuario valiadado para salir o no del programa 
    """
    #Creacion de la variable e inicializar para ingresar al ciclo
    apg='a'
    #El cilo continuara hasta que ingrese los valores de s o n
    while apg!='s' and apg != 'n':
        #Ingreso por el usuario de la variable
        apg=input(">> ")
    #retornmos la letra ingresada
    return apg
def agente():
    """
    Proceso del agente para el restaurante
    Parametros
    -----------
        No contiene parametros
    Returns:
        No retorna valores
    """
    #Estado objetivo de nuestro agente
    objetivo = {'Ventana': '0', 'Entrada': '0','Pedido': '0', 'Salida': '0'}
    #Variable costo
    costo=0

    #Ciclo termina si el usario desea salir del programa 
    while True:
        #Da la Bienvenida al programa y las instrucciones para salir del programa
        print("Bienvenido al restaurante")
        print("Si quiere apagar el servicio presione s")
        print("Estado de la entrada \n1= abrir, 0 = cerrado")
        #Llamado de la funcion para validar el estado 
        estadoE=leerEstado()
        #Condicion si sale del programa 
        if estadoE=='s'or estadoE =='S':
            #Muestra por pantalla si el usario esta seguro de apagar el aplicativo
            print("El sistema se usa 24 horas esta seguro que desea apagarlo")
            #Opciones de apagar si o no
            print("s")
            print("n")
            #Llamado de la funcion para validar si se quiere o no apagar el aplicativo
            apag=apagar()
            #Si es escogida la opcion Si el programa termina
            if (apag=='s'):
                break
            #Si no se realiza el llamado al agente nuevamente 
            else:
                agente()
        #Si si el ingeso 
        if (estadoE=='1'):
            #Cambio del estado de la entrada
            objetivo['Entrada']='1'
            #Cambio del estado de la ventana
            objetivo['Ventana']='1'
            #Cambio del estado del pedido
            objetivo['Pedido']='1'
            #Mostrar las imagenes
            imagenes(1)
            #Mostar el estado 
            print(objetivo)
            #Se entrega el pedido
            print("Pedido entregado")
            #Cambo de estado de la entrada
            objetivo['Entrada']='0'
            #Cambio del estado de la vetana 
            objetivo['Ventana']='0'
            #Cambio del estado del pedido
            objetivo['Pedido']='0'
            #Cambio del estado de la salida
            objetivo['Salida']='1'
            #Vehiculo sale del autoservicio
            print("Vehiculo salio")
            #Cambio del estado de la salida
            objetivo['Salida']='0'
            #Mostra el objetio
            print(objetivo)
            #El costo aumenta en 1
            costo+=1
            #Muestra el costo
            print("Costo ", costo)
        else:
            #Mostrar la imagen la cual no consta con vehiculos
            imagenes(0)
            #Muestra el mensaje
            print("No existe vehiculos en cola")
            #Muestra el objetivo
            print(objetivo)
            #Muestra el costo
            print("Costo ", costo)

            
#Main de la funcion
if __name__ == '__main__':
    #Llamado del agente
    agente()
    

