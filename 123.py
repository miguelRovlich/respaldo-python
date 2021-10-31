
#esta funcion valida si un numero es primo
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    #si el resultado es 1 o 2 devuelve False o True respectivamente
    else:
      #si no, hay un ciclo donde se comprueban los divisores de un numero
      #si no tiene ningun divisor retorna true, si encuentra uno no es primo entonces retorna false
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
#un for va contando los numeros hasta N y los imprime si son primos
def nPrime(n):
  for i in range(1,n):
      if isPrime(i):
          print(i)
n = int(input("Ingrese un numero: ")) 
nPrime(n)
