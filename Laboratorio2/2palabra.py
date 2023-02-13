"""
Encuentre un punto de simetría de una cadena de caracteres
Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
import big_o
import time
def solucion(palabra):
    """
    Proceso que compara si existe una simetria alos dos lados de la cadena
    Parametros:
    ------------
        palabra : string
    Retorna:
    ------------
        no retorna ningun valor
        
    """
    num=0
    #Crea una cadena con la palabra hasta la posicion del valor medio
    cantes=palabra[:int(impar)]
    #Crea una cadena con la palabra desde la posicion del valor medio hasta el final de la cadena
    cdespues=palabra[int(impar)+1:]
    #Compara si dos cadenas son iguales cdespues inverte la cadena del final
    for i in range(len(palabra)):
        num+=1

    return num
    

if __name__ == '__main__':
    print("----------Mitad de la cadena y los lados sean iguales-------------")
    #Ingreso de la cadena de caracteres
    palabra=input("Ingrese una palabra :  ")
    #Tamaño de la cadena
    tam=len(palabra)
    #Posicion de la palabr del medio
    impar= tam/2
    #Si el tampaño es impar 
    if (tam % 2 !=0):
        #Llamado a la funcion para mostrar la letra
        print(solucion(palabra))
        
    else:
        #muestra mensaje de la palabra no es permitida por el tamaño 
        print("Palabra no permitida ")
    
    #Muestra la complejidad del programa
    nombre_ejemplo= lambda ejemplo:palabra
    best, otros= big_o.big_o(solucion,nombre_ejemplo,n_repeats=1) 
    print(best)
    