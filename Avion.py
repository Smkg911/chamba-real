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
    
    def contarSillasEjecutivasOcupadas(self): 
        nOcupadas = 0 
        for ejecutivas in self.sillasEjecutivas: 
            if Silla.sillaAsignada() == True: 
                nOcupadas += 1  
                
    def contarSillaEconomicas(self):
        contador = 0
        for i in range(self.SILLAS_ECONOMICAS):
            if Silla.getPasajero() == None:
                contador +=1 
        return contador 
    
    def contarPasilloEjecutivas(self):
        contador = 0 
        for i in range(self.sillasEjecutivas): 
            if Silla.getUbicacion1() == 'pasillo' and Silla.getPasajero() == None: 
                contador += 1 
        return contador 

    def desocuparAvion(self):
        for i in range(self.SILLAS_ECONOMICAS + self.SILLAS_EJECUTIVAS): 
            Silla.desasignarPasajero()
    
    
    