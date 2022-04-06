from matrizDispersa.MatrizDispersa import matrizDispersa
from listas.ListaRobots import listaRobots

class nodoCiudad():
    def __init__(self, nombre, nFilas, nColumnas):
        self.nombre = nombre
        self.nFilas = nFilas
        self.nColumnas = nColumnas
        self.noUCiviles = 0
        self.noRecursos = 0
        self.noChapinF = 0
        self.noChapinR = 0
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

    def getNoUC(self):
        return self.noUCiviles
    
    def setNoRecursos(self, recursos):
        self.noRecursos = recursos
    
    def getNoR(self):
        return self.noRecursos
    
    def setNoChapinF(self, noChapinR):
        self.noChapinR = noChapinR
    
    def setNoChapinR(self, noChapinF):
        self.noChapinF = noChapinF
    