import math
import datetime
import pymongo
import os
from dateutil.relativedelta import relativedelta
import re 
from colorama import Back, Fore, init
import time
from memory_profiler import profile

def leerNombre(nombre):
    """
    Es una funcion, en la cual valida el ingreso de un nombre
    Parametros:
    ------------
        nombre: string    
    Retorna:
    ------------
        nombre : string
            Guradar el valor del nombre ingresado
    """
    #crea una variable booleana e inicializa con false (falso)
    con=False
    num=0
    nombre=""
    #Ciclo acabara al momento que el valor de con cambien  a true
    while con==False :
        #Ingreso del nombre
        
        nombre=input(">> ")
        #crear una lista con el nombre ingresado
        lis=list(nombre)
        #Ciclo para conocer el contenido de la lista
        inicio= time.time()
        for i in range(len(lis)):
            #Comparar si la lista contiene letras entre a y z
            if(lis[i].lower()==" " ):
                num+=1
            if lis[i].lower()>='a' and lis[i].lower()<='z' or lis[i].lower()==" " :
                #cambiar el valor de con a true
                con=True
            #si contiene numeros o caracteres especiales
            else:
                #cambiamos el valor a false
                con=False
    #retorna el nombre con la primera letra mayuscula
    if num!=1:
        print("Dato invalido ingrese de nuevo ")
        leerNombre(nombre)
    fin= time.time()
    return nombre.lower().title(), fin-inicio

def leerCita(cita):
    """
    Es una funcion, en la cual valida el ingreso de un nombre
    Parametros:
    ------------
        nombre: string    
    Retorna:
    ------------
        nombre : string
            Guradar el valor del nombre ingresado
    """
    #crea una variable booleana e inicializa con false (falso)
    con=False
    num=0
    #Ciclo acabara al momento que el valor de con cambien  a true
    while con==False :
        #Ingreso del nombre
        cita=input(">> ")
        #crear una lista con el nombre ingresado
        lis=list(cita)
        #Ciclo para conocer el contenido de la lista
        for i in range(len(lis)):
            #Comparar si la lista contiene letras entre a y z
            if lis[i].lower()>='a' and lis[i].lower()<='z' or lis[i].lower()==" " or lis[i].lower()>"0" :
                #cambiar el valor de con a true
                con=True
            #si contiene numeros o caracteres especiales
            else:
                #cambiamos el valor a false
                con=False
    #retorna el nombre con la primera letra mayuscula
    return cita

def fechas(fecha):
    """
    Es una funcion que valida la entrada de la fecha
    Parametros:
    ------------
        fecha: string    
    Retorna:
    ------------
        fecha : string
            Guradar el valor de la fecha ingresada
    """
    #Inicialia la variable con verdadero
    val=True
    while val==True:
        #Ingreso de la fecha
        fecha=input(">> ")
        try:
            #Gurada la fecha
            fecha= datetime.datetime.strptime(fecha,'%Y-%m-%d')
            val=False
        except:
            val=True
            print("Dato invalido")
    #Retorna la fecha 
    return str(fecha)[:10]

def fechasNacimiento(fecha):
    """
    Valida la fecha de nacimiento la cual debe ser antes del dia presente
    Parametros:
    ------------
        Fecha: string    
    Retorna:
    ------------
        edad: int
        fecha: string
    """
    fecha= datetime.datetime.strptime("2024-1-1",'%Y-%m-%d')
    while fecha>=datetime.datetime.now() :
        fecha=fechas(fecha)
        try:
            inicio= time.time()
            #Validar la fecha con el string ingresado
            fecha= datetime.datetime.strptime(str(fecha)[:10],'%Y-%m-%d')
            
        except:
            print("Fecha invalida")
    #Calcula la edad de la persona
    edad = relativedelta(datetime.datetime.now(), fecha)
    #Retorna la Edad y la fecha de nacimiento
    fin= time.time()
    return(int(edad.years)), str(fecha)[:10], fin-inicio

def fechasCita(fecha):
    """
    Valida la fecha de la proxima cita la cual no debe ser fin de semana y feriados ecuatorianos
    Parametros:
    ------------
        Fecha: string    
    Retorna:
    ------------
        fecha: string
    """
    #Inicializar la fecha
    fecha= datetime.datetime.strptime("2000-1-1",'%Y-%m-%d')
    while fecha<datetime.datetime.now() :
        #Ingreso de fecha validada
        fecha=fechas(fecha)
        try:
            fecha= datetime.datetime.strptime(str(fecha)[:10],'%Y-%m-%d')
        except:
            print("Fecha invalida")
    #Retorna la fecha validada
    return str(fecha)[:10]



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

