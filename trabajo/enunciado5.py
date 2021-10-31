a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))

def comparar(a,b):
    if a>b:
      return 1
    elif a<b:
      return -1
    else:
        return 0

print(comparar(a,b))
