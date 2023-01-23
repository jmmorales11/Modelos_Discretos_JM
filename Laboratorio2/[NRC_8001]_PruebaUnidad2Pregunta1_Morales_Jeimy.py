"""
Dada una cadena, extraiga todas las subcadenas únicas con su frecuencia.
Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
def contar(cadena):
    """
    Funcion contar las veces de la cadea
    Parametros:
    ------------
        cadena: string
    Retorna:
    ------------
        No retorna 
        
    """
    #Se van formando las subcadenas para ir contando las veces que esta contenida en la cadena
    for i in range(len(cadena)-1):
        for j in range(1, len(cadena)):
            print(cadena[i:j]," :",cadena.count(cadena[i:j]), end="  ")
            #Agrego la a la lista
            lista.append(cadena[:j]+" :"+str(cadena.count(cadena[:j])))

if __name__ == '__main__':
    #Ingreso de la cadena
    cadena=input("Ingrese la cadena: ")
    #Lista global
    lista=[]
    #Lista auxiliar
    Lista1=[]
    #llamado a la funcion
    contar(cadena)
    #Mostrar la lista no repetida
    for i in lista:
        if i not in Lista1:
            Lista1.append(i)
    print(Lista1)

