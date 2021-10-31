def obtener_info_pedido(pedidos,idProd):
    item = []
    for i in pedidos:
        if i[0] == idProd:
            item = i
    return item

def pedidos_por_fecha(pedidos,dd,mm,aa):
    item = []
    for i in pedidos:
        if i[-1][0] == aa and i[-1][1] == mm and i[-1][2] == dd:
            item.append(i[0])
    return item

def resumen_pedidos_por_fecha(pedidos, productos,dd,mm,aa):
    item = []
    lista = pedidos_por_fecha(pedidos,dd,mm,aa)
    itemNuevo = []
    for i in productos:
        if i[0] in lista:
            item.append([i[0],len(i)])
    for j in pedidos:
        for k in item:
            if k[0] == j[0]:
                itemNuevo.append([k[0],j[-2],k[1]])  
    return itemNuevo

pedidos = [
    [5234,'Las Casitas #123','+56987654321',35990,[2020,11,15]],
    [6532,'Arturo del Python #385','+56224523423',140000,[2020,11,14]],
    [6558,'Calle Sin Salida #1314','+56957258379',15840,[2020,11,14]],
    [6722,'Tosta Dora #1818','+56912457896',25000,[2020,11,12]],
    [7342,'Pasaje Cerrado #8843','+56224523423',3750,[2020,11,14]],
    [7558,'Las Teteras #7785','+56224523423',80000,[2020,11,13]],
]

productos_x_pedido = [
[ 5234 , ["Zapatillas Ribuk o Naik " , " Pantalones finos" ]] ,
[ 6532 , ["Mouse USB" , " Teclado USB" , "Fax /modem 14 k bps " , " Pantalla Gamer 7 pulg ."]] ,
[ 6558 , ["Autito de Juguete " , " Libro de Dinosaurios" ]] ,
[ 6722 , ["Shampoo" , " Jabon " , " Cepillo " , " Esponja " ]] ,
[ 7342 , ["Mascarillas " , " Lapiz Pasta Negro " ] ] ,
[ 7558 , ["Mancuernas " , "Cuerda para saltar " , " Traje de baño " ]]
]

print (obtener_info_pedido(pedidos,5234))
print (pedidos_por_fecha(pedidos,14,11,2020))
print (resumen_pedidos_por_fecha(pedidos, productos_x_pedido, 14, 11, 2020))