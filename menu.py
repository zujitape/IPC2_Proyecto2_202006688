from tkinter.filedialog import askopenfilename
import pathlib
import time
from typing import List
from listas.ListaCiudades import listaCiudades
from listas.ListaRobots import listaRobots
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
        if robot != None:
            noCF = nuevaCiudad.noChapinF
            noCR = nuevaCiudad.noChapinR

            for r in robot:

                capacidadR = 0

                nombreR = r.getElementsByTagName('nombre')
                for nR in nombreR:
                    nombreRobot = nR.firstChild.data
                    tipoRobot = nR.attributes['tipo'].value
                    if tipoRobot == "ChapinFighter":
                        capacidadR = nR.attributes['capacidad'].value
                        noCF += 1
                    else:
                        capacidadR = 0
                        noCR += 1

                    nuevaCiudad.robots.insertarRobot(nombreRobot, tipoRobot, capacidadR)
                ListaRobots.insertarRobot(nombreRobot, tipoRobot, capacidadR)
                    
            nuevaCiudad.setNoChapinF(noCF)
            nuevaCiudad.setNoChapinR(noCR)
        else:
            print("No hay etiquetas de robot en el xml.")
            
            

    print("\n╔═══════ LISTA DE CIUDADES ═══════╗")
    ListaCiudades.mostrarCiudades()
    print("╚═══════════════════════════════════╝")

    print("\n╔═══════ LISTA DE ROBOTS ═══════╗")
    nuevaCiudad.robots.mostrarRobots()
    print("╚═════════════════════════════════╝")
    

    

salir = False
opcion = 0


optMision = 0

