lista = [
[ "1", "2", "3"],
[ "4", "5", "6"],
[ "7", "8", "9"],
["10","11","12"],
["13","14","15"],
["16","17","18"],
["19","20","21"],
["22","23","24"],
["25","26","27"],
["28","29","30"],
["31","32","33"],
["34","35","36"],
["37","38","39"],
["40","41","42"],
]

def verAsientos(lista):
    a = 1
    for i in lista:
        #print(a,  end="")
        if a %2 == 0:
            print("     ",i)
        else:
            print(i,end="")
        a  += 1

def comprarAsiento(clientes,lista):
    rut = input("Ingrese RUT: ")
    nombre = input("Ingrese Nombre: ")
    telefono = input("Ingrese telefono: ")
    banco = input("Ingrese banco: ")
    valor = 0
    a = False
    asiento = int(input("Ingrese Asiento: "))
    if asiento <0 and asiento >43:
        print("El asiento no existe")
    elif asiento >0 and asiento <=30:
        valor = 78900
    elif asiento >30 and asiento <43:
        valor = 240000
    

    if banco.upper() == "BANCODUOC":
      valor = valor * 0.85
    datos = [rut,nombre,telefono,banco,valor,asiento]
    asiento = str(asiento)
    for i in range(len(lista)):
      for j in range(len(lista[i])):
        if lista[i][j] == asiento:
          lista[i][j] = "X"
          clientes.append(datos)

          print()
          a = True
    
    if a:
      print("El pasaje fue comprado correctamente")
    
      print()

      print("Valor del Pasaje: ",valor)
      print()
    else:
      print("El asiento se encuentra reservado")

      print()
    return (clientes,lista)




def anularPasaje(clientes,lista):
  asiento = int(input("Ingrese numero de asiento: "))
  a = asiento -1
  a = str(a)
  cont = 1
  if asiento <0 and asiento >43:
    print("El asiento no existe")
  else:
    for i in range(len(lista)):
      for j in range(len(lista[i])):
        if asiento == cont:
          print(asiento)
          lista[i][j] = str(asiento)
          print("Vuelo Anulado")
          print()
        cont += 1
  for i in clientes:
    if i[-1] == str(asiento):
      i = ''
  return clientes,lista

def modificarDatos(clientes):

  if len(clientes) == 0:
    print("Lista de clientes Vacia")
  else:
    rutVerificacion = input("Ingrese rut: ")
    asientoVerificacion = int(input("Ingrese asiento: "))


    for i in clientes:
        if i[-1] == asientoVerificacion and rutVerificacion == i[0]:
          nombreNuevo = input("Ingrese nuevo nombre: ")
          telefonoNuevo = input("Ingrese nuevo telefono: ")
          #[rut,nombre,telefono,banco,valor,asiento]
          i[1] = nombreNuevo
          i[2] = telefonoNuevo
          print(i)
          print("Datos actualizados")
          print()
        else:
          print("No se encontro ")
          print()

  return clientes

opcion = 0


clientes = []
while opcion != 5:
    print('Opcion 1', 'Ver asientos disponibles')
    print('Opcion 2', 'Comprar Asiento')
    print('Opcion 3', 'Anular Vuelo')
    print('Opcion 4', 'Modificar Datos Pasajero')
    print('Opcion 5', 'Salir')
    print()
    opcion = int(input("Ingrese opcion: "))
    print()
    if opcion == 1:
      verAsientos(lista)
      print()
    elif opcion ==2:
      clientes,lista = comprarAsiento(clientes,lista)
      print()
    elif opcion ==3:
      clientes,lista = anularPasaje(clientes,lista)
      print()
    elif opcion ==4:
      clientes = modificarDatos(clientes)
    elif opcion ==5:
      print("Fin del programa")
    else:
      pass
    



