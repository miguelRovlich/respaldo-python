class Alumno:
    def __init__(self):
        self.rut = ""
        self.nombre = ""
        self.edad = 0
        self.asistencia = 0
        self.notas = {}
        self.promedio = 0
        self.situacion = ""
    def __str__(self):
        return self.rut+" "+self.nombre+" "+str(self.edad)+" "+str(self.asistencia)+" "+str(self.notas)+" "+str(self.promedio)+" "+self.situacion

    def agregarNota(self,num_nota,nota):
        try:
            self.notas[num_nota] = nota
            return "Nota agregada satisfactoriamente."
        except:
            return "Algo salio mal."
    
    def calcularNotaMinima(self):
        menor = 100
        for i in self.notas:
            if self.notas[i] <menor:
                menor = self.notas[i]
        return menor
    
    def calcularNotaMaxima(self):
        mayor = 0
        for i in self.notas:
            if self.notas[i] >mayor:
                mayor = self.notas[i]
        return mayor
    
    def calcularDesviacionEstandar(self):
        suma = 0
        cont = 0
        for i in self.notas:
            suma += self.notas[i]
            cont += 1
        
        promedio = suma/cont
        sumaDesviacion = 0
        for j in self.notas:
            sumaDesviacion +=(self.notas[j]-promedio)**2
        
        radicando = suma/(len(self.notas)-1)
        return radicando*0.5

    def incrementarNota(self):
        if self.asistencia>=0.9:
            for i in self.notas:
                self.notas[i] += 1.03
        elif self.asistencia>=0.75 and self.asistencia<0.9:
            for i in self.notas:
                self.notas[i] += 1.02
        elif self.asistencia>=0.75:
            for i in self.notas:
                self.notas[i] += 1.01
    
    def calcularPromedio(self):
        try:
            suma = 0
            value2=0
            for i in self.notas:
                suma += self.notas[i]
                value2+=1
            self.promedio = suma/value2
            return True
        except:
            return False

    def asignaSituacion(self):
        if self.promedio>=4:
            self.situacion = "Aprobado"
        else:
            self.situacion = "Reprobado"

    def getRut(self): 
        return self.rut 
        
    def setRut(self, a):  
         self.rut = a 
  
    def getRut(self): 
        return self.nombre 
        
    def setNombre(self, a):  
         self.nombre = a 
    
    def getEdad(self): 
        return self.edad 
        
    def setEdad(self, a):  
         self.edad = a 
    
    def getAsistencia(self): 
        return self.asistencia 
        
    def setAsistencia(self, a):  
         self.asistencia = a 
  
    def getNotas(self): 
        return self.notas 
        
    def setNotas(self, a):  
         self.notas = a 
  
    def getPromedio(self): 
        return self.promedio 
        
    def setPromedio(self, a):  
         self.promedio = a 

    
    def getSituacion(self): 
        return self.situacion 
        
    def setSituacion(self, a):  
         self.situacion = a


if __name__ == "__main__":
    alumno1 = Alumno()
    alumno2 = Alumno()
    alumno3 = Alumno()
    #alumno1
    alumno1.setRut("30531119-1")
    alumno1.setNombre("Jose")
    alumno1.setEdad(23)
    alumno1.setAsistencia(0.66)
    alumno1.agregarNota(1,4.2)
    alumno1.agregarNota(2,6.5)
    alumno1.agregarNota(3,3.1)
    alumno1.calcularPromedio()
    
    print(alumno1.calcularNotaMaxima())
    print(alumno1.calcularNotaMinima())
    print(alumno1.calcularDesviacionEstandar())
    alumno1.incrementarNota()
    print(alumno1)


    #alumno2
    alumno2.setRut("89217771-1")
    alumno2.setNombre("Adrian")
    alumno2.setEdad(25)
    alumno2.setAsistencia(0.88)
    alumno2.agregarNota(1,5.2)
    alumno2.agregarNota(2,2.5)
    alumno2.agregarNota(3,6.1)
    alumno2.calcularPromedio()
    
    print(alumno2.calcularNotaMaxima())
    print(alumno2.calcularNotaMinima())
    print(alumno2.calcularDesviacionEstandar())
    alumno2.incrementarNota()
    print(alumno2)



    
    #alumno3
    alumno3.setRut("20357880-k")
    alumno3.setNombre("Nadia")
    alumno3.setEdad(21)
    alumno3.setAsistencia(0.98)
    alumno3.agregarNota(1,6.2)
    alumno3.agregarNota(2,6.7)
    alumno3.agregarNota(3,6.9)
    alumno3.calcularPromedio()
    
    print(alumno3.calcularNotaMaxima())
    print(alumno3.calcularNotaMinima())
    print(alumno3.calcularDesviacionEstandar())
    alumno3.incrementarNota()
    print(alumno3)