from matrizDispersa.NodoCabecera import nodoCabecera
from matrizDispersa.ListaCabecera import listaCabecera
from os import startfile, system

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
    
    def graficarMatriz(self, ciudad):
        name = "graphviz"
        with open(name + ".dot", "w") as dot:
            #Características generales de la gráfica:
            dot.write('digraph Matriz{\n node[fontname="IMPACT", shape = box fillcolor="#FFEDBB" color=white style=filled, border = white]nodesep=0.05; ranksep=0.05;')
            dot.write('fontname="IMPACT"\n subgraph cluster_p{')
            dot.write('label = "' + ciudad + '"\n labelloc="b" \n bgcolor = white \n edge[dir = "none" style = invisible]')
            #Root:
            dot.write('root[label="", fillcolor=white]')
            
            #CABECERAS -----------------------------------

            #fActual representa la fila actual ---- crear cada nodo cabecera(fila)
            fActual : nodoCabecera = self.filas.primero

            while fActual != None:
                dot.write('F' + str(fActual.id) + '[label = "' + str(fActual.id) +'", group = 1, fillcolor = white]\n')
                fActual = fActual.siguiente

            # enlazar nodos cabecera(fila)
            fActual : nodoCabecera = self.filas.primero

            while fActual != None:
                if fActual.siguiente != None:
                    dot.write('F'+ str(fActual.id) + '-> F'+ str(fActual.siguiente.id) + '\n')
                fActual = fActual.siguiente
            
            #CABECERAS -----------------------------------

            #cActual representa la columna actual ---- crear cada nodo cabecera(columna)
            cActual : nodoCabecera = self.columnas.primero

            while cActual != None:
                dot.write('C' + str(cActual.id) + '[label = "' + str(cActual.id)+'", group = ' + str(int(cActual.id)+1) + ', fillcolor = white]\n')
                cActual = cActual.siguiente

            # enlazar nodos cabecera(columna)
            cActual : nodoCabecera = self.columnas.primero

            while cActual != None:
                if cActual.siguiente != None:
                    dot.write('C'+ str(cActual.id) + '-> C'+ str(cActual.siguiente.id) + '\n')
                cActual = cActual.siguiente

            # rank same para cabecera(columna)
            cActual : nodoCabecera = self.columnas.primero
            iColumna = 1

            dot.write('{rank = same; root')
            while cActual != None:
                dot.write(', C' + str(iColumna))
                iColumna += 1
                cActual = cActual.siguiente
            
            dot.write('}\n')
            
            # enlazar root a cabeceras
            dot.write('root -> F1\n')
            dot.write('root -> C1\n')

            # DATOS DE LAS CELDAS ----------------------------
            fActual : nodoCabecera = self.filas.primero

            while fActual != None:
                tmp : nodoCelda = fActual.acceso
                while tmp != None:
                    if tmp.tipoCelda == "CI":
                        color = "black"
                    elif tmp.tipoCelda == "CT":
                        color = "white"
                    elif tmp.tipoCelda == "PE":
                        color = "#70ad47"
                    elif tmp.tipoCelda == "UM":
                        color = "#c30a09"
                    elif tmp.tipoCelda == "C":
                        color = "#2d71b1"
                    elif tmp.tipoCelda == "R":
                        color = "#636161"
                    else:
                        color = "white"

                    dot.write('celdaF' + str(tmp.coordenadaX) + '_C' + str(tmp.coordenadaY) + '[label="", group = ' + str(int(tmp.coordenadaY)+1) + ' , fillcolor = "'+ color + '"]\n')
                    tmp = tmp.derecha
                fActual = fActual.siguiente
            
            # apuntadores de las primera fila a la  primera celda y entre celdas
            fActual : nodoCabecera = self.filas.primero

            while fActual != None:
                tmp = fActual.acceso
                dot.write('\nF' + str(tmp.coordenadaX) + ' -> celdaF' + str(tmp.coordenadaX) + '_C' + str(tmp.coordenadaY))
                while tmp != None:
                    if tmp.derecha != None:
                        dot.write('\nceldaF'+str(tmp.coordenadaX)+'_C'+str(tmp.coordenadaY)+' -> celdaF'+str(tmp.coordenadaX)+'_C'+str(int(tmp.coordenadaY)+1))
                    tmp = tmp.derecha
                fActual = fActual.siguiente

            # apuntadores de la primera columna a la primera celda y entre celdas
            cActual : nodoCabecera = self.columnas.primero

            while cActual != None:
                tmp = cActual.acceso
                dot.write('\nC' + str(tmp.coordenadaY) + '-> celdaF' + str(tmp.coordenadaX) + '_C' + str(tmp.coordenadaY))
                while tmp != None:
                    if tmp.abajo != None:
                        dot.write('\nceldaF' + str(tmp.coordenadaX) + '_C' + str(tmp.coordenadaY) + '-> celdaF' + str(int(tmp.coordenadaX)+1) + '_C'+ str(tmp.coordenadaY))
                    tmp = tmp.abajo
                cActual = cActual.siguiente 
            
            #rank de nodos celda
            fActual : nodoCabecera = self.filas.primero

            while fActual != None:
                tmp = fActual.acceso
                dot.write('\n {rank = same; F' + str(fActual.id))

                while tmp != None:
                    dot.write(', celdaF' + str(tmp.coordenadaX) + '_C' + str(tmp.coordenadaY))
                    tmp= tmp.derecha
            
                dot.write('}')
                fActual = fActual.siguiente
            
            dot.write('}\n')
            dot.write('}')
        system("dot -Tpng graphviz.dot -o graphviz.png")
        system("dot -Tpdf graphviz.dot -o graphviz.pdf")
        startfile("graphviz.png")
        startfile("graphviz.pdf")

            
    