op = 0
usuario = []
contraseña = []
while op != 4:
   print('1) Inicio Sesion')
   print('2) Registrar Usuario')
   print('3) Eliminar Usuario')
   print('4) Salir')
   print()
   op = int(input('Ingrese opcion: '))
   if op == 1:
      username = input('Ingrese Usuario: ')
      password = input('Ingrese Contraseña: ')
      if username in usuario:
         if password in contraseña:
            print('Inicio de Sesion Correcto')
      else:
         print('Credenciales erroneas')
   elif op == 2:
      usuario1 = input('Ingrese usuario: ')
      contraseña1 = input('Ingrese contraseña: ')
      if usuario1 not in usuario:
         usuario.append(usuario1)
         contraseña.append(contraseña1)
         print("Registro exitoso")
         print()
      else:
         print('Usuario ya registrado')
         print()
      #funcion 2
   elif op == 3:
      deleteUser = input('Ingrese Usuario: ')
      deletePassword = input('Ingrese Contraseña: ')
      if deleteUser in usuario:
         usuario.remove(deleteUser)
         contraseña.remove(deletePassword)
         print('Borrado exitoso')
      else:
         print("No existe el usuario")
      #funcion 3
   elif op==4:
      print('Fin del programa')
   else:
      print("Opcion no valida")