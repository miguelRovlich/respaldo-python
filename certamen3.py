import random

n = random.randint(1,20)

estatura = []
peso = []
edad = []


def tamanoSombrero(estatura,peso):
    valor = peso/estatura
    valor = valor *2.9
    return valor
def tamanoSaco(estatura,peso,edad):
    valor = (estatura * peso)/288
    if edad >30:
        cont = 40
        while cont<=edad:
            valor = valor + 0.3175
            cont = cont + 10
    return valor
def tamanoCintura(peso,edad):
    valor = peso /5.7
    if edad >28:
        cont = 30
        while cont<=edad:
            valor = valor + 0.254
            cont = cont + 2
    return valor

for i in range(n):
    est = float(input('Ingrese estatura en pulgadas: '))
    pes = float(input('Ingrese peso en libras: '))
    eda = float(input('Ingrese edad: '))
    estatura.append(est)
    peso.append(pes)
    edad.append(eda)
    print()
    print('Tamaño del sombrero: ',tamanoSombrero(est,pes))
    print()
    print('Tamaño del saco: ',tamanoSaco(est,pes,eda))
    print()
    print('Tamaño de la cintura: ',tamanoCintura(pes,eda))