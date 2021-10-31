def abrirArchivo(nombreArchivo):
    Archivo = open(nombreArchivo+'.txt','r')
    return Archivo
nombreArchivo = 'file'
Archivo = abrirArchivo(nombreArchivo)
matriz = []
for i in Archivo:
    i = i.rstrip('\n')
    i = i.split()
    matriz.append(i)

def leer_filas(lista):
    datos = []
    duplicados = []
    duplicadosTotal = []
    for i in lista:
        for j in i:
            if j not in datos:
                datos.append(j)
            else:
                duplicados.append(j)
                duplicadosTotal.append(j)
        datos = []
        duplicados = []
    if len(duplicadosTotal) ==0:
        print("No se encontraron duplicados en las filas")
    else:
        print("se encontraron ",len(duplicadosTotal)," numeros duplicados en las filas") 

def leer_columnas(lista):
    datos = []
    duplicados = []
    duplicadosTotal = []    
    columnas = [[],[],[],[],[],[],[],[],[]]
    for i in lista:
        columnas[0].append(i[0])
        columnas[1].append(i[1])
        columnas[2].append(i[2])
        columnas[3].append(i[3])
        columnas[4].append(i[4])
        columnas[5].append(i[5])
        columnas[6].append(i[6])
        columnas[7].append(i[7])
        columnas[8].append(i[8])
    for j in columnas:
        for k in j:
            if k not in datos:
                datos.append(k)
            else:
                duplicados.append(k)
                duplicadosTotal.append(k)
        datos = []
        duplicados = []
    if len(duplicadosTotal) ==0:
        print("No se encontraron duplicados en las columnas")
    else:
        print("se encontraron ",len(duplicadosTotal)," numeros duplicados en las columnas")     

def leer_cajas(lista):
    matriz1 =[]
    for i in range(3):
        for j in range(3):
            matriz1.append(lista[i][j])
    matriz2 =[]   
    for i in range(3):
        for j in range(3,6):
            matriz2.append(lista[i][j])
    matriz3 =[]   
    for i in range(3):
        for j in range(6,9):
            matriz3.append(lista[i][j])
    matriz4 =[]
    for i in range(3,6):
        for j in range(3):
            matriz4.append(lista[i][j])
    matriz5 =[]   
    for i in range(3,6):
        for j in range(3,6):
            matriz5.append(lista[i][j])
    matriz6 =[]   
    for i in range(3,6):
        for j in range(6,9):
            matriz6.append(lista[i][j])
    matriz7 =[]
    for i in range(3):
        for j in range(3):
            matriz7.append(lista[i][j])
    matriz8 =[]   
    for i in range(3):
        for j in range(3,6):
            matriz8.append(lista[i][j])
    matriz9 =[]   
    for i in range(3):
        for j in range(6,9):
            matriz9.append(lista[i][j])
    matrizMaestra =[matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9]
    for i in matrizMaestra:    
        datos = []
        duplicados = []
        duplicadosTotal = []    
        for k in i:
            if k not in datos:
                datos.append(k)
            else:
                duplicados.append(k)
                duplicadosTotal.append(k)
        datos = []
        duplicados = []
    
    if len(duplicadosTotal) ==0:
        print("No se encontraron duplicados en las cajas")
    else:
        print("se encontraron ",len(duplicadosTotal)," numeros duplicados en las cajas")     



leer_filas(matriz)
leer_columnas(matriz)
leer_cajas(matriz)