while not salir:
    print('')
    print('║¯¯¯¯¯¯¯¯¯¯¯¯ MENÚ ¯¯¯¯¯¯¯¯¯¯¯¯¯║\n║ 1. Cargar archivo.            ║\n║ 2. Mostrar lista de ciudades. ║ \n║ 3. Mostrar lista de robots.   ║\n║ 4. Ver gráfica de una ciudad. ║\n║ 5. Asignar una misión         ║\n║ 6. Salir.                     ║\n║-------------------------------║')

    opcion = seleccionarOpt("➔ ¿Qué opción quiere seleccionar? ")

    if opcion == 1:
        print("\n .:*・°.*: CARGAR LISTA DE CIUDADES :*.°・*:.")
        try:
            data = askopenfilename()
            path = pathlib.Path(data)
            if (path.suffix == '.xml'):
                codigo = MiniDom(data)
            else:
                print('ERROR: Seleccionó un tipo de archivo no permitido.')
        except:
            print('Asegúrese de que el archivo tenga estructura correcta.')
        
    elif opcion == 2:
        if ListaCiudades.size >0:
            try:
                print("\n|  Lista de ciudades:  |")
                ListaCiudades.mostrarCiudades()
            except:
                print("¿Ya cargó un archivo al sistema?")
        

    elif opcion == 3:
            name = input("\n➔ Ver robots disponibles de la ciudad: ")
            ciudad = ListaCiudades.buscarCiudad(name)
            if ciudad != None:
                if (ciudad.robots.size>0):
                    print("\n|  Lista de robots de ", ciudad.getNombre(), "  |")
                    ciudad.robots.mostrarRobots()
                else: 
                    print("Esta ciudad no tiene robots disponibles.")
            else:
                print("Asegúrese de que el nombre ingresado sea correcto.")
                opcion == 3

        
    elif opcion == 4:
            name = input("\n➔ Ingrese el nombre de la ciudad que verá: ")
            ciudad = ListaCiudades.buscarCiudad(name)

            if ciudad == None:
                print("Asegúrese de que el nombre ingresado sea correcto.")
            
            else:
                print("\nEstamos generando la gráfica de", ciudad.getNombre())
                ciudad.matriz.graficarMatriz(ciudad.getNombre())


    elif opcion == 5:
        nombreCiudad = input("\n➔ Ingrese el nombre de la ciudad a la que asignará la misión: ")
        ciudad = ListaCiudades.buscarCiudad(nombreCiudad)

        if ciudad != None:
            salirMision = False
            print("\n .:*・°.*: MISIÓN EN "+ str(ciudad.getNombre()).upper() + " :*.°・*:.\n║ 1. Misión de rescate.                    ║\n║ 2. Misión de extracción de recursos.     ║\n║ 3. Regresar al menú principal.           ║")
            optMision = seleccionarOpt("\n➔ Seleccione el tipo de misión que quiere realizar: ")
            print("")

            while not salirMision:
                if optMision == 1:
                    #ROBOT PARA LA MISIÓN DE RESCATE-----------------
                    tipo = "ChapinRescue" 
                    coordX = 0
                    coordY = 0
                    cr = ciudad.robots.verDisponibilidad(tipo) #cr -> almacena la cantidad de robots "ChapinRescue" de la ciudad
                    if cr == 0:
                        print("Esta ciudad no tiene robots disponibles para la misión.")
                        break
                    elif cr == 1:
                        robot = ciudad.robots.primero.nombre
                        print(robot, ", ¡está listo para ir al rescate!")
                        #robot será el primero de la lista
                    else:
                        print("\nRobots disponibles: ")
                        ciudad.robots.verTipo(tipo)
                        robot = input("\n➔ Ingrese el nombre del robot que realizará la misión: ")
                        print(robot,", ¡está listo para ir al rescate!")
                        #robot será el seleccionado por el usuario
                    
                    #UNIDAD CIVIL QUE SE RESCATARÁ------------------------
                    uc = ciudad.getNoUC()
                    if uc == 0:
                        print("No hay unidades civiles para rescatar.")
                        break
                    else:
                        print("\nUnidades civiles de ", ciudad.getNombre())
                        print("[ x , y ]")
                        ciudad.matriz.verTipoCelda("C")
                        print("\nIngrese las coordendas de la unidad civil que se rescatará")
                        coordX = input("➔ Coordenada x: ")
                        coordY = input("➔ Coordenada y: ")  
                        
                        print("Se rescatará la unidad civil de la celda [", coordX,",",coordY,"]")
                    
                    print("\nPuntos de entrada en ", ciudad.getNombre())
                    print("[ x , y ]")
                    ciudad.matriz.verTipoCelda("PE")
                    print("\nIngrese las coordendas del punto de entrada")
                    coordXPE = input("➔ Coordenada x: ")
                    coordYPE = input("➔ Coordenada y: ")  
                    print("Punto de partida [", coordXPE,",",coordYPE,"]")
                    txt = "Unidad civil rescatada: "
                    
                    ciudad.matriz.graficar(ciudad.getNombre(), "Rescate", tipo, robot, coordX, coordY, txt)
                    break
                elif optMision == 2:
                    #ROBOT PARA LA MISIÓN DE RESCATE-----------------
                    tipo = "ChapinFighter" 
                    coordX = 0
                    coordY = 0
                    cr = ciudad.robots.verDisponibilidad(tipo) #cr -> almacena la cantidad de robots "ChapinFighter" de la ciudad
                    if cr == 0:
                        print("Esta ciudad no tiene robots disponibles para la misión.")
                        break
                    elif cr == 1:
                        robot = ciudad.robots.primero.nombre
                        print(robot, ", ¡está listo para ir a la extracción!")
                        #robot será el primero de la lista
                    else:
                        print("\nRobots disponibles: ")
                        ciudad.robots.verTipo(tipo)
                        robot = input("\n➔ Ingrese el nombre del robot que realizará la misión: ")
                        print(robot,", ¡está listo para ir a la extracción!")
                        #robot será el seleccionado por el usuario
                    
                    #UNIDAD CIVIL QUE SE RESCATARÁ------------------------
                    nr = ciudad.getNoR()
                    if nr == 0:
                        print("No hay recursos para extraer.")
                        break
                    else:
                        print("\nRecursos de ", ciudad.getNombre())
                        print("[ x , y ]")
                        ciudad.matriz.verTipoCelda("R")
                        print("\nIngrese las coordendas del recurso que se extraerá")
                        coordX = input("➔ Coordenada x: ")
                        coordY = input("➔ Coordenada y: ")  
                        print("Se extraerá el recurso de la celda [", coordX,",",coordY,"]")
                    
                    print("\nPuntos de entrada en ", ciudad.getNombre())
                    print("[ x , y ]")
                    ciudad.matriz.verTipoCelda("PE")
                    print("\nIngrese las coordendas del punto de entrada")
                    coordXPE = input("➔ Coordenada x: ")
                    coordYPE = input("➔ Coordenada y: ")  
                    print("Punto de partida [", coordXPE,",",coordYPE,"]")

                    txt = "Recurso extraido: "
                    ciudad.matriz.graficar(ciudad.getNombre(), "Extraccion", tipo, robot, coordX, coordY, txt)
                    break
                elif optMision == 3:
                    salirMision = True
            
        else:
            print("Asegúrese de ingresar un nombre correcto.")
    elif opcion == 6:
        print("Saliendo... :b")
        time.sleep(0.5)
        salir = True

    else:
        print ("Asegúrate de ingresar una opción correcta.")