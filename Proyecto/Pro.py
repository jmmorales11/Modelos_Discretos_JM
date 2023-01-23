"""
Generar los servicios del centro odontológico
1. Nombres y apellidos fecha de nacimiento (No contenga números ni caracteres
especiales) menor de edad (Debe tener más 18)
2. Validar correo electrónico
3. Historia clínica
4. Lista de usuarios registrados
5. Ingreso de la cita próxima (día y hora) valida (feriados) registra cita del día
(turno)
6. Facturación
7. Descuento a familiares con el mismo apellido (10% de la facturación)
8. Lista de persona en una fecha determinada

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
#Importa la libreria para la conexion a mogno
import pymongo
#Importar la libreria para limpiar y pausar
import os
#Importar la libreria para calcular el tiempo
import time
import big_o
#Importar la funcion feriado del py Fechasvalidas
from Fechasvalidas import feriado
#Importar para calcular la memoria
from memory_profiler import profile
#Importar funciones propias
from Opciones import familiar,presentacion,leerNombre,menu,cedulaValida,fechasNacimiento,menuDesuentos, fechas, correoValido,leerCita,menuHistorial,fechasCita, menuCitas, descuentos
class persona(object):
    def __init__(self, cedula,nombre, apellido,nacimiento,correo) :
        """
        Constructor de la clase persona
        Parametros:
        ------------
            cedula: string
            nombre: string
            apellido:string
            nacimiento: string
            correo: string
        """
        #Asignar valores
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.nacimiento=nacimiento
        self.correo=correo

    def getCedula(self):
        """
        Funcion que retorna el valor de la cedula
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            cedula:string
        """
        #Retorna el valor de la cedula
        return self.cedula
    def getNombre(self):
        """
        Funcion que retorna el valor del nombre
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nombre:string
        """
        #Retorna el valor de la nombre
        return self.nombre
    def getApellido(self):
        """
        Funcion que retorna el valor del apellido
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            apellido:string
        """
        #Retorna el valor de la apellido
        return self.apellido
    def getNacimiento(self):
        """
        Funcion que retorna el valor del nacimiento
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nacimiento:string
        """
        #Retorna el valor de la nacimiento
        return self.nacimiento
    def getCorreo(self):
        """
        Funcion que retorna el valor del correo
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            correo:string
        """
        #Retorna el valor de la correo
        return self.correo


class personaMenor(object):
    def __init__(self, cedula,nombre, apellido,nacimiento,nombreR,apellidoR,nacimientoR,correo) :
        """
        Constructor de la clase persona
        Parametros:
        ------------
            cedula: string
            nombre: string
            apellido:string
            nacimiento: string
            nombreR : string
            apellidoR: String
            nacimientoR : string
            correo: string
        """
        #Asignar valores
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.nacimiento=nacimiento
        self.nombreR=nombreR
        self.apellidoR=apellidoR
        self.nacimientoR=nacimientoR
        self.correo=correo
    def getCedula(self):
        """
        Funcion que retorna el valor de la cedula
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            cedula:string
        """
        #Retorna el valor de la cedul
        return self.cedula
    def getNombre(self):
        """
        Funcion que retorna el valor del nombre
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nombre:string
        """
        #Retorna el valor de la nombre
        return self.nombre
    def getApellido(self):
        """
        Funcion que retorna el valor del apellido
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            apellido:string
        """
        #Retorna el valor de la apellido
        return self.apellido
    def getNacimiento(self):
        """
        Funcion que retorna el valor del nacimiento
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nacimiento:string
        """
        #Retorna el valor de la nacimiento
        return self.nacimiento
    def getNombreR(self):
        """
        Funcion que retorna el valor del nombreR
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nombreR:string
        """
        #Retorna el valor de la nombreR
        return self.nombreR
    def getApellidoR(self):
        """
        Funcion que retorna el valor del apellidoR
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            apellidoR:string
        """
        #Retorna el valor de la apellidoR
        return self.apellidoR
    def getNacimientoR(self):
        """
        Funcion que retorna el valor del nacimientoR
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            nacimientoR:string
        """
        #Retorna el valor de la nacimientoR
        return self.nacimientoR
    def getCorreo(self):
        """
        Funcion que retorna el valor del correo
        Parametros:
        ------------
            no tiene parametro
        
        Retorna:
        ------------
            correo:string
        """
        #Retorna el valor de la correo
        return self.correo

    

def ListaPacientes():
    """
    Extrae los pacientes registrados mayor de edad y menor de edad
    Parametros:
    ------------
        No contiene parametros    
    Retorna:
    ------------
        No retorna 
    """
    #Try except para conocer los errores
    inicio=time.time()
    try:
        #Muestra mensaje para los pacientes mayores de Edad
        print("-----------Pacientes mayores de edad-----------------")
        #Mostrar los documentos de la coleccion clien de la base de datos
        for documento in coleccion.find():
            #Mostrar los datos extraidos de la coleccion
            print(documento["cedula"]," ",documento["nombre"]," ",documento["apellido"])
        #Mostrar mensaje para  los pacientes menor de edad
        print("-----------Pacientes menores de edad-----------------")
        #Mostrar los datos de la coleccio1 la cual tiene datos de la coleccion de menores de edad
        for documento1 in coleccion1.find():
            #Mostrar los datos extraidos de la coleccion1
            print(documento1["cedula"]," ",documento1["nombre"]," ",documento1["apellido"])
    #La excepcion si se demora en recargar los datos de la base de datos 
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        #Mostrar la demora de la extraccion de datos
        print("Tiempo extendido "+errorTiempo)
    #Excepcion de algu tipo de coneccion
    except pymongo.errors.ConnectionFailure as errorConexion:
        #Mostrar la falla de conexion
        print("Fallo a conectar "+ errorConexion)
    fin=time.time()
    return fin-inicio


def craerHistoria(lis):
    """
    Insertar en la coleccion de historial
    Parametros:
    ------------
        lis: List
            Contiene la cedula he historial clinico 
    Retorna:
    ------------
        No retorna 
    """
    #Crea un documento con los campos de cedula e historia
    documento={"cedula":str(lis[0]),"historia":str(lis[1])}
    #Inserta en la coleccion de historia clinica
    coleccion2.insert_one(documento)

def craerCita(lis):
    """
    Insertar en la coleccion citas para conocer la proxima cita
    Parametros:
    ------------
        lis: List
            Contiene la cedula he historial clinico 
    Retorna:
    ------------
        No retorna 
    """
    inicio=time.time()
    #Crear un documento con los datos de la lista
    documento2={"cedula":str(lis[0]),"nombre":str(lis[1]),"apellido":str(lis[2]),"fCita":str(lis[3])}
    #Insertar el documento en la coleccion
    coleccion3.insert_one(documento2)
    fin=time.time()
    return fin-inicio

def craerFactura(lis):
    """
    Insertar en la coleccion la factura 
    Parametros:
    ------------
        lis: List
            Contiene los datos de la factura
    Retorna:
    ------------
        No retorna 
    """
    #Crear un documento con los datos de la lista
    documento={"cedula":str(lis[0]),"nombre":str(lis[1]),"apellido":str(lis[2]),"valor":str(lis[3])}
    #Insertar el documento en la coleccion
    coleccion4.insert_one(documento)

def craer(obj):
    """
    Insertar la persona mayor de edad
    Parametros:
    ------------
        obj= Object
            Contiene los datos de la persona mayor de edad
    Retorna:
    ------------
        No retorna 
    """
    #Crea un documentos con los datos del objeto
    documento={"cedula":obj.cedula,"nombre":obj.nombre,"apellido":obj.apellido,"fechaNa":obj.nacimiento,"correo":obj.correo}
    #Insertar el documento
    coleccion.insert_one(documento)

def craerRepre(obj):
    """
    Insertar la persona mayor de edad
    Parametros:
    ------------
        obj= Object
            Contiene los datos de la persona mayor de edad
    Retorna:
    ------------
        No retorna 
    """
    #Crear un documento para la persona menor de edad
    documento={"cedula":obj.cedula,"nombre":obj.nombre,"apellido":obj.apellido,"fechaNa":obj.nacimiento,"repreNombre":obj.nombreR,"repreApe":obj.apellidoR,"fechaNaR":obj.nacimientoR,"correo":obj.correo}
    #Insertar el documento en la colccion de menor de edad
    coleccion1.insert_one(documento)

def buscarHistoria(cedula):
    """
    Buscar las historias clinicas de un usuario
    Parametros:
    ------------
        obj= Object
            Contiene los datos de la persona mayor de edad
    Retorna:
    ------------
        No retorna 
    """
    inicio=time.time()
    #Creao un diccionario 
    objetBuscar={}
    #Guardar en el diccionario la cedula 
    objetBuscar["cedula"]=cedula
    #Mostrar la cedula a buscar
    print(cedula)
    try:
        #mostrar las historias clinicas de la colccion con el numero de cedula 
        for documento in coleccion2.find(objetBuscar):
            #MNostrar la historia clinica del paciente
            print("--",documento["historia"])
    #La excepcion si se demora en recargar los datos de la base de datos 
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        #Mostrar la demora de la extraccion de datos
        print("Tiempo extendido "+errorTiempo)
    #Excepcion de algu tipo de coneccion
    except pymongo.errors.ConnectionFailure as errorConexion:
        #Mostrar la falla de conexion
        print("Fallo a conectar "+ errorConexion)
    fin=time.time()
    return fin-inicio
   
 
def buscarCita(fecha):
    """
    Buscar las citas  de un dia en especifico
    Parametros:
    ------------
        obj= Object
            Contiene los datos de la persona mayor de edad
    Retorna:
    ------------
        No retorna 
    """
    #Creao un diccionario 
    inicio=time.time()
    objetBuscar={}
    objetBuscar["fCita"]=fecha
    print(fecha)
    try:
        #mostrar las historias clinicas de la colccion con el numero de cedula 
        for documento in coleccion3.find(objetBuscar):
            print(documento["cedula"]," ",documento["nombre"]," ",documento["apellido"])
    #La excepcion si se demora en recargar los datos de la base de datos 
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        #Mostrar la demora de la extraccion de datos
        print("Tiempo extendido "+errorTiempo)
    #Excepcion de algu tipo de coneccion
    except pymongo.errors.ConnectionFailure as errorConexion:
        #Mostrar la falla de conexion
        print("Fallo a conectar "+ errorConexion)
    fin=time.time()
    return fin-inicio

if __name__=="__main__":
    #Creamos los valores para conectar a nustra bases de datos 
    MONGO_HOST="localhost"
    MONGO_PUERTO="27017"
    MONGO_TIEMPO_FUERA=1000
    MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
    #Dar  el nombre de la base de datos
    MONGO_BASEDATOS="Dentista"
    #Dar valor a la coleccion para igresar y buscar documentos
    MONGO_COLECCION="clien"
    MONGO_COLECCION1="clienRepre"
    MONGO_COLECCION2="historiasClinicas"
    MONGO_COLECCION3="citas"
    MONGO_COLECCION4="facturas"
    #Coneccion a nuestra base de datos con los valores creados
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=cliente[MONGO_BASEDATOS]
    #La coneccion a cada una de las coleciones de nuestra base de datos
    coleccion=baseDatos[MONGO_COLECCION]
    coleccion1=baseDatos[MONGO_COLECCION1]
    coleccion2=baseDatos[MONGO_COLECCION2]
    coleccion3=baseDatos[MONGO_COLECCION3]
    coleccion4=baseDatos[MONGO_COLECCION4]
    #Creacion de las variables a utilizar en el programa
    ced="";nombre="";apellido="";fecha="";edad=0;nRepre="";ARepre="";fRepre="";naRepre="";edadRepre=0;correo="";opc=1
    #Mientras el programa sea diferente de cerp continuara
    while opc!=0:
        presentacion()
        #Llamado al menu principal la cual retorna un valor de opcion
        opc=menu()
        os.system("cls")
        #Menu dependiendo de las opciones del programa
        if (opc==1):
            print("Registrar nuevo usuario")
            #Muestra lo que debe ingresar el usuario la cedula
            print("Cedula")
            #Llamado de la funcion cedulaValida par validar el ingreso de la cedula y retona la misma
            ced=cedulaValida(ced)
            #Muestra lo que deb ingresar el usuario el nombre
            print("Nombres")
            #Llamdo de la funcion leerNombre la cual retorna el nombre
            nombre,tNombre=leerNombre(nombre)
            #Muestra lo que deb ingresar el usuario el apellido
            print("Apellidos")
            #Llamdo de la funcion leerNombre la cual retorna el apellido
            apellido,tNombre=leerNombre(apellido)
            #Muestra un mensaje del ingreso de la fecha
            print("Fecha de nacimiento AAAA-MM-DD")
            #Llamado de la funcion Fecha de nacimiento la cual retorna la edad y la fecha validad
            edad,fecha,tFecha= fechasNacimiento(fecha)
            #Muestra un mensaje de ingreso de correo
            print("Correo electronico")
            #Valida la entrada de correos electronicos y retorna lo mismo
            correo,tCorreo=correoValido(correo)
            #Si la variable edad es un valor menor a 18 solict el ingreso de un representante
            if(edad<18):
                #La edad del representante debe ser mayor a 18
                while edadRepre<18:
                    #Muestra un mensaje de solicitud de un representante mayor a 18 años
                    print("Necesita un representnte mayor a 18 años")
                    #Muestra lo que debe ingresar
                    print("Nombre")
                    #Valida el nombre del Representante
                    nRepre,tNombre=leerNombre(nombre)
                    #Muestra lo que debe ingresar
                    print("Apellido")
                    #Validar el apellido del representante
                    ARepre,tNombre=leerNombre(apellido)
                    #Ingreso de la fecha de nacimiento en el formato
                    print("Fecha de nacimiento AAAA-MM-DD")
                    #Llamado de la funcion fecha de Nacimiento y guardar el retorno de la funcion
                    edadRepre,fRepre, tFecha= fechasNacimiento(fRepre)
            #Muestra un mensaje de si quiere registrar al usuario
            print("Registrar a la persona s/n")
            #Inicia una variable con un valor para entrar al ciclo
            reg="a"
            #Mientras el ingreso de las letras sea diferente de s y n
            while reg.lower()!='s' or reg.lower()!='n':
                #Ingreso del valor de s o n
                reg=input(">>")
                #Si se preciona la s validad que tipo de persona es mayor o menor de edad
                if reg.lower()=='s':
                    #Ingreso de la persona menor de edad
                    if edad<18:
                        #Creacion del objeto
                        per=personaMenor(ced,nombre,apellido,fecha,nRepre,ARepre,fRepre,correo)
                        #Llamado a la funcion para crear representante
                        craerRepre(per)
                        #Muestra un mensaje de registrado
                        print("Registrado")
                        #Termina el ciclo
                        break
                    #Persona mayor de edad
                    else:
                        #Creacion del objeto
                        per=persona(ced,nombre,apellido,fecha,correo)
                        #Llamado a la funcion para crear representante
                        craer(per)
                        #Muestra un mensaje de registrado
                        print("Registrado")
                        #Termina el ciclo
                        break
                if reg.lower()=='n':
                    break
                #Muestra el mensaje de valor incorrecto
                print("valor incorrecto")
            os.system("cls")
        if ( opc==2):
            #Limpiar la pantalla
            #Llamado del meniHistorial
            opc1=menuHistorial()
            #La opc1 es igual a 1 se hace el registro del historial clinico
            if( opc1==1):
                #creacion de la lista
                lis=[]
                #Creacion de reg
                reg=""
                #Mostrar el registro 
                print("Registro")
                #Mostrar el ingreso de cedula
                print("Cedula")
                #Llamado de la funcion para validad el ingreo de la cedula
                ced=cedulaValida(ced)
                #inserta en la lista la cedula
                lis.append(ced)
                #Muestra lo que debe ingresar 
                print("Tratamiento realizado")
                #Leer el tratamiento
                reg=leerCita(reg)
                #Inserta en la lista el tratamiento
                lis.append(reg)
                #Llamado de la funcion para insertar los valores de la lista en la coleccion
                craerHistoria(lis)
                #Pausa del programa
                os.system("pause")
                #Limpiar la pantalla
                os.system("cls")
            if(opc1==2):
                #Muestra el historial de un cliente con su numero de cedula
                print("Historial clinico")
                print("Cedula")
                #Llamado de la validacion de la cedula 
                ced=cedulaValida(ced)
                #Busca las historias de la cedula 
                tHistorial=buscarHistoria(ced)
                numero_ejemplo= lambda ejemplo:ced
                #Calcular la complejidad
                #Muestra la complejidad 
                #Pausa al programa
                os.system("pause")
                #Limpia la pantalla
                os.system("cls")
        #Lista de pacientes es la opcion 3
        if ( opc==3):
            print("Lista de pacientes")
            #Muestra todos los pacientes registrados en el sistema
            tbuscar=ListaPacientes()

            #Pausa al programa
            os.system("pause")
            #Limpia la pantalla
            os.system("cls")
        if ( opc==4):
            #Inica una lista
            lis=[]
            val=True
            #Muestra el mensaje de registro
            print("Registro de cita")
            #Muestra lo que debe ingresar
            print("Cedula")
            #Valida la entrada de la cedula 
            ced=cedulaValida(ced)
            #Inserta en la lista
            lis.append(ced)
            print("Nombre")
            nombre,tNombre=leerNombre(nombre)
            #Muestra lo que deb ingresar el usuario el apellido
            lis.append(nombre)
            print("Apellidos")
            #Llamdo de la funcion leerNombre la cual retorna el apellido
            apellido,tNombre=leerNombre(apellido)
            lis.append(apellido)
            #Ingreso de la fecha en un formato
            print("Fecha de la proxima cita AAAA-MM-DD")
            #Ingreso de la fecha
            while val==True:
                fecha=fechasCita(fecha)
                if fecha in feriado(fecha[:4]):
                    print("Feriado")
                    val=True
                else: val=False
            #Insertar la fecha en la lista
            lis.append(fecha) 
            #Insertar en la coleccion los datos de la lista
            tCProxima=craerCita(lis)
            #Pausa en el programa
            os.system("pause")
            #Limpia la pantalla
            os.system("cls")
        if ( opc==5):

            #Mostra la facturacion
            print("Facturacion")
            #Menu de descuentos 
            valor=menuDesuentos()
            lista1=[]
            lis1=[]
            print("Cedula")
            #Valida la entrada de la cedula 
            ced=cedulaValida(ced)
            lis1.append(ced)
            print("Nombre")
            nombre,tNombre=leerNombre(nombre)
            lis1.append(nombre)
            #Muestra lo que deb ingresar el usuario el apellido
            print("Apellidos")
            apellido,tNombre=leerNombre(apellido)
            lista1.append(apellido)
            lis1.append(apellido)
            #Llamdo de la funcion leerNombre la cual retorna el apellido
            if valor==2:
                print("Apellidos del familiar")
                ARepre,tNombre=leerNombre(ARepre)
                lista1.append(ARepre)
                if (familiar(lista1)==True):
                    print("Aplica al descuento familiar del 10%")
                else: 
                    print("No aplica al descuento familiar")
                    valo=1
            #Mostrar el valor a pagar de la factura
            os.system("cls")
            des,tDescuento=descuentos(valor)
            lis1.append(str(des))
            print(des," $")
            
            craerFactura(lis1)
            lista_ejemplo= lambda ejemplo:lis1
            #Calcular la complejidad
            tFactura, otros= big_o.big_o(craerFactura,lista_ejemplo) 
            #Pausar el programa
            os.system("pause")
            #Limpiar la pantalla
            os.system("cls")
        #Mostrar la cita de una fecha
        if ( opc==6):
            #Mostrar un mensaje 
            print("Citas en una fecha")
            print("Ingreso de la fecha a buscar")
            #Validar la fecha
            fecha=fechas(fecha)
            #Buscar la fecha
            tCitas=buscarCita(fecha)
            #Pausar el programa
            os.system("pause")
            #Limpiar la pantalla
            os.system("cls")
        if (opc==7):
            #Mostrar cla complejidad de cada funcion 
            try:
                print("Funcion leer nombre         >>time: ",format(tNombre,'.1E'))
                print("Funcion fecha de nacimiento >>time: ",format(tFecha,'.1E'))
                print("Funcion correo              >>time: ",format(tCorreo,'.1E'))
                print("Funcion historial           >>time: ", format(tHistorial,'.1E'))
                print("Lista de usuarios           >>time: ",format(tbuscar,'.1E'))
                print("Cita proxima                >>time: ",format(tCProxima,'.1E') )
                print("Descuento                   >>time: ",format(tDescuento,'.1E') )
                print("Factura                     >>time: ",format(tDescuento,'.1E') )
                print("Cita en una fecha           >>time: ",format(tDescuento,'.1E') )
            except:
                #Si un tiempo falta calcular manda la excepcion 
                print("Falta calcular un tiempo")

            os.system("pause")
            os.system("cls")
        if (opc==8):
            #Mostramos el contenido de un archivo txt
            os.system("pause")
            os.system("cls")
    cliente.close()