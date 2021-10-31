

def generaArchivo(region,lista):
    nombre = region+".txt"
    Archivo = open(nombre,'w',encoding='utf-8')
    avistamientos = []
    mayor = 0
    segundo = 0
    tercero = 0
    textoMayor = ''
    textoMayor2 = ''
    textoMayor3 = ''

    for i in lista:
        if i[1] == region:
            avistamientos.append(i)

    for j in avistamientos:
        totales = int(j[2])
        ovnis = int(j[3])
        calculo = ovnis/totales
        porcentaje = calculo *100
        porcentaje = round(porcentaje,2)
        if porcentaje> mayor:
            segundo = mayor
            tercero = segundo
            mayor = porcentaje
            textoMayor2 = textoMayor
            textoMayor3 = textoMayor2
            textoMayor = j
        elif porcentaje> segundo and porcentaje<=mayor:
            tercero = segundo
            segundo = porcentaje
            textoMayor3 = textoMayor2
            textoMayor2 = j
        elif porcentaje>tercero and porcentaje<=segundo:
            tercero = porcentaje
            textoMayor3 = j
    if textoMayor2 == "" and textoMayor3 == "":
        fecha = textoMayor[0]
        fecha = fecha.split('-')
        ano = fecha[0]
        mes = fecha[1]
        Archivo.write('En el mes '+str(mes) + ' de '+str(ano)+" hubo "+str(mayor)+'% de avistamientos confirmados de un total de '+str(textoMayor[1])+"\n")
    elif textoMayor3 == '':
        fecha = textoMayor[0]
        fecha = fecha.split('-')
        ano = fecha[0]
        mes = fecha[1]
        Archivo.write('En el mes '+str(mes) + ' de '+str(ano)+" hubo "+str(mayor)+'% de avistamientos confirmados de un total de '+str(textoMayor[1])+"\n")


        fecha2 = textoMayor2[0]
        fecha2 = fecha2.split('-')
        ano2 = fecha2[0]
        mes2 = fecha2[1]
        Archivo.write('En el mes '+str(mes2)+ ' de '+str(ano2)+" hubo "+str(segundo)+'% de avistamientos confirmados de un total de '+str(textoMayor2[1])+"\n")
    else:
        fecha = textoMayor[0]
        fecha = fecha.split('-')
        ano = fecha[0]
        mes = fecha[1]
        Archivo.write('En el mes '+str(mes) + ' de '+str(ano)+" hubo "+str(mayor)+'% de avistamientos confirmados de un total de '+str(textoMayor[1])+"\n")

        fecha2 = textoMayor2[0]
        fecha2 = fecha2.split('-')
        ano2 = fecha2[0]
        mes2 = fecha2[1]
        Archivo.write('En el mes '+str(mes2)+ ' de '+str(ano2)+" hubo "+str(segundo)+'% de avistamientos confirmados de un total de '+str(textoMayor2[1])+"\n")

        fecha3 = textoMayor3[0]
        fecha3 = fecha3.split('-')
        ano3 = fecha3[0]
        mes3 = fecha3[1]
        Archivo.write('En el mes '+str(mes3)+ ' de '+str(ano3)+" hubo "+str(tercero)+'% de avistamientos confirmados de un total de '+str(textoMayor3[1])+"\n")

nombreArchivo = 'ovnis_mediano.csv'

def avistamientosPorRegion(nombreArchivo):
    Archivo = open(nombreArchivo,'r',encoding='utf-8')
    lista = []

    for linea in Archivo:
        dato = linea.split(';')
        lista.append(dato)
    
    lista.pop(0)
    regiones = []
    
    for i in lista:
        if i[1] not in regiones:
            regiones.append(i[1])
            
    
    for j in regiones:
        generaArchivo(j,lista)

    return len(regiones)
print(avistamientosPorRegion(nombreArchivo))

