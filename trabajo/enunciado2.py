lista1 = ['aas','gbasja',"aksfj","agkl",'asmaeb']

lista2 = ['gis','asmaeb',"palsdhu","jafkhs","jafkhs",'wowoowso','aas']

listaNueva = []

for i in lista1:
    if i not in listaNueva:
        if i in lista2:
            listaNueva.append(i)
        elif lista1.count(i) >1:
            listaNueva.append(i)



for j in lista2:
    if j not in listaNueva:
        if j in lista1:
            listaNueva.append(j)
        elif lista2.count(j) >1:
            listaNueva.append(j)

print(listaNueva)