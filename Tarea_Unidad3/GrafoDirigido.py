from colorama import Back, init
import networkx as nx
import matplotlib.pyplot as plt
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
	if inicio == objetivo:
		#Muestra el costo del camino 
		print(camino, " Costo : ", cost)
	else:
		#Recorre los nodos del grafo
		for i in graph[inicio]:
			#Si el nodo no se ha visitado
			if not nodosV[i]:
				#El costo aumenta en uno para mostar el costo del camino
				cost+=1
				#Utilizamos recursividad para enviar otro punto de inicio 
				grafo( i, objetivo)
	#Eliminamos el ultimo elemento de la lista del camino para evitar que el mismo camino se recorra varias veces 
	camino.pop()
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
			while num<0 or num>4:
				#Ingreso del numero por el usuario 
				num=int(input(">> "))
				#coparamos el numero ingresado
				if num>=0 or num <=4:
					#cambiamos el valor de val
					val=False
		except:
			#Si existe algun error en el ingreso
			print("Valor invalido")
	#retornamos el valor del numero
	return num
def estrella():
	"""
    El proceso nos grafica los puntos 
    Parametros
    -----------
        No contiene parametros
    Returns:
        No retorna
    """
	init()
	#Motsramos cada punto con un color rojo para mejor visibilidad 
	print("                    ",Back.RED ,"A(0)",Back.RESET,"\n")
	print("      ",Back.RED ,"E(4)",Back.RESET,"                       ",Back.RED ,"B(1)",Back.RESET,"           \n\n")
	print("            ",Back.RED ,"D(3)",Back.RESET,"           ",Back.RED ,"C(2)",Back.RESET,"")


	
# main function
if __name__ == '__main__':
    # Nombres de los nodos
	nodos = ["A", "B", "C", "D", "E"]
	# Grafo con listas de adyacencia
	graph= [[] for i in range(len(nodos))]
	cost=0
	# Índices de los nodos
	#Vertice A de una estrella
	A = 0
	#Vertice  B de una estrella
	B = 1
	#Vertice  C de una estrella
	C = 2
	#Vertice  D de una estrella
	D=3
	#Vertice  E de una estrella
	E=4
	# Conexión entre el vertice A  y C de una estrella
	graph[A].append(C)
	# Conexión entre el vertice C  y E de una estrella
	graph[C].append(E)
	# Conexión entre el vertice E  y B de una estrella
	graph[E].append(B)
	# Conexión entre el vertice B  y D de una estrella
	graph[B].append(D)
	# Conexión entre el vertice D  y A de una estrella
	graph[D].append(A)
	#Creamos una lista boolena con el tamaño de lista nodos, la cual estara con valores falsos 
	nodosV = [False for i in range(len(nodos))]
	#creamos una lista para guardar los caminos visitados
	camino=[]
	estrella()
	print("Vertices A=0, B=1 , C=2, D=3, E=4")
	print("Ingrese los vertices a conectar plos los vertices de la estrella")
	inicio=leer()
	objetivo=leer()
	#lamado de la funcion con el punto de inicio en quito y el obejetivo
	grafo( inicio, objetivo)
	