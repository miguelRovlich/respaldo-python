Lrut = []
Ledad = []
Lnombre = []
Lapellido = []
Ltelefono = []



opcion = 0

while opcion != 4:
    print('Opcion 1: Ingresar socios')
    print('Opcion 2: Buscar socio por rut')
    print('Opcion 3: Calcular promedio edades y mayores de 18')
    print('Opcion 4: Salir.')
    print()
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        rut = input('Ingrese rut: ')
        edad = int(input('Ingrese edad: '))
        nombre = input("Ingrese nombre: ")
        apellido =input("Ingrese apellido: ")
        telefono = int(input('Ingrese telefono: '))
        Lrut.append(rut)
        Lnombre.append(nombre)
        Ledad.append(edad)
        Lapellido.append(apellido)
        Ltelefono.append(telefono)
        print()
        print('Usuario registrado')
        print("")
        print("")         
    elif opcion == 2:
        rutB = input('Ingrese rut: ')
        if rutB not in Lrut:
            print("No existe ningun usuario con ese rut")
        else:
            pos = 0
            for i in range(len(Lrut)):
                if Lrut[i] == rutB:
                    pos = i
            print(Lrut[pos])
            print(Lnombre[pos])
            print(Lapellido[pos])
            print(Ledad[pos])
            print(Ltelefono[pos])
    elif opcion == 3:
        suma = 0
        cont = 0
        mayor = 0
        for i in Ledad:
            if i >18:
                mayor += 1
            suma += i
            cont += 1
        promedio = suma/cont
        print("Promedio de edad: ", promedio)
        print("Mayores de edad: ",mayor)
    elif opcion ==4:
        print("Fin del programa")
    else:
        print("Opcion invalida")
