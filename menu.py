from tkinter.filedialog import askopenfilename
import pathlib
import time
from ListaCiudades import listaCiudades
from ListaRobots import listaRobots
from xml.dom import minidom

ListaCiudades = listaCiudades()
ListaRobots = listaRobots()

class Menu():
    pass

def seleccionarOpt(salida):
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(salida))
            correcto=True
        except ValueError:
            print('Asegúrese de seleccionar una opción correcta.')
    return num

def MiniDom(ruta):
    mydoc = minidom.parse(ruta)

    #ciudades del archivo
    ciudad = mydoc.getElementsByTagName('ciudad')
    for c in ciudad: 
        noUC = 0 #número de unidades civiles en la ciudad / validación para misión de rescate
        noR = 0 #número de recursos en la ciudad / validación para misión de extracción

        # AGREGAR UNA NUEVA CIUDAD ----------------- 
        nombre = c.getElementsByTagName('nombre')
        for n in nombre:

            nombreCiudad = n.firstChild.data
            nF = int(n.attributes['filas'].value)
            nC = int(n.attributes['columnas'].value)

            nuevaCiudad = ListaCiudades.insertarCiudad(nF, nC, nombreCiudad)
        
        filas = c.getElementsByTagName('fila')
        posX = 0
        posY = 1
        tipo = ''
        for f in filas:
            posX = int(f.attributes['numero'].value)
            cadena = f.firstChild.data
            cadena = cadena.replace('"', '')

            for ca in cadena:
                if ca == '*':
                    tipo = 'CI'
                elif ca == ' ':
                    tipo = 'CT'
                elif ca == 'E':
                    tipo = 'PE'
                elif ca == 'C':
                    tipo = 'C'
                    noUC += 1
                elif ca == 'R':
                    tipo = 'R'
                    noR += 1
                else:
                    pass
                
                nuevaCiudad.matriz.insertar(posX, posY, tipo)

                if posY < nC:
                    posY += 1
                else:
                    posY = 1

        unidadMilitar = c.getElementsByTagName('unidadMilitar')
        for um in unidadMilitar:
            iFila = int(um.attributes['fila'].value)
            iColumna = int(um.attributes['columna'].value)
            capacidad = um.firstChild.data
            tipo = 'UM'

            nuevaCiudad.matriz.ubicarCoordenada(iFila, iColumna, capacidad, tipo)  

        nuevaCiudad.setNoUC(noUC)
        nuevaCiudad.setNoRecursos(noR)
    
    #robots del archivo
        robot = mydoc.getElementsByTagName('robot')
        for r in robot:

            capacidadR = 0

            nombreR = r.getElementsByTagName('nombre')
            for nR in nombreR:
                nombreRobot = nR.firstChild.data
                tipoRobot = nR.attributes['tipo'].value

                if tipoRobot == "ChapinFighter":
                    capacidadR = nR.attributes['capacidad'].value
                else:
                    capacidadR = 0

                nuevaCiudad.robots.insertarRobot(nombreRobot, tipoRobot, capacidadR)

    print("----- CIUDADES AGREGADAS -----")
    ListaCiudades.mostrarCiudades()

    nuevaCiudad.robots.mostrarRobots()
    print("\n----- ROBOTS AGREGADAS -----")

    

salir = False
opcion = 0

while not salir:
    print('')
    print('¡BIENVENIDO! \n 1. Cargar archivo. \n 2. Mostrar pisos. \n 3. Ver piso. \n 4. Salir.')

    opcion = seleccionarOpt("¿Qué opción quiere seleccionar? ")

    if opcion == 1:
        print("\n .:*・°☆CARGAR LISTA DE CIUDADES☆.。.:")
        data = askopenfilename()
        path = pathlib.Path(data)
        if (path.suffix == '.xml'):
            codigo = MiniDom(data)
        else:
            print('ERROR: Seleccionó un tipo de archivo no permitido.')
        
    elif opcion == 2:
        try:
            print("\nLista de pisos disponibles: ")
            
        except:
            print("¿Ya cargó un archivo al sistema?")

    elif opcion == 3:
            name = input("\nIngrese el nombre del piso que manejará: ")           

    elif opcion == 4:
        print("Saliendo... :b")
        time.sleep(0.5)
        salir = True

    else:
        print ("Asegúrate de ingresar una opción correcta.")