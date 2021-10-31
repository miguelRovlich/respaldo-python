def menor_distancia(trayectos):
    distanciaMenor = 9999999999999999999999999999999999999999999999
    suma = 0
    for i in range(len(trayectos)):
        for j in range(len(trayectos[0])):
            suma = suma + trayectos[i][j]
        if suma < distanciaMenor:
            distanciaMenor = suma
    return suma

# escribe tu código aquí
def mayor_costo_promedio(costos):
    mayor = 0
    promediosFilas = []
    for fila in range(len(costos)):
        prom = 0
        for columna in range(len(costos[0])):
            prom = prom + costos[fila][columna]
            prom = prom / len(costos[0])
            if prom > mayor:
                mayor = prom
            promediosFilas.append(prom)
    promediosColumnas = []
    for columna in range(len(costos[0])):
        prom = 0
        for fila in range(len(costos)):
            prom = prom + costos[fila][columna]
            prom = prom / len(costos)
            if prom > mayor:
                mayor = prom
            promediosColumnas.append(round(prom,2))
    return mayor
    
# escribe tu código aquí
def eliminar_servicio(conectividad, supermercado, proveedor):
    pass
# escribe tu código aquí
# programa principal
menor_trayecto, proveedor = menor_distancia(trayectos)
print(f'La menor cantidad de km recorridos es de {menor_trayecto} y la realiza el proveedor {proveedor}.')
mayor_costo_prom, proveedor = mayor_costo_promedio(costos)
print(f'El mayor costo promedio generado es de {mayor_costo_prom} u.m y lo realiza el proveedor {proveedor}.')
# Ejemplo … Cancelar el servicio de abastecimiento que realiza el proveedorP4 al
# supermercado S3.
def imprimir_conectividad(new_conectividad):
    print('La nueva matriz de conectividad es:')
    for i in range(len(new_conectividad)):
        print(new_conectividad[i])
        nueva_conectividad = eliminar_servicio(conectividad,'S3','P4')
        imprimir_conectividad(nueva_conectividad)
