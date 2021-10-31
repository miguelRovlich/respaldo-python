mayor = 0
menor = 999999999999999999999999999999999999999999999
for i in range(4):
    d = int(input("Ingrese numero " + str(i+1)))
    if d > mayor:
        mayor = d
    if d < menor:
        menor = d

print("numero mayor: ",mayor)

print("numero menor: ",menor)