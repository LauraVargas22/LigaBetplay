import os
import json
import modulos.salir as s
import modulos.mensajes as m
LIGA_BASE = None
#JSON A DICT
def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
#DICT A JSON  
def guardarLiga (ligaBetplay:dict, LIGA_BASE: str):
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)
    
def addEquipo (LIGA_BASE: str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)

    isAddEquipo = True
    while (isAddEquipo):
        os.system ('cls')
        nomEquipo = input('Ingrese el nombre del equipo a registrar\n').capitalize()
        if nomEquipo in ligaBetplay:
            print ("El equipo ya se encuentra registrado")
            os.system('pause')
        else:
            equipo = {
                'Nombre Equipo': nomEquipo,
                'Jugadores': {
                    'Nombre Jugadores': '',
                    'Posición Jugador': '',
                    'Dorsal Jugador': 0,
                    'Tarjeta Amarilla': 0,
                    'Tarjeta Roja': 0,
                    'Goles Anotados': 0,
                    'Faltas Cometidas': 0,
                    },
                'Técnicos':{
                    'Nombre': '',
                    'Cargo': ''
                    },
                'Partido': {
                    'Fecha Partido': '',
                    'Equipo Local': '',
                    'Equipo Visitante': '',
                    'Goles Equipo Local': 0,
                    'Goleadores Equipo Local': '',
                    'Goles Equipo Visitante': 0,
                    'Goleadores Equipo Visitante': '',
                    },       
                }
            
            ligaBetplay [nomEquipo] = equipo
            guardarLiga(ligaBetplay,LIGA_BASE)
            isAddEquipo = s.validateAnswer('¿Desea agregar otro equipo S(Si) N(No)?')

def equiposRegistrados (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    for nomEquipo in ligaBetplay.keys():
        print (nomEquipo)

def removeEquipo (LIGA_BASE: str):
    print ("EQUIPOS REGISTRADOS")
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    equipoEliminar = equiposRegistrados (LIGA_BASE)
    equipoEliminar = input('¿Cuál equipo desea eliminar? ').capitalize()
    if equipoEliminar in ligaBetplay:
        if s.validateAnswer (m.msgDelete):
            ligaBetplay.pop(equipoEliminar)
            guardarLiga(ligaBetplay,LIGA_BASE)
        else: 
            print (m.msgCancel)
    else:
        print(m.msgEquipo)
    
