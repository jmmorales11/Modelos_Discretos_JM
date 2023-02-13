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
			while num<0 or num>7:
				#Ingreso del numero por el usuario 
				num=int(input(">> "))
				#coparamos el numero ingresado
				if num>=0 or num <=7:
					#cambiamos el valor de val
					val=False
		except:
			#Si existe algun error en el ingreso
			print("Valor invalido")
	#retornamos el valor del numero
	return num
def estrella():
    init()
    print("                    ",Back.BLUE,"PBus(1)",Back.RESET,"\n")
    print(" ",Back.BLUE ,"Coliseo(0)",Back.RESET,"                       ",Back.BLUE ,"Tienda(2)",Back.RESET,"           \n\n")
    print("                       ",Back.BLUE ,"Parque(3)",Back.RESET,"           ",Back.BLUE,"Panaderia(6)",Back.RESET,"\n")
    print("   ",Back.BLUE,"CSalud(4)",Back.RESET,"\n")
    print("                      ",Back.BLUE,"CComercial(5)",Back.RESET,"           ",Back.BLUE,"Floreria(7)",Back.RESET,"")
    
	
# main function
if __name__ == '__main__':
    nodos = ["ColiseO", "P Bus", "Tienda", "Parque", "Centro de salud", "Centro comercial", "Panaderia", "Floreria"]
    graph= [[] for i in range(len(nodos))]
    cost=0
    coliseo = 0
    pBus = 1
    tienda= 2
    parque=3
    cSalud=4
    cComercial=5
    panaderia=6
    floreria=7
    # Conexión entre Coliseo y parque
    graph[coliseo].append(parque)
    graph[parque].append(coliseo)

    # Conexión entre Coliseo y pBus
    graph[coliseo].append(pBus)
    graph[pBus].append(coliseo)

    # Conexión entre  parque y PBus
    graph[parque].append(pBus)
    graph[pBus].append(parque)  

    # Conexión entre  pBus y tienda
    graph[pBus].append(tienda)
    graph[tienda].append(pBus)

    # Conexión entre  parque y Centro de salud
    graph[parque].append(cSalud)
    graph[cSalud].append(parque)

    # Conexión entre  parque y panaderia
    graph[parque].append(panaderia)
    graph[panaderia].append(parque)

    # Conexión entre  parque y CComercial
    graph[parque].append(cComercial)
    graph[cComercial].append(parque)

    # Conexión entre  cSalud y CComercial
    graph[cSalud].append(cComercial)
    graph[cComercial].append(cSalud)

    # Conexión entre  panaderia y tienda
    graph[panaderia].append(tienda)
    graph[tienda].append(panaderia)

    # Conexión entre  panaderia y tienda
    graph[parque].append(floreria)
    graph[floreria].append(parque)

    #Creamos una lista boolena con el tamaño de lista nodos, la cual estara con valores falsos 
    nodosV = [False for i in range(len(nodos))]
    #creamos una lista para guardar los caminos visitados
    camino=[]
    estrella()
    print("Vertices Coliseo P Bus Tienda Parque Centro de salud Centro comercial Panaderia Floreria")
    print("Ingrese los vertices a conectar plos los vertices de la estrella")
    inicio=leer()
    objetivo=leer()
        #lamado de la funcion con el punto de inicio en quito y el obejetivo
    grafo( inicio, objetivo)
	