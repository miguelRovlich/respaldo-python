import random;
nombre1 = input("Ingrese nombre 1: ")
nombre2 = input("Ingrese nombre 2: ")
numeroSorpresa = random.randint(1111,9999)
numero1 = 0
numero2 = 0
strNumeroSorpresa = str(numeroSorpresa)
ronda = 1
rondas1 = 0
rondas2 = 0
win1 = 0
win2 = 0
while win1==0 or win2 ==0:
    cont1 = 0
    cont2 = 0
    print("ronda ",ronda,":")
    print("Ingrese numero de 4 digitos,",nombre1, ": ")
    numero1 = int(input())
    comp1 = str(numero1)
    a1 = 0
    a2 = 0

    for i in range(len(comp1)):
        if comp1[i] == strNumeroSorpresa[i]:
            cont1 +=1
    if cont1 == 4:
        win1 = 1
        a1+=1
        break
    print("Ha logrado acertar a ",cont1," valores.")
    print()
    print("Ingrese numero de 4 digitos,",nombre2, ": ")
    numero2 = int(input())
    comp2 = str(numero2)

    for j in range(len(comp2)):
        if comp2[j] == strNumeroSorpresa[j]:
            cont2=1
    if cont2 == 4:
        win2 += 1
        a2+=1
        break
    print("Ha logrado acertar a ",cont2," valores.")
    print()
    if cont1 > cont2:
        print("La ronda ",ronda," la gano",nombre1," en ",ronda," intentos")
        rondas1 +=1
        print()
    elif cont1 < cont2:
        rondas2 +=1
        print("La ronda ",ronda," la gano",nombre1," en ",ronda," intentos")
        print()
    if rondas2 - rondas1 == 3:
        win2 = 1
        break
    elif rondas1 - rondas2 ==3:
        win1 = 1
        break
    ronda +=1
    print(nombre1," lleva ",rondas1,", ",nombre2," lleva ",rondas2)
    print()
if cont1 == 4:
    print(nombre1," Es el ganador",' con un promedio de ',cont1/rondas1)
elif cont2 == 4:
    print(nombre2," Es el ganador",' con un promedio de ',cont2/rondas2)
elif rondas1 - rondas2 ==3:
    print(nombre1," Es el ganador",' con un promedio de ',cont1/rondas1)
elif rondas2 -rondas1 ==3:
    print(nombre2," Es el ganador",' con un promedio de ',cont2/rondas2)
