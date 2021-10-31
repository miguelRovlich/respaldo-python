

def areaCirculo(radio):
    radio2 = radio*radio

    pi = 3,141592


    area = pi * radio2
    return area



opcion = 0
while opcion != 3:
    print("Opcion 1: Calcular area de un circulo")
    print("Opcion 2: Calcular perimetro de un cuadrado")
    print("Opcion 3: Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion ==1:
        radio = int(input("Ingrese el radio del Circulo"))
        print(areaCirculo(radio))
    elif opcion ==2:
      lado = int(input("Ingrese el largo de un lado"))
      print(lado*4)
    elif opcion ==3:
      print("Fin del programa")
    else:
        print("Opcion Invalida")