def menuServicios():
    """
    Muestra un menu con los servicios que ofrece el centro odontologico
    Parametros:
    ------------
        No contiene parametros
    
    Retorna:
    ------------
        opc:
    """
    opc=0
    val=False
    #Ingreso de al ciclo
    while val==False:
        #Muestra las opciones 
        print("Limpieza dental---------------------- 45$")
        print("Blanqueamiento dental---------------- 45$")
        print("Diseño de sonrisa-------------------- 250$")
        print("Exodoncia---------------------------- 40$")
        print("Endodoncia premolares---------------- 200$")
        print("Endodoncia molares------------------- 240$")
        print("Ortodoncia--------------------------- 40$")
        print("Prótesis dentales-------------------- 120$")
        print("Periodoncia-------------------------- 250$")
        print("Cirugía bucal------------------------ 250$")
        print("Protesis----------------------------- 350$")
        print("Implantes dentales------------------- 500$")
        print("Tratamiento de urgencias dentales---- 300$")
        #Escoge las opciones
        opc=validar(opc,"Ingrese la opcion: ")
        #Valida que sean las opciones necesarias 
        if (opc==45 or opc== 250 or opc==40 or opc==200 or opc==240 or opc==120 or opc==350 or opc==500  or opc==300 ):
            val=True
        else:
            val=False
    #retorna la opcion escogida
    return opc
def menu():
    """
    Muestra un menu con los servicios que ofrece el programa
    impieza dental, blanqueamiento dental, endodoncia, ortodoncia, prótesis dentales, periódica, cirugía bucal, implantes dentales y tratamiento de urgencias dentales.
    Parametros:
    ------------
        No contiene parametros
    
    Retorna:
    ------------
        opc:
    """
    #VCrear las variables a utilizar
    opc=0
    val=False
    #Ingreso al ciclo
    while val==False:
        #Mostras las opciones que tiene el sistema
        print("[1] Ingresar datos Personales")
        print("[2] Historia clinica")
        print("[3] Lista de pacientes")
        print("[4] Cita proxima")
        print("[5] Facturacion")
        print("[6] Lista de citas en una fecha")
        print("[7] Complejidad en tiempo")
        print("[8] complejidad en almacenamiento")
        print("[0] salir")
        #Valida el ingreso de numeros
        opc=validar(opc,"Ingrese la opcion: ")
        #Valores permitidos dentro del rango
        if (opc>=0 and opc<=8):
            val=True
        else:
            os.system ("cls") 
            print("Opcion inavlida")
            val=False
    #Retornar la opcion escogida
    return opc

def menuHistorial():
    """
    Muestra un menu para mostra historia clinica o registrar
    Parametros:
    ------------
        No contiene parametros
    
    Retorna:
    ------------
        opc:
    """
    #Creacion de variables
    opc=0
    val=False
    #Ingreso al ciclo
    while val==False:
        #Muestra las opciones
        print("[1] Registrar Historial clinico")
        print("[2] Mostrar historial clinico")
        #valida la opcion escogida
        opc=validar(opc,"Ingrese la opcion: ")
        if (opc==1 or opc==2 ):
            val=True
        else:
            os.system ("cls") 
            print("Opcion inavlida")
            val=False
    #retorna la opcion
    return opc
def menuCitas():
    opc=0
    val=False
    while val==False:
        print("[1] Registrar Cita")
        print("[2] Mostras citas de una fecha")
        opc=validar(opc,"Ingrese la opcion: ")
        if (opc==1 or opc==2 ):
            val=True
        else:
            os.system ("cls") 
            print("Opcion inavlida")
            val=False
    return opc
def leercorreo(correo):
    """
    Es una funcion, en la cual valida el ingreso de un correo
    Parametros:
    ------------
        correo: string    
    Retorna:
    ------------
        correo : string
            Guradar el valor del correo ingresado
    """
    #crea una variable booleana e inicializa con false (falso)
    num=0
    #Ciclo acabara al momento que el valor de con cambien  a true
    #crear una lista con el nombre ingresado
    lis=list(correo)
    #Ciclo para conocer el contenido de la lista
    for i in range(len(lis)):
        #Comparar si la lista contiene letras entre a y z
        if(lis[i].lower()==" " ):
            num+=1
        if lis[i]>='a' and lis[i]<='z' and lis[i]!='ñ' or lis[i]=="-" or   lis[i]=="_" or lis[i]>="0":
            #cambiar el valor de con a true
            con=False
        #si contiene numeros o caracteres especiales
        else:
            #cambiamos el valor a false
            con=True
    #retorna el nombre con la primera letra mayuscula
    if(correo.islower()==False):
        con=True
    #retorna un boleano
    return  con

