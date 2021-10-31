#345654 polidivisible
numero = 1

def poliDivisible(numero):
    poli = False
    largo = str(numero)
    lista = list(largo)
    largo = len(largo)
    numero = int(numero)
    acumulador = 0
    if numero == 1:
        poli = True
    else:
        for i in lista:
            a = int(i)
            acumulador = acumulador + a
        if numero % largo == 0:
            poli = True
        else:
            poli = False
    return poli
esPoli = 0
noEsPoli = 0
while numero >0:
    numero = int(input("Ingrese un numero: "))
    poli = poliDivisible(numero)

    if poli:
        print(numero,' Es polidivisible')
        esPoli = esPoli + 1
    else:
        print(numero,' No es polidivisible')
        noEsPoli += 1
else:
    print('Polidivisibles: '+str(esPoli))
    print('No polidivisibles: ',noEsPoli)
    print('Fin del programa')