def reverse(num):
    reverse=0
    while num >= 1:
         reverse=reverse*10+int(num%10)
         num=num/10
    return reverse


opcion =0

while opcion != 4:
    print('Opcion 1', 'Factorial')
    print('Opcion 2', 'Invertir numero')
    print('Opcion 3', 'Lista con nombres de personas')
    print('Opcion 4', 'Salir')
    print()
    opcion = int(input("Ingrese opcion: "))
    print()
    if opcion == 1:
        y = input("Ingrese un numero:")
        x = int(y)
        count = 1
        z = 1
        while z <= x:
            count = count * z
            z = z + 1
        print(count)
    elif opcion == 2:
        numero = int(input("Ingrese numero: "))
        
        print(reverse(numero))
    elif opcion == 3:
      listaNombres = []
      nombres = ''
      while nombres.upper() != 'X':
          print("(Si desea dejar de ingresar nombres ingrese X)")
          nombres = input("Ingrese nombre para agregar a la lista: ")
          if nombres.upper() != 'X':
            listaNombres.append(nombres)
      for i in listaNombres:
          print(i)
    elif opcion == 4:
      print("Fin del programa")
    else:
      pass
    
