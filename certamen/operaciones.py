numero = int(input("Ingrese un numero"))

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  



esPrimo = True
esPar = False
if numero <5 or numero >100:
    print("Numero Invalido")
else:
    esPrimo = isPrime(numero)
    if numero%2 == 0:
        esPar = True


if esPrimo:
    print(numero,' Es un numero primo')
else:
    print(numero,' Es un numero compuesto')

if esPar:
    print(numero,' Es un numero par')
else:
    print(numero,' Es un numero impar')