def correoValido(correo):
    """
    Validar el ingreso del correo electronico
    Parametros:
    ------------
        correo: string    
    Retorna:
    ------------
        correo : string
            Guradar el valor del nombre ingresado
    """
    #VCreacion de variables
    correo="Jm"
    val=True
    #Valida el correo electronico
    while val==True:
        correo=input(">> ")
        inicio= time.time()
        if(correo.find("@")!=-1):
            if(correo[correo.find('@')+1:]=="gmail.com" or correo[correo.find('@')+1:]=="hotmail.com" or correo[correo.find('@')+1:]== "yahoo.es" or correo[correo.find('@')+1:]== "espe.edu.ec"):
                #Llamado a la funcion para leer correo
                val=leercorreo(correo[:correo.find('@')])
    #Retornar correo
    fin= time.time()
    return correo, fin-inicio

def cedulaValida(cedula):
    """
    Validar el ingreso de la cedula Ecuatorina
    Parametros:
    ------------
        correo: string    
    Retorna:
    ------------
        correo : string
            Guradar el valor del nombre ingresado
    """

    val=True
    while val==True:
        suma=0
        cedula=input(">> ")
        try:
            for i in range(len(cedula)-1):
                x= int(cedula[i])
                if i%2==0:
                    x=x*2
                    if x>9:
                        x=x-9
                suma=suma+x
            if suma%10 !=0:
                result=10-(suma%10)
            if int(cedula[-1])==result:
                val=False
            else:
                print("Incorrecto")
        except:
            val=True
            print("Invalido ")
    return cedula

def descuentos(valor):
    """
    Descuentos especiales 
    Parametros:
    ------------
            valor = opcion escogida
    Retorna:
    ------------
        suma: float
            Valor a cancelar
    """
    #Inicializa la variable en verdadero
    val=True
    #Inicializa la variable 
    suma=0
    while val==True:
        #Muestra lo servicio y retorna el valor
        opc=menuServicios()
        #Suma los valores
        inicio=time.time()
        suma=suma+opc
        #Ingresa la opcion de s para continuar con el ingreso de servicios
        res=input("Desea introducir otro servicio s\n salir cualquier letra ")
        #Compara y convierte la letra ingresada a minuscula
        if(res.lower()=='s'):
            #Cambia el  valor
            val=True
        else:
            #Cambia el valor y sale del programa
            val=False
    #Comparar el valor del parametro
    
    if(valor==1):
        fin=time.time()
        #retorna el total a pagar
        return suma, fin- inicio
    if (valor==2):
        fin=time.time()
        #Retorna con el 10 % de descuento
        suma= suma-(suma*0.1)
    return suma,fin-inicio


def menuDesuentos():
    """
    Una funcion con un menu para descuentos 
    Parametros:
    ------------
        No contiene valores
    Retorna:
    ------------
        opc : int
            Guarda la opcion
    """
    #Inicializa la variable
    opc=0
    #Inicializa la variable bollena para ingresar al ciclo
    val=False
    while val==False:
        #Primera opcion  
        print("[1] Normal")
        #Segunda opcion
        print("[2] Descuento a familiares")
        #Validar la entrada de enteros
        opc=validar(opc,"Ingrese la opcion: ")
        #Si es la opcion1 o 
        if (opc==1 or opc==2 ):
            #Cambia el valor a verdader
            val=True
        else:
            #Limpia la pantalla
            os.system ("cls") 
            #Mensajde de dato invalido
            print("Opcion invalida")
            #Cambio del valor de val
            val=False
    #Retorna la opcion escogida
    return opc


def familiar(lista):
    """
    Una funcion la cual valida si los familiares tienen un mismo apellido
    Parametros:
    ------------
        lista:List
    Retorna:
    ------------
        val : booleano

    """
    #iniciamos al valor bolleano
    val=False
    #Extraemos al apellido lo que contiene la lista en la posicion 0
    apellido=lista[0]
    #Extraemos al apellido lo que contiene la lista en la posicion 1
    apellido1=lista[1]
    #Comparamos si tienen subcadenas parecidas osea los apellidos
    if apellido1.find(apellido[:apellido.find(" ")]) != -1 or  apellido1.find(apellido[apellido.find( " ")+1:]) != -1:
        val =True
    else:
        val = False
    return val

def presentacion():
    print(Back.LIGHTCYAN_EX + Fore.GREEN )
    print("-----------------------ODONTOLOGY JEIM-------------------------            ")
    print(" _____                                          _____      __   __         ")
    print("|     |     |        __|__    |                   |  __  °|  |_|  |        ")
    print("|     |  ___| ___  __  |  __  |  __  __           | |__| ||       |        ")
    print("|_____| |___||___||  | | |__| | |__||__||__|    __| |__  ||       |        ")
    print("                                     __| __|                               ")
    print(">>Tu mejor sonrisa, nuestra mayor felicidad                                ")
    print(Back.RESET + Fore.RESET)

