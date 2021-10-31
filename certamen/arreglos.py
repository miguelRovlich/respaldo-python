import random


lista = [[],[],[]]


for i in lista:
    for j in range(3):
        i.append(random.randint(1,100))


cont = 0
print("Elementos Diagonal Arreglo: ")
for l in range(0,3):
    print(lista[l][l])






print("Arreglo Bidimensional: ")
print(lista)




unidimensional = []
for i in lista:
    for j in range(3):
        unidimensional.append(i[j])


print("Arreglo Unidimensional: ")
print(unidimensional)


print("Arreglo Unidimensional ordenado: ")

for recorrido in range(1,len(unidimensional)):
    for posicion in range(len(unidimensional)-recorrido):
        if unidimensional[posicion] >unidimensional[posicion+1]:
            temp = unidimensional[posicion]
            unidimensional[posicion] = unidimensional[posicion+1]
            unidimensional[posicion+1] = temp

print(unidimensional)