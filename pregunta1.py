def agregarActividades(actividades):
    agregar = input("Ingrese una actividad: ")
    actividades.append(agregar)
    print("Actividad Agregada con Exito")
    print()
    return actividades

def borrarActividades(actividades,actividad):
    for i in actividades:
        if actividad == i:
          actividades.pop(i)
    print("Actividad borrada con Exito")
    print()
    return actividades
 
def agregarActividadesRealizadas(actividades,realizadas):
    agregar = input("Ingrese una actividad: ")
    if agregar not in actividades:
        print("No existe esa actividad en el listado de actividades")
    else:
        for i in actividades:
          if i == agregar:
            realizadas.append(agregar)
            print("Actividad Realizada con Exito")
            print()
    return realizadas

def verActividades(actividades):
  if len(actividades) == 0:
     return 'No hay actividades'
  else:
      for i in actividades:
        print(i)
      print()

def escribir(lista):
    Archivo = open('actividades.txt','w')
    for i in range(len(lista)):
        Archivo.write(lista[i] + '\n')
    Archivo.close()

def crearCuenta(usuarios):
    nombre = input("Ingrese nombre: ")
    password = input('Ingrese contraseña: ')
    if nombre in usuarios: 
      print("El usuario ya existe")
    else:
      usuarios[nombre] = {password}
    return usuarios

def iniciarSesion(usuarios):
    nombre = input("Ingrese nombre: ")
    password = input('Ingrese contraseña: ')
    if nombre in usuarios and password in usuarios[nombre]: 
      print("Sesion Iniciada con exito")
    else:
        print("Usuario o contraseña incorrectas")
    
def leer():
    try:
      Archivo = open('actividades.txt','r')
      lista = []
      if Archivo == '':
        return False
      else:  
        for i in Archivo:
            dato = i.split('\n')
            valor = int(dato[0])
            lista.append(valor)
        return lista
    except:
      print("El archivo no existe")

def eliminarActividades(actividades):
    eliminar = input('Ingresa actividad a borrar:')
    actividades2 = []
    if len(actividades)  == 0:
        print("Listado de actividades vacio")
    else:
        for i in actividades:
            if str(i) != str(eliminar):
                actividades2.append(i)
        print("Borrado con Exito")
        return actividades2


def editarActividades(actividades,actividad):
    actividades2 = []
    if len(actividades) == 0:
        print('Listado Vacio')
    elif actividad not in actividades:
        print('No se encontro la actividad buscada')
    else:
        for i in actividades:
            if actividad == i:
              nuevoI = input("Ingrese Actividad Nueva: ")
              actividades2.append(nuevoI)
            else:
              actividades2.append(i)
        print("Actividad Editada exitosamente")
    return actividades2

    
usuarios = {}
realizadas = []
actividades = []

opcion = 0
while opcion != 11:
    print('Opcion 1: Leer Archivo de Actividades existente')
    print('Opcion 2: Escribir nuevo archivo de actividades')
    print('Opcion 3: Editar Actividad')
    print('Opcion 4: Eliminar Actividad')
    print('Opcion 5: Agregar Actividad')
    print('Opcion 6: Realizar Actividad') #marcarla como realizada al trasladarla a la lista de realizadas
    print('Opcion 7: Mostrar Listado Actividades')
    print('Opcion 8: Mostrar listado Actividades realizadas')
    print('Opcion 9: Registrar usuario')
    print('Opcion 10: Iniciar Sesion')
    print('Opcion 11: Salir')
    print('')
    print('')
    opcion = int(input('Ingrese opcion: '))
    print('')
    print('')

    if opcion == 1:
        lista = leer()
        if not lista:
          print("Archivo vacio")
          print()
        else:
          print('Lista de actividades creada correctamente')
          print()
    elif opcion == 2:
        escribir(actividades)
        print("Archivo de Actividades guardado correctamente")
    elif opcion == 3:
      editar = input("Ingrese Actividad que desea editar: ")
      actividades = editarActividades(actividades,editar)
    elif opcion == 4:
        actividades = eliminarActividades(actividades)
    elif opcion == 5:
        actividades = agregarActividades(actividades)
    elif opcion == 6:
        realizadas = agregarActividadesRealizadas(actividades,realizadas)
    elif opcion == 7:
      if len(actividades) == 0:
          print("Listado Vacio")
      else:
        print("Lista Actividades")
        print()
        print()
        print(verActividades(actividades))
    elif opcion == 8:

      if len(realizadas) == 0:
          print("Listado Vacio")
      else:
        print("Lista Actividades Realizadas")
        print()
        print()
        print(verActividades(realizadas))
    elif opcion == 9:
      crearCuenta(usuarios)
    elif opcion == 10:
      iniciarSesion(usuarios)
    elif opcion == 11:
      print("Fin del programa")
    else:
      print("Opcion invalida")