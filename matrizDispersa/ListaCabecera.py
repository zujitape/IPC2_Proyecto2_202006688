from matrizDispersa.NodoCabecera import nodoCabecera

class listaCabecera():
    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None
        self.tipo = tipo #TIPO: fila/columna
        self.size = 0


    def insertarNodoCabecera(self, nuevoNodo):
        self.size += 1

        if self.primero == None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            if nuevoNodo.id < self.primero.id:
                nuevoNodo.siguiente = self.primero
                self.primero.anterior = nuevoNodo
                self.primero = nuevoNodo
            
            elif nuevoNodo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevoNodo
                nuevoNodo.anterior = self.ultimo
                self.ultimo = nuevoNodo
            
            else:
                tmp = self.primero
                while tmp != None:
                    if nuevoNodo.id < tmp.id:
                        nuevoNodo.siguiente = tmp
                        nuevoNodo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevoNodo
                        tmp.anterior = nuevoNodo
                        break
                    elif nuevoNodo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break
    
    def showCabeceras(self):
        tmp = self.primero
        while tmp != None:
            print('Header ', self.tipo, " ", tmp.id)
            tmp = tmp.siguiente

    
    def getCabecera(self, id):
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None
