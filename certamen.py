op = 0
arrid = []
exp = ['junior','senior','master']
arrexperiencia = []
arredad = []
arrorigen =[]
arrantiguedad = []
while op != 4:
    print('1) Registrar Carpintero')
    print('2) Eliminar Carpintero')
    print('3) Ficha Carpintero')
    print('4) Salir')
    print()
    op = int(input('Ingrese opcion: '))
    if op == 1:
        aap =input('Ingrese Id del carpintero (no ponga el @): ') 
        if len(aap)<2:
            aap =input('Ingrese Id del carpintero nuevamente: ') 
        else:    
            id = '@'+aap      
        experiencia = input('Ingrese Experiencia: ').lower()
        if experiencia not in exp:
            experiencia = input('Ingrese Experiencia nuevamente: ').lower()    
        try:
            edad = int(input('Ingrese edad: '))
            if edad <15 or edad>105:
                edad = int(input('Ingrese edad nuevamente: '))
        except:
            print('Edad es un numero')
        origen = input('Ingrese nacionalidad (c= Chileno/o: Otro)').upper()
        
        if origen != 'C' or origen != 'O':
            origen = input('Ingrese nacionalidad nuevamente (c= Chileno/o: Otro)').upper()
        try:
            antiguedad = int(input('Ingrese antiguedad: '))
            if antiguedad <2:
                antiguedad = int(input('Ingrese antiguedad Nuevamente: '))
        except:
            print("Antiguedad es un numero")    
        arrid.append(id)
        arrexperiencia.append(experiencia)
        arredad.append(edad)
        arrorigen.append(origen)
        arrantiguedad.append(antiguedad)
    elif op == 2:
        deleteUser = input('Ingrese Id: ')
        deleteId = '@'+deleteUser
        for i in range(len(arrid)):
            if deleteId == arrid[i]:
                arrid.remove(arrid[i])
                arrexperiencia.remove(arrexperiencia[i])
                arredad.remove(arredad[i])
                arrorigen.remove(arrorigen[i])
                arrantiguedad.remove(arrantiguedad[i])
                print('Borrado exitoso')
            else:
                print("No existe el usuario")
    elif op == 3:
        #no se solicita validar asi que asumire que los datos ingresados son correctos
        mayor = input('Ingrese Experiencia: ')
        for j in range(len(arrexperiencia)):
            if arrexperiencia[j] == mayor and mayor == 'junior':
                print(arrid[j])
                print(arrexperiencia[j])
                print(arredad[j])
                print(arrorigen[j])
                print(arrantiguedad[j])
                print()
            
        print('---------------------------')        
        for k in range(len(arrexperiencia)):
            if arrexperiencia[k] == mayor and mayor == 'senior':
                print(arrid[k])
                print(arrexperiencia[k])
                print(arredad[k])
                print(arrorigen[k])
                print(arrantiguedad[k])
        print('---------------------------')        
        for l in range(len(arrexperiencia)):
            if arrexperiencia[l] == mayor and mayor == 'master':
                print(arrid[l])
                print(arrexperiencia[l])
                print(arredad[l])
                print(arrorigen[l])
                print(arrantiguedad[l])
            
    elif op==4:
        print('Que te vaya muy bien...')
    else:
        print("Opcion no valida")




