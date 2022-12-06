"""
Simon dice, es un juego tradicional, consiste en en grupo de jugadores minimo 2 y maximo 5 
los cuales deben ir acumulando puntos en 5 rondas, al final se muestra al jugador ganador con mas puntos realizados

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.1.2
"""
def simonDice():
    """
    Es un procedimiento que nos muestra en que ronda de juego estan los jugadores, asignar puntos al jugador el
    cual realizo el reto, y escoger el jugador con mayor puntos acumulados
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    #Declaracion de un contador ronda,R, el cual va sumar 1 por cad ronda
    R=1
    #Declaracion de la variable ganador,G , la cual va a guardar el maximo de puntos de un jugador
    G=0
    #Declaracion de los 5 jugadores 
    #Jugador A
    Ja=0
    #Jugador B
    Jb=0
    #Jugador C
    Jc=0
    #Jugador D
    Jd=0
    #Jugador E
    Je=0
    #Comienza las rondas de juego hasta que la ronda sea 5
    while R<=5:
        #Imprime la ronda en la que se encuentran los jugadores con las rondas maximas
        print("Ronda  ", R," de ",5)
        #Imprime el reto que debe realizar los participantes
        print("\n-----------\nSimon dice  ",reto())
        #En la variable jugador,la cual es una variable auxiliar donde se guarda el valor de retorno de la funcion escoger Jugador la cual es un letra
        jugador=escogerJugador()
        #Comparamos el jugador escogido con el jugador A
        if(jugador == 'a'or jugador == 'A'):
            #Si el jugador A realizo el reto se acumula un punto adicional a Ja
            Ja+=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador A realizo el reto tiene ",Ja," puntos")
        #Comparamos el jugador escogido con el jugador B
        elif (jugador=='b'or jugador == 'B'):
            #Si el jugador B realizo el reto se acumula un punto adicional a Jb
            Jb+=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador B realizo el reto tiene ",Jb," puntos")
        #Comparamos el jugador escogido con el jugador C
        elif (jugador=='c' or jugador == 'C'):
            #Si el jugador C realizo el reto se acumula un punto adicional a Jc
            Jc +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador C realizo el reto tiene ",Jc," puntos")
        #Comparamos el jugador escogido con el jugador D
        elif (jugador=='d'or jugador == 'D'):
            #Si el jugador D realizo el reto se acumula un punto adicional a Jd
            Jd+=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador D realizo el reto tiene ",Jd," puntos")
        #Comparamos el jugador escogido con el jugador E
        elif (jugador=='e' or jugador == 'E'):
            #Si el jugador E realizo el reto se acumula un punto adicional a Je
            Je +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador E realizo el reto tiene ",Je," puntos")
        R +=1
    #Compardamos si el jugador A es mayor al ganador
    if(Ja>G ):
        #En la variable ganador se guarda el valor del Jugador A
        G=Ja
    #Compardamos si el jugador B es mayor al ganador
    if(Jb>G):
        #En la variable ganador se guarda el valor del Jugador B
        G=Jb
    #Compardamos si el jugador C es mayor al ganador
    if(Jc>G):
        #En la variable ganador se guarda el valor del Jugador C
        G=Jc
    #Compardamos si el jugador D es mayor al ganador
    if(Jd>G):
        #En la variable ganador se guarda el valor del Jugador D
        G=Jd
    #Compardamos si el jugador E es mayor al ganador
    if (Je>G):
        #En la variable ganador se guarda el valor del Jugador E
        G=Je
    #Utilizamos el proceso ganadorJuego, para imprimir el ganador del juego
    ganadorJuego(G,Ja,Jb,Jc,Jd,Jd)

def reto():
    """
    Es una funcion la cual nos permite ingresar el reto que el jugador debe realizar
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        Reto : string
            valor que contiene el reto el cual debe realizar los jugadores

    """
    #Ingreso del reto el cual los jugadores deben realizar en la variable R
    Reto=input("Ingrese el reto que los jugadores deben realizar: ")
    #retornamos el reto
    return Reto


def escogerJugador():
    """
    Es una funcion la cual utiliza la variable global "cantidadJugadores", para utilizar el menu correspondiente
    con la cantidad de jugadores
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        Ju : string
            valor contiene el jugador que realizo primero el reto

    """
    #comparamos la variable global, cantidad de jugadores, con 2 para presentar el menu correspondiente a la cantidad de jugadores
    if(CJ==2):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        #ingresamos el jugador que realizo primero el reto
        Ju=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(Ju.lower()=='b' or Ju.lower()=='a'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador valido")
        else:
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
     #comparamos la variable global, cantidad de jugadores, con 3 para presentar el menu correspondiente a la cantidad de jugadores
    elif(CJ==3):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        #ingresamos el jugador que realizo primero el reto
        Ju=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(Ju.lower()=='c' or Ju.lower()=='b' or Ju.lower()=='a'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador valido")
        else:
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #comparamos la variable global, cantidad de jugadores, con 4 para presentar el menu correspondiente a la cantidad de jugadores
    elif(CJ==4):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        print("[d]  Jugador D")
        #ingresamos el jugador que realizo primero el reto
        Ju=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(Ju.lower()=='c' or Ju.lower()=='b' or Ju.lower()=='a'or Ju.lower()=='d'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador valido")
        else:
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #comparamos la variable global, cantidad de jugadores, con 5 para presentar el menu correspondiente a la cantidad de jugadores
    elif(CJ==5):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        print("[d]  Jugador D")
        print("[e]  Jugador E")
        #ingresamos el jugador que realizo primero el reto
        Ju=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(Ju.lower()=='c' or Ju.lower()=='b' or Ju.lower()=='a'or Ju.lower()=='d' or Ju.lower()=='e'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador valido")
        else:
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #Retornamos el jugador escogido
    return Ju

def ganadorJuego(G,Ja,Jb,Jc,Jd,Je ):
    """
    Es un proceso, el cual compara el valor maximo de puntos echos por un jugador con los puntos
    de cada jugador, para presentar al jugador ganador
    Parametros:
    ------------
        G : int 
            ganador valor que contiene el maximo de puntos echos por un jugador
        Ja : int
            Jugador A valor que contiene los puntso echos por el jugador A
        Jb : int
            Jugador B valor que contiene los puntso echos por el jugador B
        Jc : int
            Jugadir C valor que contiene los puntso echos por el jugador C
        Jd : int
            Jugador D valor que contiene los puntso echos por el jugador D
        Je : 
            Jugador E valor que contiene los puntso echos por el jugador E
    Retorna:
    ------------
        No retorna ningun valor
    """
    #La variable contador, acumula si elvalor del ganador es igual al jugador elacumulador suma mas 1
    #para saber si existe empate de jugadores
    cont=0
    print("\n----------------Felicidades---------------------")
    #Comparamos el valor del ganador con el valor del jugador A
    if(Ja==G ):
        #Si el valor del ganador es igual valor del jugador A se presenta el mensaje con lo puntos del jugador A
        print("El ganador es el jugador A  con ",Ja," Puntos" )
        #Adiciona mas uno si cumple la condicion
        cont+=1
    #Comparamos el valor del ganador con el valor del jugador B
    if(Jb==G):
        #Si el valor del ganador es igual valor del jugador B se presenta el mensaje con lo puntos del jugador B
        print("El ganador es el jugador B  con ",Jb," Puntos" )
        #Adiciona mas uno si cumple la condicion
        cont+=1
     #Comparamos el valor del ganador con el valor del jugador C
    if(Jc==G):
        #Si el valor del ganador es igual valor del jugador C se presenta el mensaje con lo puntos del jugador C
        print("El ganador es el jugador C  con ",Jc," Puntos" )
        #Adiciona mas uno si cumple la condicion
        cont+=1
    #Comparamos el valor del ganador con el valor del jugador D
    if(Jd==G):
        #Si el valor del ganador es igual valor del jugador D se presenta el mensaje con lo puntos del jugador D
        print("El ganador es el jugador D  con ",Jd," Puntos" )
        #Adiciona mas uno si cumple la condicion
        cont+=1
    #Comparamos el valor del ganador con el valor del jugador E  
    if (Je==G):
        #Si el valor del ganador es igual valor del jugador E se presenta el mensaje con lo puntos del jugador E
        print("El ganador es el jugador E  con ",Je," Puntos" )
        #Adiciona mas uno si cumple la condicion
        cont+=1
    #Compara el valor del contador,para saber si existe empate de jugadores o un solo ganador
    if(cont==1):
        #Imprimer que le juego a finalizado
        print(("************FIN DEL JUEGO*************"))
    #Si el contador es mas de uno 
    else:
        #Imprimer que existe empate entre los jugadores
        print("\tExiste empate con los jugadores")
        #Imprime el fin del juego
        print(("\t      FIN DEL JUEGO"))


def entero(valor):
    """
    Es un proceso, el cual compara el valor maximo de puntos echos por un jugador con los puntos
    de cada jugador, para presentar al jugador ganador
    Parametros:
    ------------
        valor : string
            Contiene el valor ingresado por el usuario 
    Retorna:
    ------------
        Retorna un booleano
    """
    #Comparamos el valor de ingreso del usuario, con los valores, 2, 3 ,4 y 5
    if(valor=='2' or valor=='3' or valor=='4' or valor=='5' ):
        #retornamos verdadero si cumple la condicion
        return True
    else:
        #retornamos falso si no cumplela condicon
        return False

    
if __name__ == '__main__':
    #Declaramos una variable global CJ "cantidad de jugadores"
    CJ=0
    #Comenzamos el juego
    print("\n<<<<<<<JUEGO TRADICIONAL SIMON DICE>>>>>>>\n")
    #Declaramos variable bool
    con=False
    #Presenta al usuario la cantidad de jugadores permitidos
    print("Jugadores permitidos de 2 a 5")
        #Mientras la variable con sea falsa el ingreso debe repetir
    while(con==False):
        #Ingreso de la cantidad de jugadores 
        CJ=input("Ingrese la cantidad de jugadores: ")
        #Guardamos el valor de retorno de la funcion entero()
        con=entero(CJ)
    #Convertimos la cantidad de jugadores al valor entero
    CJ=int(CJ)
    #llamado al proceso
    simonDice()

        
