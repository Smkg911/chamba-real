class Pasajero: 
    
    def __init__(self, pCedula, pNombre):
        self.__cedula = pCedula
        self.__nombre = pNombre
        
    def getCedula(self):
        return self.__cedula
    
    def setCedula(self, pCedula):
        self.__cedula = pCedula
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, pNombre):
        self.__nombre = pNombre
    
    