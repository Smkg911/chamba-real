from Silla import Silla
class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEonomicas = []
        self.AsignacionSillasEjecuticas()
        

    def AsignacionSillasEjecuticas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if ((i+1)%2) == 0: 
                self.sillasEjecutivas.append(Silla((i+1), False, 'pasillo'))
            else:
                self.sillasEjecutivas.append(Silla((i+1), False, 'ventana'))
                
    # def AsignarSillasEconomicasPasillo(self):
    #     for i in range (1, self.SILLAS_ECONOMICAS, 3):
    #         self.sillasEconomicas.append(Silla(i, True, 'ventana'))
            
    # def AsignarSillasEconomicasPasillo(self):
    #     for i in range (2, self.SILLAS_ECONOMICAS, 3):
    #         self.sillasEconomicas.append(Silla(i, True, 'centro'))
            
    # def AsignarSillasEconomicasPasillo(self):
    #     for i in range (3, self.SILLAS_ECONOMICAS, 3):
    #         self.sillasEconomicas.append(Silla(i, True, 'pasillo'))
    
    def AsignarSillasEconomicasPasillo(self):
        for i in range(1, self.SILLAS_ECONOMICAS + 1):
            if i % 3 == 1:
                self.sillasEconomicas.append(Silla(i, True, 'ventana'))
            elif i % 3 == 2:
                self.sillasEconomicas.append(Silla(i, True, 'centro'))
            else:
                self.sillasEconomicas.append(Silla(i, True, 'pasillo'))
    
    