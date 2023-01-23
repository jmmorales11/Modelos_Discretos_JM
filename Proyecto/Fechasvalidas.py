import datetime
import calendar
from Opciones import fechas
import os
from memory_profiler import profile
def pascua(anno):
    d=(19*(anno%19)+24)%30
    e=(2*(anno%4)+4*(anno%7)+6*d+5)%7
    if d+e<10:
        dia_de_pascua=d+e+22
    else:
        dia_de_pascua=d+e-9
    if d+e<10:
        mes_de_pascua=3
    else:
        mes_de_pascua=4
    if dia_de_pascua==26 and mes_de_pascua==4:
        dia_de_pascua=19
    if dia_de_pascua==25 and mes_de_pascua==4 and d==28 and e==6 and (anno%19)>10:
        dia_de_pascua=18
    return str(int( (mes_de_pascua)))+"-"+str(int((dia_de_pascua)))

def semana(fecha):
    dia=calendar.day_name[fecha.weekday()]
    
    if dia=="Wednesday":
        fecha=fecha+datetime.timedelta(days=2)
        dia=calendar.day_name[fecha.weekday()]
    if dia=="Thursday":
        fecha=fecha+datetime.timedelta(days=1)
        dia=calendar.day_name[fecha.weekday()]
    if dia=="Saturday":
        fecha=fecha-datetime.timedelta(days=1)
        dia=calendar.day_name[fecha.weekday()]
    if dia=="Sunday":
        fecha=fecha+datetime.timedelta(days=1)
        dia=calendar.day_name[fecha.weekday()]
    if dia=="Tuesday":
        fecha=fecha-datetime.timedelta(days=1)
        dia=calendar.day_name[fecha.weekday()]
    return fecha
    
def verdia(dia):
    if dia=="Wednesday" or dia=="Thursday" or dia=="Saturday" or dia=="Sunday" or dia=="Tuesday":
        return True
    else: 
        return False


def feriado(annio):
    """
    Valida la fecha de la proxima cita la cual no debe ser fin de semana y feriados ecuatorianos
    Parametros:
    ------------
        annio: string    
    Retorna:
    ------------
        lista: list
    """
    lista=[]
    #Creando la fecha de primero de enero
    fecha= datetime.datetime.strptime(annio+"-1-1",'%Y-%m-%d')
    #Encontrar el dia
    dia=calendar.day_name[fecha.weekday()]
    #Verificar si el dia de feriado debe trasladarse
    if(verdia(dia)==True):
        fecha=semana(fecha)
    #Se agrega el feriado a la lista
    lista.append(str(fecha)[:10])
    #Se calcula el domingo de pascua para encontrar el feeriado de carnaval
    pas=pascua(int(str(fecha)[:4]))
    #Calcular primer y segundo dia de carnaval de carnavl
    carnaval=str(datetime.datetime.strptime(str(fecha)[:4]+"-"+pas,'%Y-%m-%d')-datetime.timedelta(days=48))[0:10]
    carnaval2=str(datetime.datetime.strptime(str(fecha)[:4]+"-"+pas,'%Y-%m-%d')-datetime.timedelta(days=47))[0:10]
    #Feriado de viernes santo
    vierneSanto=str(datetime.datetime.strptime(str(fecha)[:4]+"-"+pas,'%Y-%m-%d')-datetime.timedelta(days=2))[0:10]
    #Se agregan  los dos feriados de carnaval y el viernes santo
    lista.append(carnaval)
    lista.append(carnaval2)
    lista.append(vierneSanto)
    #Dia del trabajador
    fecha= datetime.datetime.strptime(annio+"-5-1",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #Primer Grito
    fecha= datetime.datetime.strptime(annio+"-8-10",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #Independencia de guayaquil 
    fecha= datetime.datetime.strptime(annio+"-10-9",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #Dia de los difunto
    fecha= datetime.datetime.strptime(annio+"-11-2",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #independecia de cuenca
    fecha= datetime.datetime.strptime(annio+"-11-3",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #Navidad 
    fecha= datetime.datetime.strptime(annio+"-12-25",'%Y-%m-%d')
    dia=calendar.day_name[fecha.weekday()]
    if(verdia(dia)==True):
        fecha=semana(fecha)
    lista.append(str(fecha)[:10])
    #Retorna la lista con los feriados del años
    return lista

