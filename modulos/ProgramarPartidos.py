'''
Funcion para implementar en el proyecto Liga Betplay 
para la programacion de partidos (equipo visitante y local).
By Mariana Vargas
'''
import os
import json
import modulos.salir as s
import modulos.mensajes as m
LIGA_BASE = None

#Implementaciòn archivo JSON
def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
    
def guardarLiga (ligaBetplay:dict, LIGA_BASE:str): #guargar cambie json a str
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)

#Funcion para evaluar registro de equipos al partido
def addPartido (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    os.system ('cls')
    #Ingresar datos de equipo visitante y equipo local 
    equipoLocal = input ('Ingrese el nombre del equipo local: ').capitalize()
    equipoVisitante = input ('Ingrese el nombre del equipo visitante: ').capitalize()
    fechaPartido = ''
    
    #Evaluar si los equipos ingresados estan registrados previamente
    if (equipoLocal in ligaBetplay) and (equipoVisitante in ligaBetplay):
        programarPartidos (LIGA_BASE,equipoLocal,equipoVisitante)
    #Mensaje en caso de que no esten registrados
    else:
        print (m.msgEquipo)
        os.system ('pause')

#Funcion para programar partidos    
def programarPartidos (LIGA_BASE:str,equipoLocal:str,equipoVisitante:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    isAddPartido = True
    while (isAddPartido):
        os.system ('cls')
        fechaPartido = input('Ingrese la fecha del partido (dd/mm/aaaa): ') #Ingresar la fecha de ejecucion del partido
        partido = {
            'Equipo Local': equipoLocal,
            'Equipo Visitante': equipoVisitante,
            'Fecha programada': fechaPartido,
            'Goles Equipo Local': 0,
            'Goles Equipo Visitante': 0
        }
        #Guardar datos del partido
        if 'Partidos' not in ligaBetplay[equipoLocal]:
            ligaBetplay[equipoLocal]['Partidos'] = {}
        ligaBetplay[equipoLocal]['Partidos'][fechaPartido] = partido
        guardarLiga(ligaBetplay,LIGA_BASE)

        print(f"Partido entre {equipoLocal} y {equipoVisitante} programado para el {fechaPartido}.")
        isAddPartido = s.validateAnswer ('¿Desea programar otro partido para estos equipos S(Si) N(No)?')

#Funcion para la visualizacion de partidos programados
def mostrarPartidos (LIGA_BASE:str):
    print ("PARTIDOS PROGRAMADOS")
    ligaBetplay = cargarLigaJson(LIGA_BASE)

    isFoundPartidos = False
    #Por cada equipo evaluar si tiene partidos programados
    for equipoLocal, datosEquipo in ligaBetplay.items():
        print (f'Equipo Local: {equipoLocal}')
        #Si el equipo tiene partidos programados como local
        if 'Partidos' in datosEquipo and isinstance(datosEquipo['Partidos'], dict):
            isFoundPartidos = True
            for fechaPartido, partido in datosEquipo['Partidos'].items():
                if isinstance (partido,dict):
                    equipoVisitante = partido.get ('Equipo Visitante', '')
                    print (f' -Fecha Partido: {fechaPartido}, Equipo Local: {equipoLocal}, Equipo Visitante: {equipoVisitante}')
        #En caso de no tener partidos programados como local
        else:
            print ('El equipo no tiene partidos programados como equipo Local')
    #Si no hay partidos registrados
    if not isFoundPartidos:
        print ("No hay partidos registrados")

        