"""
Grafo de las rutas para llegar al aeropuerto mariscal sucre desde Quito

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
from colorama import Back, init
import networkx as nx
import matplotlib.pyplot as plt
import os
def grafo( inicio, objetivo):
    """
    Esta funcion nos muestras lo caminos disponibles para llegar al objetivo desde un inicio 
    Parametros
    -----------
        inicio: int 
			Contiene el punto inicla par comezar a budcar el camino 
		objetivo : int
			Contien el objetivo ara encontrar el camino mas corto 
    Returns:
        No contiene valores de retorno
    """
    global cost
            #Nodos visitados cambiamos el estado a visitado al primer nodo
    nodosV[inicio] = True
            #Almaceno cada camino desde el inicio hasta el objetivo
    camino.append(inicio)
            #Si el nodo inical es igual al objetivo se muestra costos del camino
    if inicio != objetivo:
                #Recorre los nodos del grafo
        for i in graph[inicio]:	
			#Si el nodo no se ha visitado
            if not nodosV[i]:
				#El costo aumenta en uno para mostar el costo del camino
                cost+=1
				#Utilizamos recursividad para enviar otro punto de inicio 
                grafo( i, objetivo)
    else:
		#Muestra el costo del camino 
        print( "Camino:  ",camino," Costo : ", cost)
	#Decrementamos el costo ya que si regresa a un nivel anterior se debe decrementar los pasos o costo
    cost-=1
    #Eliminamos el ultimo elemento de la lista del camino para evitar que el mismo camino se recorra varias veces 
    camino.pop()
	#Cambiomos el valor de nodosV de visitado a no
    nodosV[inicio] = False


def leer():
	"""
    La funcion permite el ingreso del numero entre 0 y 14 que son la cantidad de nodos
    Parametros
    -----------
        No contiene parametros
    Returns:
        num: contiene el valor escogido 
    """
	#Inicia la variable val tipo boolena con true (verdadero)
	val=True
	#Inica la variable num con menos uno para ingresar al bucle
	num=-1
	#El cicle termina cuando la variable val sea falsa
	while val==True:
		#Para saltar de algun error
		try:
			#Cilo repetira hasta que ingrese un numero valido
			while num<0 or num>19:
				#Ingreso del numero por el usuario 
				num=int(input(">> "))
				#coparamos el numero ingresado
				if num>=0 or num <=19:
					#cambiamos el valor de val
					val=False
		except:
			#Si existe algun error en el ingreso
			print("Valor invalido")
	#retornamos el valor del numero
	return num
def gragoDefinido(opc):
    """
    Conectar el grafo automaticamente o conectarlo manualmente
    Parametros
    -----------
        opc: int 
            Guarda la opcion para relizar el proceso
    Returns:
        no retorna 
    """
    #Compara la opcion con 1 para realizar la coneccion automatica
    if opc==1:

        # Conexión entre Quito y Miravalle
        graph[quito].append(miravalle)
        graph[miravalle].append(quito)

        # Conexión entre  Miravalle y cumbaya
        graph[miravalle].append(cumbaya)
        graph[cumbaya].append(miravalle)

        # Conexión entre Cumbaya y Tumbaco
        graph[cumbaya].append(tumbaco)
        graph[tumbaco].append(cumbaya)
            
        # Conexión entre Tumbaco y Puembo
        graph[tumbaco].append(puembo)
        graph[puembo].append(tumbaco)

        # Conexión entre Puembo y Pifo
        graph[puembo].append(pifo)
        graph[pifo].append(puembo)

        # Conexión entre Pifo y Tababela
        graph[pifo].append(tababela)
        graph[tababela].append(pifo)

        # Conexión entre  tababela y aeropuerto
        graph[tababela].append(aeropuerto)
        graph[aeropuerto].append(tababela)

        # Conexión entre tababela y yaruqui
        graph[tababela].append(yaruqui)
        graph[yaruqui].append(tababela)

        # Conexión entre  yaruqui y checa
        graph[yaruqui].append(checa)
        graph[checa].append(yaruqui)

        # Conexión entre checa y Quiinche
        graph[checa].append(quinche)
        graph[quinche].append(checa)

        # Conexión entre Quinche y La Victoria
        graph[quinche].append(laVictoria)
        graph[laVictoria].append(quinche)

        # Conexión entre La Victoria y Bello Horizonte
        graph[laVictoria].append(belloHorizonte)
        graph[belloHorizonte].append(laVictoria)

        # Conexión entre Bello Horizonte y Guayllabamba
        graph[belloHorizonte].append(guallabamba)
        graph[guallabamba].append(belloHorizonte)

        # Conexión entre Guallabamba y San Miguel del comun
        graph[guallabamba].append(sanMiguel)
        graph[sanMiguel].append(guallabamba)

        # Conexión entre  San Miguel del comun y calderon
        graph[sanMiguel].append(calderon)
        graph[calderon].append(sanMiguel)
        
        # Conexión entre Calderon y Llano grande
        graph[calderon].append(llanoGrande)
        graph[llanoGrande].append(calderon)

        # Conexión entre Llano grande y Quito
        graph[llanoGrande].append(quito)
        graph[quito].append(llanoGrande)

        # Conexión entre Calderon y carapungo
        graph[calderon].append(carapungo)
        graph[carapungo].append(calderon)

        # Conexión entre Carapungo y Oyacoto
        graph[carapungo].append(oyacoto)
        graph[oyacoto].append(carapungo)

        # Conexión entre Oyacoto y Comuna Santa Anita
        graph[oyacoto].append(comunaSAna)
        graph[comunaSAna].append(oyacoto)

        # Conexión entre  Comuna Santa Anita y aeropuerto
        graph[comunaSAna].append(aeropuerto)
        graph[aeropuerto].append(comunaSAna)
        
        ruta()
    #Si se desea conectr manualmente 
    else:
        #Crea la variable para ingresar al puble
        val=True
        while val==True:
            #Muestra todos los puntos disponible
            print("Quito=0 Miravale= 1 Cumbaya=2  Tumbaco =3  Puembo= 4 Pifo=5 Tababela=6 \n Aeropuerto=7 Yaruqui=8 Checah=9 Quinche= 10 La Victoria=11 Bello Horizonte=12 Guallabamba=13\n San Miguel=14 Calderon=15 Llano Grande=16 Carapungo =17 Oyacoto=18 comunaSAna=19")
            print("Ingrese el punto A concetar")
            #Ingreso del primer puto
            puntoA=leer()
            #Ingreso del segundo punto
            print("Ingrese el punto B concetar")
            puntoB=leer()
            # Conexión entre  puntoA y PuntoB
            graph[puntoA].append(puntoB)
            graph[puntoB].append(puntoA)
            #Mostrar la conexion del grafo
            print(graph)
            #Mensaje para salir o no del programa
            print("Desea seguir conectando s o salir n")
            #Ingreso para salir del proceso
            salida=salir()
            #Si desea salir n 
            if(salida=="n"):
                #Limpia la pantalla
                os.system ("cls")
                #Cambia el valor de val 
                val=False
            

def salir():
    """
    La funcion permite el ingreso de las letras s o n 
    Parametros
    -----------
        No contiene parametros
    Returns:
        num: contiene el valor escogido 
    """
    #Inicializar la variable salida 
    salida="r"
    #Ingreso al ciclo
    while salida!="s" and salida!="n":
        #Ingreso por el usuario
        salida=input(">>  ")
        #Transformar a minuscula
        salida=salida.lower()
    #Retornar la salida
    return salida        

def ruta():
    """
    El proceso nos grafica los puntos 
    Parametros
    -----------
        No contiene parametros
    Returns:
        No retorna
    """
	#Motsramos cada punto con un color azul para mejor visibilidad 
    init()
    print("                ",Back.BLUE,"0",Back.RESET,"   ",Back.BLUE,"16",Back.RESET)
    print("            ",Back.BLUE,"1",Back.RESET,"            ",Back.BLUE,"15",Back.RESET)
    print("       ",Back.BLUE,"2",Back.RESET,"             ",Back.BLUE,"17",Back.RESET,"   ",Back.BLUE,"14",Back.RESET)
    print("   ",Back.BLUE,"3",Back.RESET,"              ",Back.BLUE,"18",Back.RESET,"           ",Back.BLUE,"13",Back.RESET,"")
    print("   ",Back.BLUE,"4",Back.RESET,"          ",Back.BLUE,"19",Back.RESET,"               ",Back.BLUE,"12",Back.RESET)
    print("       ",Back.BLUE,"5",Back.RESET,"   ",Back.BLUE,"7",Back.RESET,"              ",Back.BLUE,"11",Back.RESET)
    print("           ",Back.BLUE,"6",Back.RESET,"            ",Back.BLUE,"10",Back.RESET)
    print("                ",Back.BLUE,"8",Back.RESET,"   ",Back.BLUE,"9",Back.RESET)

#Funcion main
if __name__ == '__main__':

    # Nombres de los nodos
    nodos = ["Quito","Miravalle", "Cumbaya", "Tumbaco", "Puembo", "Pifo", "tababela", "aeropuerto", "yaruqui", "Checa","quinche", "laVictoria", "Bello horizonte","guallabamba","San miguel del comun", "calderon", "llanoGrande", "Carapungo","Oyacoto", "comunaSAna"]
	# Grafo con listas de adyacencia
    graph= [[] for i in range(len(nodos))]
    cost=0
	# Índices de los nodos
	#Quito es el nodo 0
    quito = 0
    #Miravalle es el nodo 1
    miravalle=1
    #Cumbaya es el nodo 2
    cumbaya = 2
	#Tumbaco es el nodo 3
    tumbaco = 3
	#Puembo es el nodo 4
    puembo=4
	#Pifo es el nodo 5
    pifo=5
    #Tababela es el nodo 6
    tababela=6
	#Aeropuerto es el nodo 7
    aeropuerto=7
	#Yaruqui el nodo 8
    yaruqui=8
    #Checa el nodo 9
    checa=9
	#Quinche es el nodo 10
    quinche=10
	#La Victoria es el nodo 11
    laVictoria=11
    #Bello horizonte es el nodo 12
    belloHorizonte=12
	#Guallabamba es el nodo 13
    guallabamba=13
	#San Miguel del comun es el nodo 14 
    sanMiguel=14
    #Calderon es el nodo 15
    calderon=15
	#Llano Grande es el nodo 16
    llanoGrande=16
    #carapungo es el nodo 17
    carapungo=17
    #Oyacoto es el nodo 18
    oyacoto=18
	#Comuna Santa Ana es el nodo 19
    comunaSAna=19
    #Inicalizar la variable val para ingresar al cilo
    val=True
    #Mostrar las opciones para el grafo
    print("Grafo listo-------------1\nGrafo personalizado-----2")
    print("Ingrese ")
    #Leer el valor del grafo
    gra=leer()
    #Enviar la opcion a la funcion
    gragoDefinido(gra)
    while val==True:
        #Lista para los caminos
        camino=[]
        #Creamos una lista boolena con el tamaño de lista nodos, la cual estara con valores falsos 
        nodosV = [False for i in range(len(nodos))]	
        #Mostramos los puntos disponibles
        print("Quito=0 Miravale= 1 Cumbaya=2  Tumbaco =3  Puembo= 4 Pifo=5 Tababela=6 \nAeropuerto=7 Yaruqui=8 Checah=9 Quinche= 10 La Victoria=11 Bello Horizonte=12 Guallabamba=13\nSan Miguel=14 Calderon=15 Llano Grande=16 Carapungo =17 Oyacoto=18 comunaSAna=19")
        #Ingreso de la ruta 
        print("Ingrese el inicio de la ruta")
        inicio=leer()
        #Ingreso del fin de la ruta
        print("Ingrese el fin de la ruta")
        objetivo=leer()
        #Llamado de la funcion con el punto de inicio en quito y el obejetivo
        grafo( inicio, objetivo)
        #Pregunta al usuario si desea continuar en el programa
        print("Desea  seguir en el programa s salir y n continuar")
        #Leer la salida
        salida=salir()
        #Si la salida es igual a s el programa termina
        if(salida=="s"):
            #Cambio de val para salir del cilo
            val=False