opcion = ''
entradaSocio = 0
entradaGeneral = 0

def calcular(numero,tipo):
    if tipo == 2:
        total = 8500 * numero
    elif tipo == 1:
        total = 6800 * numero
    else:
        error = "Error, tipo de entrada invalido"
        return error
    return total

while opcion != 'N':
    entradas = int(input("ingrese cantidad de entradas: "))
    tipo = int(input("Ingrese tipo de entrada (1.Socio/2.General) :"))
    if tipo == 1:
        total = calcular(entradas,tipo)
        entradaSocio = entradaSocio + entradas
    elif tipo == 2:
        total = calcular(entradas,tipo)
        entradaGeneral = entradaGeneral + entradas
    else:
        print("Error de tipo")
    print("Valor total entradas: ",total)
    print("Entradas vendidas a socios: ",entradaSocio)
    print("Entradas vendidas a publico general: ",entradaGeneral)
    print()
    opcion = input("Desea seguir vendiendo entradas? (Y/N): ")
print("fin del programa")