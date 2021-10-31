A=270
B=340
C=390
pago=0
total = 0
validos = ["A","B","C"]
precio=input("Elija Producto: ").upper()
if precio in validos:
    if precio == validos[0]:
        precio = A
    if precio == validos[1]:
        precio = B
    if precio == validos[2]:
        precio = C
while total < precio:
    pago = int(input("Ingrese monedas: "))
    if pago == 10:
        total = total + pago
    elif pago == 50:
        total = total + pago
    elif pago == 100:
        total = total + pago
    else:
        print("Valor invalido") 
    print(total)
vuelto = total - precio
if vuelto == 0:
    print("Pago justo.")
else:
    print("Su vuelto: ")
while vuelto > 0:
    if vuelto >=100:
        print("100")
        vuelto -=100
    elif vuelto >=50:
        print("50")
        vuelto -=50
    elif vuelto >=10:
        print("10")
        vuelto -=10