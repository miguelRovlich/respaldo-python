import random


arreglo = []
for i in range(10):
    arreglo.append(random.randint(1,100))



numero = int(input("Ingrese numero a buscar: "))

if numero in arreglo:
    print(numero," si se encuentra en el arreglo")
else:
    print(numero," no se encuentra en el arreglo")
