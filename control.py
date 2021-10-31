def listFunction(list1,list2):
    #comparo el largo de cada lista, si son iguales se imprime que son iguales
    if len(list1) == len(list2):
        print('Las listas tienen el mismo largo')
    else:
        print('Las listas no tienen el mismo largo')
    
    lista11 = []
    lista22 = []
    #recorro toda la lista y si el indice es mayor a 1 para evitar los valores del indice 0 y 1 
    #el for es en rango del largo porque necesito que el indice sea numerico
    for i in range(len(list1)):
        if i >1:
            lista11.append(list1[i])
    
    print(lista11)
    #reduzco el rango en 2 y asi quedan fuera los 2 utlimos numeros de la lista
    resultado = len(list2) - 2
    for j in range(resultado):
            lista22.append(list2[j])
    print(lista22)


    listaNueva = []
    #recorro toda la lista, multiplico por 25 el numero y lo añado a la lista
    for k in list1:
        res = k*25
        listaNueva.append(res)
    print(listaNueva)


    #calcular promedios
    acum1 = 0
    acum2 = 0
    
    #acumumlo todos los valores en las variables de acumulacion y luego las divido por el largo de la lista
    for l in list1:
        acum1 = acum1 + l
    
    for m in list2:
        acum2 = acum2 + m
    
    print("promedio lista 1")
    print(acum1/len(list1))
    print()
    print("promedio lista 2")
    print(acum2/len(list2))

    #guardo los numeros mayores y menores en sus respectivas variables, luego recorro las listas y voy comparando y asignando el numero mayor a quien corresponda
    numeroMayor = 0
    listaMayor = 0
    
    numeroMenor = 99999999999999999999999999999999999999999999999999999999999999999
    listaMenor = 0

    for o in list1:
        if o > numeroMayor:
            numeroMayor = o
            listaMayor = 1

        if o < numeroMenor:
            numeroMenor = o
            listaMenor = 1
    
    for p in list2:
        if p > numeroMayor:
            numeroMayor = o
            listaMayor = 2

        if p < numeroMenor:
            numeroMenor = o
            listaMenor = 2

    print('La lista con el numeor mas alto es ',listaMayor)
    print('La lista con el numeor mas bajo es ',listaMenor)    






a = [12,2,56,75,8,13,33]
b = [15,36,85,64,11,4,23]
listFunction(a,b)

