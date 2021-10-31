cont = 0 
longitud = 1
total = 0
cincuenta = 0
cont50 = 0
while longitud != 0:
    longitud = int(input("Ingrese una longitud: "))
    if longitud >=50 and longitud <=70:
        cincuenta += longitud
        cont50 +=1
    total += longitud
    cont +=1
print("Cantidad de datos ingresados: ",cont)
print("Cantidad de barras entre 50 y 70 cm: ",cont50)
print("Promedio longitud: ",total/cont)

