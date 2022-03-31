class nodoRobot():
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = 0
        self.siguiente = None

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, ciudad):
        self.siguiente = ciudad
    
    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad
    
    