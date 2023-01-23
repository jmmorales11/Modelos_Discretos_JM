import os
def pascua():
    anno = float (input ('Ingresa el valor de anno: '))
    d=(19*(anno%19)+24)%30
    e=(2*(anno%4)+4*(anno%7)+6*d+5)%7
    if d+e<10:
        dia_de_pascua=d+e+22
    else:
        dia_de_pascua=d+e-9
    if d+e<10:
        mes_de_pascua=3
        print ('Marzo')
    else:
        mes_de_pascua=4
        print ('Abril')
    if dia_de_pascua==26 and mes_de_pascua==4:
        dia_de_pascua=19
    if dia_de_pascua==25 and mes_de_pascua==4 and d==28 and e==6 and (anno%19)>10:
        dia_de_pascua=18
    print ('Valor de d: ' + repr (d))
    print ('Valor de dia de pascua: ' + repr (dia_de_pascua))
    print ('Valor de e: ' + repr (e))
    print ('Valor de mes de pascua: ' + repr (mes_de_pascua))
    print ()
    os.system ('pause')