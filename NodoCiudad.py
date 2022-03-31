from matrizDispersa.MatrizDispersa import matrizDispersa
from ListaRobots import listaRobots

class nodoCiudad():
    def __init__(self, nombre, nFilas, nColumnas):
        self.nombre = nombre
        self.nFilas = nFilas
        self.nColumnas = nColumnas
        self.noUCiviles = 0
        self.noRecursos = 0
        self.matriz = matrizDispersa()
        self.robots = listaRobots()
        self.siguiente = None
        

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, ciudad):
        self.siguiente = ciudad

    def getNombre(self):
        return self.nombre 
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setNFilas(self, filas):
        self.nFilas = filas
    
    def setNColumnas(self, columnas):
        self.nColumnas = columnas
    
    def setNoUC(self, uCiviles):
        self.noUCiviles = uCiviles
    
    def setNoRecursos(self, recursos):
        self.noRecursos = recursos