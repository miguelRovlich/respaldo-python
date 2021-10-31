
def conversion_dolar(valor_dolar,dia,monto,cambio):
    while dia not in valor_dolar:
        dia -= 1
    else:
        if cambio == "clp":
            valor_hoy = valor_dolar[dia]
            valor_hoy = monto/valor_hoy
            return valor_hoy
        else:
            valor_hoy = valor_dolar[dia]
            valor_hoy = monto*valor_hoy
            return valor_hoy

valor_dolar = {
        1:775.14,
        2:767.10,
        3:768.36,
        6:766.53,
        7:770.33,
        8:777.94,
        9:787.51,
        10:791.28,
        13:789.91,
        14:784.26,
        15:783.25,
        16:781.85,
        20:780.59,
        21:788.05,
        22:785.10,
        23:785.03,
        24:787.24,
        27:788.98,
        28:795.48,
        29:798.63,
        30:803.59
    }
opcion = input("Desea convertir de peso a dolar?: (s/n)")
monto = int(input("Ingrese monto: "))
dia = int(input("Ingrese dia: "))
if opcion.lower() == 's':
    print(conversion_dolar(valor_dolar,dia,monto,'clp'))
else:
    print(conversion_dolar(valor_dolar,dia,monto,'usd'))

