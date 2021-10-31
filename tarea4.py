vacunas = {
    "Sinovac":['11.111.111-1','12.345.678-9'],
    "Pfizer":['8.978.657-3'],
    "CanSino":["13.789.456-k"],
    "AstraZeneca":["12.189.446-k"]
    }

dosis = {
 "11.111.111-1":[55,(2021,4,11),(2021,5,10)],
 "12.345.678-9":[47,(2021,6,3)],
 "8.978.657-3": [79,(2021,3,23)],
 "13.789.456-k":[40,(2021,5,18),(2021,6,10)],
 "16.719.226-4":[40,(2021,5,18),(2021,6,10)]
}


def actualizar(vacunas,nombre,rut):
    a = vacunas[nombre]
    a.append(rut)
    vacunas.update({nombre:a})
    return vacunas


def actualizar2daDosis(dosis,fecha,rut):
    a = dosis[rut]
    a.append(fecha)
    dosis.update({rut:a})
    return dosis

def contar(dosis):
    b = []
    mayor = 0
    segundoMayor = 0
    terceroMayor = 0
    edadMayor = 0
    edadSegundoMayor = 0
    edadTerceroMayor = 0
    for i in dosis:
        a = list(dosis[i])
        b.append(a[0])
    for j in b:
        c = b.count(j)
        if c >= mayor and edadMayor!= j:
            terceroMayor = segundoMayor
            segundoMayor = mayor
            mayor = c
            edadTerceroMayor = edadSegundoMayor
            edadSegundoMayor = edadMayor
            edadMayor = j
    print('Edades con mas personas con esquema de inoculacion completo:')
    print(edadMayor, ' Años', mayor, ' personas.')
    print(edadSegundoMayor, ' Años', segundoMayor, ' personas.')
    print(edadTerceroMayor, ' Años', terceroMayor, ' personas.')
opcion = ""

dia = int(input('Ingrese dia: '))    
mes = int(input('Ingrese mes: '))
año = int(input('Ingrese año: '))

fecha = (dia,mes,año)

while opcion.upper() != "N":
    rut = input('Rut: ')
    if rut in dosis:
        if rut in vacunas["CanSino"]:
            print('Vacunacion completa.')
        elif rut in vacunas["Pfizer"]:
            dosis = actualizar2daDosis(dosis,fecha,rut)
            print('Segunda dosis, el paciente debe ser innoculado con: Pfizer.')
        elif rut in vacunas["Sinovac"]:
            dosis = actualizar2daDosis(dosis,fecha,rut)
            print('Segunda dosis, el paciente debe ser innoculado con: Sinovac')
        elif rut in vacunas["AstraZeneca"]:
            dosis = actualizar2daDosis(dosis,fecha,rut)
            print('Segunda dosis, el paciente debe ser innoculado con: AstraZeneca')
    else:
        edad = int(input('Edad: '))
        tipoVacuna = input('Tipo Vacuna: ')
        dosis.update({rut:[edad,fecha]})
        if tipoVacuna == 'CanSino':
           vacuna = actualizar(vacunas,'CanSino',rut)
        elif tipoVacuna == 'Pfizer':
            vacuna = actualizar(vacunas,'Pfizer',rut)
        elif tipoVacuna == 'Sinovac':
            vacuna = actualizar(vacunas,'Sinovac',rut)
        elif tipoVacuna == 'AstraZeneca':
            vacuna = actualizar(vacunas,'AstraZeneca',rut)
    opcion = input("desea continuar? (Y/N): ")
contar(dosis)
