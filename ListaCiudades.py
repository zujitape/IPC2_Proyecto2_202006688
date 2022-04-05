from NodoCiudad import nodoCiudad

class listaCiudades():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    #Lista simple para las ciudades
    def insertarCiudad(self, nFilas, nColumnas, nombre):
        nuevaCiudad = nodoCiudad(nombre, nFilas, nColumnas)
        self.size += 1
        if self.primero == None:
            self.primero = nuevaCiudad
            self.ultimo = nuevaCiudad
        else: 
            self.ultimo.setSiguiente(nuevaCiudad)
            self.ultimo = nuevaCiudad   
        return nuevaCiudad
    
    def mostrarCiudades(self):
        tmp = self.primero
        while tmp != None:
            print("▷ ", tmp.nombre, "- > (",tmp.nFilas, ",", tmp.nColumnas, ")\nNúmero de unidades civiles: ", tmp.noUCiviles, "\nNúmero de recursos de la ciudad: ", tmp.noRecursos, "\n")
            tmp = tmp.siguiente
    
    def buscarCiudad(self, name):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == name:
                return tmp
            tmp = tmp.getSiguiente()
    
    def buscarMatrizCiudad(self, name):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == name:
                return tmp.matriz.graficarMatriz()
            tmp = tmp.getSiguiente()

