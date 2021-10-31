def sismosPorPais(nombreArchivo):
    sismos = []
    Archivo = open(nombreArchivo,'r')

    for linea in Archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(';')
        linea = tuple(linea)
        sismos.append(linea)

    Archivo.close()
    Archivo2 = open("estados_eeuu.txt")
    estados = []

    for linea2 in Archivo2:
        linea2 = linea2.rstrip('\n')
        estados.append(linea2)
    Archivo2.close()
    paises = []

    for i in sismos:
        tiempo,latitud,longitud,profundidad,magnitud,lugar = i

        if lugar not in paises and lugar not in estados:
            paises.append(lugar)
    
    resultado = []
    for j in paises:
        eeuu = 0
        cont = 0

        for k in sismos:    
            tiempo,latitud,longitud,profundidad,magnitud,lugar = k  
            
            if lugar == j and float(magnitud) >=2:
                cont +=1
            
            elif lugar in estados and float(magnitud) >=2:
                eeuu += 1
        
        if cont >=1:
            resultado.append((j,cont))
    resultado.append(("EEUU",eeuu))
    resultado.sort(reverse=True,key = lambda x: x[1])
    return resultado

sismos = print(sismosPorPais('sismos.txt'))

def escribir(f,sismos):
    disponibles = []
    Archivo = open("mag"+str(f)+".txt","w")
    limite = f + 1
    f = float(f)
    for i in sismos:
        tiempo,latitud,longitud,profundidad,magnitud,lugar = i
        magnitud = float (i[-2])
        if float(magnitud) >f and float(magnitud) <limite:
            disponibles.append(i)
    disponibles.sort(reverse=False,key = lambda x: x[1])
    for j in range(3):
        a = disponibles[j][0].split("T")
        fecha = a[0]
        hora = a[1]
        Archivo.write("Fecha: "+str(fecha)+" Hora: "+str(hora) + " Lugar: "+str(disponibles[j][-1])+" Magnitud: "+str(disponibles[j][-2])+"\n")   
    Archivo.close()

def categorizarSismos(nombreArchivo):
    Archivo = open(nombreArchivo,'r')
    sismos = []
    categoriaMenor = 9999999
    categoriaMayor = 0

    for linea in Archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(';')
        sismos.append(linea)
    Archivo.close()

    for i in sismos:
        tiempo,latitud,longitud,profundidad,magnitud,lugar = i
        if float(magnitud)>2.0:
            escala = float(magnitud)
            comp = int(escala)
            if comp > categoriaMayor:
                categoriaMayor = comp
            elif comp < categoriaMenor:
                categoriaMenor = comp
    diferencia = categoriaMayor - categoriaMenor + 1
    for i in range(categoriaMenor,categoriaMayor+1):
        escribir(i,sismos)
    return diferencia

print(categorizarSismos("sismos.txt"))