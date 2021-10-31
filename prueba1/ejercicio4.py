masConveniente = 0
utilidadMasAlta = 0
for i in range(3):
    ingresos = int(input("Ingrese ingresos esperados: "))
    costos = int(input("Ingrese costos de locacion: "))
    utilidad = ingresos-costos
    if utilidad> utilidadMasAlta:
        utilidadMasAlta = utilidad
        i = masConveniente


if masConveniente == 0:
  print("La localizacion A es la que tiene mejor rendimiento")
elif masConveniente == 1:
  print("La localizacion B es la que tiene mejor rendimiento")
elif masConveniente == 2:
  print("La localizacion C es la que tiene mejor rendimiento")
