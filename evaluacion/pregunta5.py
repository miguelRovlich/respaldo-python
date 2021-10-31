import random
def calcular_produccion_metal(nivel):
    resultado = 30*nivel*1.1**nivel
    return resultado
def calcular_produccion_cristal(nivel):
    resultado = 20*nivel*1.1**nivel
    return resultado
def calcular_sintetizacion_deuterio(nivel,t_max,v_universo):
    resultado = 10*nivel*1.1**nivel*(1.44-0.0004*t_max)*v_universo
    return resultado



t_max = random.randint(10,30)
v_universo = random.randint(1,5)
nivel = int(input("Ingrese nivel: "))
print("Produccion de Metal: ",calcular_produccion_metal(nivel))

print("Produccion de Cristal: ",calcular_produccion_cristal(nivel))
print("Sintetizacion de Deuterio",calcular_sintetizacion_deuterio(nivel,t_max,v_universo))