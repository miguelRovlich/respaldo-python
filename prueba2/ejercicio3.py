Archivo = open("VtasBertica.txt", "r")

diccionario = {}
menor = 999999999
mayores = []

for linea in Archivo:
    linea = linea.strip()
    linea = linea.split("%")
    idArticulo = linea[0]
    nombre = linea[1]
    unidadesVendidas = linea[2]
    montoVendido = linea[3]
    if idArticulo not in diccionario:
        diccionario[idArticulo] = [nombre, int(unidadesVendidas), int(montoVendido)]


#ordenar diccionario por monto vendido de mayor a menor
for key, value in sorted(diccionario.items(), key=lambda item: item[1][2]):
    if value[2] < menor:
        menor = value[2]
    else:
        mayores.append(value)

print(mayores)

#invertir lista 
mayores.reverse()
print(mayores)

#calcular promedio de ventas
suma = 0
for i in mayores:
    suma += i[2]


promedio = suma / len(mayores)

print("Promedio de ventas",promedio)

Archivo2 = open("Top5.txt", "w")
print(mayores)
for i in mayores:
    Archivo2.write(i[0] + "%" + str(i[1]) + "%" + str(i[2]) + "\n")