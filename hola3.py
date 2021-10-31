import random 

lista = []



def rellenarLista(n):
    
    lista = []
    for i in range(n):
        a = random.uniform(0,25)
        a = round(a,1)
        lista.append(a)
    return lista


def calculaMedia(results):
    m = sum(results) / len(results)
    return m
def calculaVarianza(results):
    m = sum(results) / len(results)
    var_res = sum((xi - m) ** 2 for xi in results) / len(results)
    return var_res

def escribir(lista):
    print("Longitud de los tornillos: ")
    for i in lista:
        print(i)
    print()
    print("Media: ")
    print(calculaMedia(lista))
    print()
    print("Varianza: ")
    print()
    print(calculaVarianza(lista))
opcion = 0

while opcion != 5:
    print("Opcion 1: Ingresar Medidas")
    print("Opcion 2: Calcular media")
    print("Opcion 3: Calcular varianza")
    print("Opcion 4: Imprimir")
    print("Opcion 5: salir")
    opcion = int(input('Ingrese opcion: '))

    if opcion == 1:
        n = int(input("Ingrese la cantidad de tornillos: "))
        if n <2:
            print("La cantidad de tornillos ingresados es muy baja")
        else:
            lista = rellenarLista(n)
            print(lista)
    elif opcion == 2:
        if len(lista)>2:
            print(calculaMedia(lista))
        else:
            print('Por favor genere la lista')
    elif opcion == 3:
        if len(lista)>2:
            print(calculaVarianza(lista))
        else:
            print('Por favor genere la lista')
    elif opcion == 4:
        
        if len(lista)>2:
            print(escribir(lista))
        else:
            print('Por favor genere la lista')
    elif opcion == 5:
        print("Fin del programa")
    else:
        print('Entrada invalida, por favor ingrese otra')
        opcion = int(input('Ingrese opcion: '))
