class nodoCabecera():
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None #acceso a las celdas de la matriz
    
    def getAcceso(self):
        return self.acceso

    def setAcceso(self, nuevo_acceso):
        self.acceso = nuevo_acceso