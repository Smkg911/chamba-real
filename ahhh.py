from Curso import Curso
class Estudiante:
    def __init__(self):
        self.PRUEBA_ACADEMICA = 3.25
        self.CANDIDATO_BECA = 4.75
        self.codigo = 0
        self.nombre = ""
        self.apellido = "" 
        self.curso1 = Curso
        self.curso2 = Curso
        self.curso3 = Curso
        self.curso4 = Curso
        
    def darPromedio(self): 
        notaTotal = 0
        creditosTotales = 0
        if self.curso1.nota > 0.0:
            notaTotal += self.curso1.nota * self.curso1.creditos
            creditosTotales += self.curso1.creditos
        elif self.curso2.nota > 0.0:
            notaTotal += self.curso2.nota * self.curso2.creditos
            creditosTotales += self.curso2.creditos
        elif self.curso3.nota > 0.0:
            notaTotal += self.curso3.nota * self.curso3.creditos
            creditosTotales += self.curso3.creditos
        elif self.curso4.nota > 0.0:
            notaTotal += self.curso4.nota * self.curso4.creditos
            creditosTotales += self.curso4.creditos
        else:
            if notaTotal == 0:
                return 0
        return notaTotal / creditosTotales
    
    def EstaEnPRueba(self):
        return self.darPromedio() <= 3.75
        
    
