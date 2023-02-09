"""
Grafo de las rutas para llegar al aeropuerto mariscal sucre desde Quito

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""

def grafo( inicio, objetivo, cost):
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
	#global cost
	#Nodos visitados cambiamos el estado a visitado al primer nodo
	nodosV[inicio] = True
	#Si el nodo inical es igual al objetivo se muestra costos del camino
	if inicio != objetivo:
		#Recorre los nodos del grafo
		for i in graph[inicio]:	
			#Si el nodo no se ha visitado
			if not nodosV[i]:
				#El costo aumenta en uno para mostar el costo del camino
				cost+=1
				#Utilizamos recursividad para enviar otro punto de inicio 
				grafo( i, objetivo,cost)
	else:
		#Muestra el costo del camino 
		print( " Costo : ", cost)
	#Decrementamos el costo ya que si regresa a un nivel anterior se debe decrementar los pasos o costo
	cost-=1
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
			while num<0 or num>14:
				#Ingreso del numero por el usuario 
				num=int(input(">> "))
				#coparamos el numero ingresado
				if num>=0 or num <=14:
					#cambiamos el valor de val
					val=False
		except:
			#Si existe algun error en el ingreso
			print("Valor invalido")
	#retornamos el valor del numero
	return num

#Funcion main
if __name__ == '__main__':
	# Nombres de los nodos
	nodos = ["Quito", "Cumbaya", "Tumbaco", "Puembo", "Pifo", "tababela", "aeropuerto"
	, "yaruqui", "quinche", "laVictoria", "guallabamba", "calderon", "llanoGrande", "yacoto", "comunaSAna"]
	# Grafo con listas de adyacencia
	graph= [[] for i in range(len(nodos))]
	cost=0
	# Índices de los nodos
	#Quito es el nodo 0
	quito = 0
	#Cumbaya es el nodo 1
	cumbaya = 1
	#Tumbaco es el nodo 2
	tumbaco = 2
	#Puembo es el nodo 3
	puembo=3
	#Pifo es el nodo 4
	pifo=4
	#Tababela es el nodo 5
	tababela=5
	#Aeropuerto es el nodo 6
	aeropuerto=6
	#Yaruquies el nodo 7
	yaruqui=7
	#Quinche es el nodo 8
	quinche=8
	#La Victoria es el nodo 9
	laVictoria=9
	#Guallabamba es el nodo 10
	guallabamba=10
	#Calderon es el nodo 11
	calderon=11
	#Llano Grande es el nodo 12
	llanoGrande=12
	#Yacoto es el nodo 13
	yacoto=13
	#Comuna Santa Ana es el nodo 14
	comunaSAna=14
	
	# Conexión entre Quito y Cumbaya
	graph[quito].append(cumbaya)
	graph[cumbaya].append(quito)

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

	# Conexión entre yaruqui y Quiinche
	graph[yaruqui].append(quinche)
	graph[quinche].append(yaruqui)

	# Conexión entre Quinche y La Victoria
	graph[quinche].append(laVictoria)
	graph[laVictoria].append(quinche)

	# Conexión entre La Victoria y Guallabamba
	graph[laVictoria].append(guallabamba)
	graph[guallabamba].append(laVictoria)

	# Conexión entre Guallabamba y calderon
	graph[guallabamba].append(calderon)
	graph[calderon].append(guallabamba)

	# Conexión entre Calderon y Llano grande
	graph[calderon].append(llanoGrande)
	graph[llanoGrande].append(calderon)

	# Conexión entre Llano grande y Quito
	graph[llanoGrande].append(quito)
	graph[quito].append(llanoGrande)

	# Conexión entre Calderon y Yacoto
	graph[calderon].append(yacoto)
	graph[yacoto].append(calderon)

	# Conexión entre Yacoto y Comuna Santa Anita
	graph[yacoto].append(comunaSAna)
	graph[comunaSAna].append(yacoto)

	# Conexión entre  Comuna Santa Anita y aeropuerto
	graph[comunaSAna].append(aeropuerto)
	graph[aeropuerto].append(comunaSAna)
	#Creamos una lista boolena con el tamaño de lista nodos, la cual estara con valores falsos 
	nodosV = [False for i in range(len(nodos))]	
	print("Quito=0 Cumbaya=1  Tumbaco =2  Puembo= 3 Pifo=4 tababela=5  aeropuerto=6\n yaruqui=7 quinche= 8 La Victoria=9 guallabamba=10 calderon=11 llanoGrande=12 yacoto=13 comunaSAna=14")
	print("Ingrese el inicio de la ruta")
	inicio=leer()
	print("Ingrese el fin de la ruta")
	objetivo=leer()
	#Llamado de la funcion con el punto de inicio en quito y el obejetivo
	grafo( inicio, objetivo, cost)

	
