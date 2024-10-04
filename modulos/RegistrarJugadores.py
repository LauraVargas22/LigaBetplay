'''
Funcion para implementar en el proyecto Liga Betplay 
para el registro del plantel (jugadores, posición y dorsal).
By Mariana Vargas
'''
import os
import json
import modulos.salir as s
import modulos.mensajes as m
import modulos.RegistrarEquipo as re
LIGA_BASE = None

def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
    
def guardarLiga (ligaBetplay:dict, LIGA_BASE:json):
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)

def addPlantel (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    nomEquipo = input ('Ingrese el nombre del equipo a buscar: ').capitalize()
    if (len(ligaBetplay)> 0):
        for equipo in ligaBetplay:
            if (nomEquipo in equipo):
                addJugador (LIGA_BASE,nomEquipo)
                break
        else:
            print (m.msgEquipo)
            os.system ('pause')
    else: 
        os.system ('cls')
        print (m.msgAdvice)
        os.system ('pause')

def addJugador (LIGA_BASE: str,nomEquipo:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    isAddJugador = True
    while (isAddJugador):
        os.system ('cls')
        nomJugador = input ('Ingrese el nombre del jugador a registrar\n').capitalize()
        if 'Jugadores' not in ligaBetplay[nomEquipo]:
            ligaBetplay[nomEquipo]['Jugadores'] = {}
            
        if (nomJugador in ligaBetplay[nomEquipo]['Jugadores']):
            print ("El jugador ya se encuentra registrado")
            os.system('pause')
        else:
            posJugador = input(f'Ingrese la posición del jugador {nomJugador}\n')
            dorsalJugador = int(input(f'Ingrese el dorsal del jugador {nomJugador}\n'))
            Jugadores = {
                'Jugadores': nomJugador,
                'Posición Jugador': posJugador,
                'Dorsal Jugador': dorsalJugador,
                'Tarjeta Amarilla': 0,
                'Tarjeta Roja': 0,
                'Goles Anotados': 0,
                'Faltas Cometidas': 0
                }

            ligaBetplay[nomEquipo]['Jugadores'][nomJugador] = Jugadores
            guardarLiga(ligaBetplay,LIGA_BASE)
            print (f'El jugador {nomJugador} se ha registrado al equipo {nomEquipo}')
            isAddJugador = s.validateAnswer ('¿Desea registrar otro jugador a este equipo S(Si) N(No)?')

def jugadoresRegistrados (LIGA_BASE:str):
    print("JUGADORES REGISTRADOS:")
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    if (len(ligaBetplay)== 0):
        print (m.msgAdvice)
        return
    
    for nomEquipo, datosEquipo in ligaBetplay.items():
        print (f'Equipo: {nomEquipo}')

        if ('Jugadores' in datosEquipo) and datosEquipo['Jugadores']:
            for nomJugador, dataJugador in datosEquipo['Jugadores'].items():
                if isinstance (dataJugador,dict):
                    posJugador = dataJugador.get ('Posición Jugador', '')
                    dorsalJugador = dataJugador.get ('Dorsal Jugador', '')
                    print (f' -Nombre: {nomJugador}, Posición: {posJugador}, Dorsal: {dorsalJugador}')
        else:
            print ("El equipo no tiene jugadores registrados")

def removeJugadores (LIGA_BASE:str):
    os.system ('cls')
    print ("EQUIPOS REGISTRADOS")
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    equipos = re.equiposRegistrados (LIGA_BASE)
    print (equipos)
    equipo = input ('Ingrese el equipo a eliminar jugadores: ').capitalize()
    if (equipo in ligaBetplay):
        jugadorEliminar = jugadoresRegistrados(LIGA_BASE)
        print (jugadorEliminar)
        jugadorEliminar = input ('¿Cuál jugador desea eliminar? ').capitalize()
        if jugadorEliminar in ligaBetplay[equipo]['Jugadores']:
            if s.validateAnswer (m.msgDelete):
                ligaBetplay[equipo]['Jugadores'].pop(jugadorEliminar)
                print (f'Jugador {jugadorEliminar} ha sido eliminado')
                guardarLiga(ligaBetplay,LIGA_BASE)
            else:
                print (m.msgCancel)
        else:
            print (m.msgJugador)
    else:
        print (m.msgEquipo)
