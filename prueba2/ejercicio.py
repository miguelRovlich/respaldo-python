import random


def dim_matriz(filas, columnas):
    """
    Función que crea una matriz
    """
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            x = random.uniform(1, 100)
            matriz[i].append(round(x, 1))
    return matriz

n = int(input("Introduce el número de filas: "))
m = int(input("Introduce el número de columnas: "))
nombre = input("Introduce el nombre del archivo: ")
print(dim_matriz(n, m))

Archivo = open(nombre+".txt", "w")
Archivo.write(str(dim_matriz(n, m)))
print(dim_matriz(n, m))
Archivo.close()