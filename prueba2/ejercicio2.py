opcion = 0 
a = 0
b = 0


def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a / b
def raiz(a,b):
    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a ** (1/b)

while opcion !=7:
    print("1. Ingresar valores")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Raiz")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        a = int(input("Ingrese un valor: "))
        b = int(input("Ingrese otro valor: "))
    elif opcion == 2:
        print(suma(a, b))
    elif opcion == 3:
        print(resta(a, b))
    elif opcion == 4:
        print(multiplicacion(a, b))
    elif opcion == 5:
        print(division(a, b))
    elif opcion == 6:
        print(raiz(a, b))
    elif opcion == 7:
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")
        print("Intente de nuevo")
        print("")

