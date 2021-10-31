import random

def paresAndTrios(lista,n):
    pares= 0
    posibleTrio = False
    trios= 0
    for i in range(0,len(lista)-1):    
        if lista[i] ==n and lista[i+1] ==n and lista[i-1] ==n:
            trios +=1
            i+=1
            posibleTrio = False
        elif lista[i] ==n and lista[i+1] ==n and not posibleTrio:
            posibleTrio = True
            pares +=1
    return [pares,trios]
    
def generarLista(m,inicio,fin):
    lista = []
    for i in range(m):
        numero = random.randint(inicio,fin)
        lista.append(numero)
    return lista

lista1 = [1,2,2,2,4,7,2,2,1,9,3,2,2]
print(lista1)
print(paresAndTrios(lista1,2))
print(generarLista(12,5,17))

def funcionAgregada():
    lista = generarLista(100,1,10)
    print(lista)
    pares = paresAndTrios(lista,6)
    return pares


print(funcionAgregada())