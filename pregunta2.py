def ingresarTrabajadores(num):
    cont = 0
    lista = []
    while cont <num:
        nombre = input('ingrese nombre ')
        lista.append(nombre)
        cont = cont + 1
    return lista

def ingresarKilometros():
    #se asume una jornada de lunes a viernes
    lista = []
    for i in range(5):
        km = int(input('Ingrese kilometraje: '))
        lista.append(km)
    return lista
    
def sumarTotal(lista):
    acum = 0
    for i in lista:
        acum = acum + i
    return acum

def retornaIndice(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]    
    return mayor

nombreMayor = ''
kmMayor = 0

trabajadores = int(input("Ingrese cuantos trabajadores: "))

nombres = ingresarTrabajadores(trabajadores)

for i in nombres:
    km = ingresarKilometros()
    suma = sumarTotal(km)
    if suma > kmMayor:
        kmMayor = suma
        nombreMayor = i


print('El Trabajador con mas con mas KM es: ',nombreMayor)
print('Su kilometraje semanal fue: ',kmMayor)