from matrizDispersa.NodoCabecera import nodoCabecera
from matrizDispersa.ListaCabecera import listaCabecera
import os
import webbrowser

class nodoCelda():
    def __init__(self, coordenadaX, coordenadaY, tipoCelda):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.tipoCelda = tipoCelda
        self.capacidad = 0
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

    def setDerecha(self, derecha):
        self.derecha = derecha
    
    def getDerecha(self):
        return self.derecha
    
    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
    
    def getIzquierda(self):
        return self.izquierda

    def setArriba(self, arriba):
        self.arriba = arriba
    
    def getArriba(self):
        return self.arriba

    def setAbajo(self, abajo):
        self.abajo = abajo

    def getAbajo(self):
        return self.abajo
    
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def setTipoCelda(self, tipo):
        self.tipoCelda = tipo

class matrizDispersa():
    def __init__(self):
        self.capa = 0
        self.filas = listaCabecera('Fila') #x
        self.columnas = listaCabecera('Columna') #y

    def insertar(self, pos_x, pos_y, tipo):
        nueva_celda = nodoCelda(pos_x, pos_y, tipo) 
        nodo_X = self.filas.getCabecera(pos_x)
        nodo_Y = self.columnas.getCabecera(pos_y)

        if nodo_X == None:
            nodo_X = nodoCabecera(pos_x)
            self.filas.insertarNodoCabecera(nodo_X)

        if nodo_Y == None:
            nodo_Y = nodoCabecera(pos_y)
            self.columnas.insertarNodoCabecera(nodo_Y)

        # ----- INSERTAR NUEVA_CELDA EN FILA
        if nodo_X.getAcceso() == None: 
            nodo_X.setAcceso(nueva_celda)
        else: 
            if nueva_celda.coordenadaY < nodo_X.getAcceso().coordenadaY:    
                nueva_celda.setDerecha(nodo_X.getAcceso())        
                nodo_X.getAcceso().setIzquierda(nueva_celda)
                nodo_X.setAcceso(nueva_celda)
            else:
                tmp : nodoCelda = nodo_X.getAcceso() 
                while tmp != None:                      
                    if nueva_celda.coordenadaY < tmp.coordenadaY:
                        nueva_celda.setDerecha(tmp)
                        nueva_celda.setIzquierda(tmp.getIzquierda())
                        tmp.getIzquierda().setDerecha(nueva_celda)
                        tmp.setIzquierda(nueva_celda)
                        break
                    elif nueva_celda.coordenadaX == tmp.coordenadaX and nueva_celda.coordenadaY == tmp.coordenadaY: 
                        break
                    else:
                        if tmp.getDerecha() == None:
                            tmp.setDerecha(nueva_celda)
                            nueva_celda.setIzquierda(tmp)
                            break
                        else:
                            tmp = tmp.getDerecha() 
                           
        # ----- INSERTAR NUEVA_CELDA EN COLUMNA
        if nodo_Y.getAcceso() == None:  
            nodo_Y.setAcceso(nueva_celda)
        else:  
            if nueva_celda.coordenadaX < nodo_Y.getAcceso().coordenadaX:
                nueva_celda.setAbajo(nodo_Y.getAcceso())
                nodo_Y.getAcceso().setArriba(nueva_celda)
                nodo_Y.setAcceso(nueva_celda)
            else:
                tmp2 : nodoCelda = nodo_Y.getAcceso()
                while tmp2 != None:
                    if nueva_celda.coordenadaX < tmp2.coordenadaX:
                        nueva_celda.setAbajo(tmp2)
                        nueva_celda.setArriba(tmp2.getArriba())
                        tmp2.getArriba().setAbajo(nueva_celda)
                        tmp2.setArriba(nueva_celda)
                        break
                    elif nueva_celda.coordenadaX == tmp2.coordenadaX and nueva_celda.coordenadaY == tmp2.coordenadaY: 
                        break
                    else:
                        if tmp2.getAbajo() == None:
                            tmp2.setAbajo(nueva_celda)
                            nueva_celda.setArriba(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getAbajo()

    #Unidades militares
    def ubicarCoordenada(self, fila, columna, capacidad, tipo):
        try:
            tmp : nodoCelda = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    tmp.setCapacidad(capacidad)
                    tmp.setTipoCelda(tipo)
                    return tmp
                tmp = tmp.getDerecha()
            return None
        except:
            print('Coordenada no encontrada')
            return None

    def recorridoPorFila(self, fila):
        inicio : nodoCabecera = self.filas.getCabecera(fila)
        tmp : nodoCelda = inicio.getAcceso()
        while tmp != None:
            print(tmp.coordenadaX, tmp.coordenadaY, tmp.tipoCelda)
            tmp = tmp.getDerecha()
    
    
    