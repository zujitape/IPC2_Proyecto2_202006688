from listas.NodoRobot import nodoRobot

class listaRobots():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    
    def insertarRobot(self, nombre, tipo, capacidad):
        nuevoRobot = nodoRobot(nombre, tipo, capacidad)
        self.size += 1
        if self.primero == None:
            self.primero = nuevoRobot
            self.ultimo = nuevoRobot
        else:
            self.ultimo.setSiguiente(nuevoRobot)
            self.ultimo = nuevoRobot
        return nuevoRobot
    
    def mostrarRobots(self):
        tmp = self.primero
        for i in range(self.size):
            print(" ",i+1, "|",tmp.tipo, "-", tmp.nombre)
            tmp = tmp.siguiente
    
    def verDisponibilidad(self, tipo):
        tmp = self.primero
        contador = 0
        while tmp != None:
            if tmp.tipo == tipo:
                contador += 1
            tmp = tmp.siguiente
        return contador
    
    def verTipo(self, tipo):
        tmp = self.primero
        i = 1
        while tmp != None:
            if tmp.tipo == tipo:
                print(i,".", tmp.nombre)
                i += 1
            tmp = tmp.siguiente
        