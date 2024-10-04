'''
Funcion para implementar en el proyecto Liga Betplay 
se mostrarán las estadísticas del torneo. 
By Mariana Vargas
'''
import os
import json
import modulos.mensajes as m
import modulos.RegistrarJugadores as rj
LIGA_BASE = None

def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
    
def guardarLiga (ligaBetplay:dict, LIGA_BASE:str):
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)

def estadisticaEquipo (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson (LIGA_BASE)
    totalGoles = {}

    for equipoLocal, datosEquipo in ligaBetplay.items():
        if ('Partidos' in datosEquipo) and isinstance(datosEquipo['Partidos'],dict):
            for fechaPartido, partido in datosEquipo['Partidos'].items():
                if isinstance (partido,dict):
                    golesEquipoLocal = partido.get ('Goles Equipo Local', 0)
                    if (equipoLocal not in totalGoles):
                        totalGoles[equipoLocal] = 0
                    totalGoles[equipoLocal] += golesEquipoLocal

                    equipoVisitante = partido.get('Equipo Visitante', '')
                    golesEquipoVisitante = partido.get('Goles Equipo Visitante', 0)
                    if (equipoVisitante not in totalGoles):
                        totalGoles[equipoVisitante] = 0
                    totalGoles[equipoVisitante] += golesEquipoVisitante

    print ("     GOLES POR EQUIPO      ")
    for equipo, goles in totalGoles.items():
        print (f'{equipo}: {goles} goles')

    equipoMaxGoles = max(totalGoles, key=totalGoles.get)
    masGoles = totalGoles[equipoMaxGoles]
    print (f'El equipo con más goles es {equipoMaxGoles} con {masGoles} goles')

    equipoMinGoles = min(totalGoles, key=totalGoles.get)
    minGoles = totalGoles[equipoMinGoles]
    print (f'El equipo con menos goles es {equipoMinGoles} con {minGoles} goles')

def estadisticasjugador (lIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    faltasPorJugador = {}

    for equipo, datosEquipo in ligaBetplay.items():
        if ('Jugadores' in datosEquipo) and isinstance(datosEquipo['Jugadores'],dict):
            for nomJugador, jugador in datosEquipo['Jugadores'].items():
                numFaltas = jugador.get ('Faltas Cometidas', 0)
                if (nomJugador not in faltasPorJugador):
                    faltasPorJugador[nomJugador] = 0
                faltasPorJugador[nomJugador] += numFaltas
 
    print ("   FALTAS POR JUGADOR    ")
    for nomJugador, numFaltas in faltasPorJugador.items():
        print (f'{nomJugador}: {numFaltas}')
    guardarLiga(ligaBetplay,LIGA_BASE)
        
    if (faltasPorJugador):
        jugadorMasFaltas = max(faltasPorJugador, key=faltasPorJugador.get)
        faltasCometidas = faltasPorJugador[nomJugador]
        print (f'El jugador con más faltas es {jugadorMasFaltas} con {faltasCometidas} faltas')
    else: 
        print ("No se han registrado faltas en el torneo")

  


    