"""
Ingresar un nombre y saludar

Autores:
Jeimy Marley Morales Sosa

Verision:
VER.0.1
"""
def leer(nombre):
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
    #Ciclo acabara al momento que el valor de con cambien  a true
    while con==False:
        #Ingreso del nombre
        nombre=input("Ingrese su nombre  ")
        #crear una lista con el nombre ingresado
        lis=list(nombre)
        #Ciclo para conocer el contenido de la lista
        for i in range(len(lis)):
            #Comparar si la lista contiene letras entre a y z
            if lis[i].lower()>='a' and lis[i].lower()<='z':
                #cambiar el valor de con a true
                con=True
            #si contiene numeros o caracteres especiales
            else:
                #cambiamos el valor a false
                con=False
    #retorna el nombre con la primera letra mayuscula
    return nombre.lower().capitalize()

def saludo(nombre):
    """
    Es un proceso, en el cual saluda junto al nombre
    Parametros:
    ------------
        nombre: string    
    Retorna:
    ------------
        no retorna
    """
    #Muestra el saludo junto al nombre
    print("Hola ", nombre)

if __name__ == '__main__':
    #Crea una variable tipo string
    nombre=""
    #Ingreso del nombre con la funcion leer
    nombre=leer(nombre)
    #Llama al proceso saludo
    saludo(nombre)