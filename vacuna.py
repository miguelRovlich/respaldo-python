personas = int(input("ingrese cantidad de personas a vacunar: "))
cont = 1
mujeres = 0 
primeraDosis = 0
pfizer = 0
edadMujeres = 0
while cont <= personas:
    print("ingrese datos de paciente ",cont)
    edad = int(input("ingrese edad: "))
    genero = input("Ingrese genero (M/H) ").upper()
    dosis = int(input("Ingrese dosis (1/2) "))
    vacuna = input("Ingrese vacuna Pfizer o Sinnovac: (P/S) ").upper()
    if genero == "M":
        mujeres = mujeres + 1
        edadMujeres = edadMujeres + edad
    if dosis == 1:
        primeraDosis = primeraDosis + 1
    if vacuna == "P":
        pfizer = pfizer + 1
    cont = cont + 1
print("cantidad de personas vacunadas con primera dosis: ",primeraDosis)
promedioEdad = edadMujeres / mujeres
porcentajeMujeres = 100 * (mujeres / personas)
print("promedio de edad de las mujeres: ",promedioEdad)
print("porcentaje de mujeres: ",promedioMujeres)
print("cantidad de personas vacunadas Pfizer: ",pfizer)
