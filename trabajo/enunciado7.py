def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)



numero = int(input("Ingrese un numero: "))

if numero <10 or numero >15:
    print("Numero Invalido")
else:
    for i in range(numero):
        a = fib(i)
        print(a)

