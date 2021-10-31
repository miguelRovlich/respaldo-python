import random
a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))


def DIM_MATRIZ(FILAS, COLUMNAS):
    MATRIZ = []
    suma = 0
    suma2 = 0
    for FILA in range(0, FILAS):
        MATRIZ.append([])
        for COLUMNA in range(0, COLUMNAS):
            MATRIZ[FILA].append(random.uniform(1,100))
            suma2 += int(MATRIZ[FILA][COLUMNA])
        suma += int(MATRIZ[FILA][COLUMNA])
        print("Suma: ",suma)
    print("suma por filas: ",suma)
    promedio = suma2/COLUMNAS
    print("Promedio por columnas: ",promedio)
    return MATRIZ

if a >6 or a <3 or b >6 or b <3:
    print("Numeros Fuera de Rango") 
else:
    print(DIM_MATRIZ(a,b))
