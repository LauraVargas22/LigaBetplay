'''
Funcion para implementar en el proyecto Liga Betplay 
se mostrarán las estadísticas del torneo. 
By Mariana Vargas Esto es una prueba
'''
#Importación
import os
import json
import modulos.mensajes as m
import modulos.RegistrarJugadores as rj
LIGA_BASE = None
#Implementación archivo JSON
def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
    
def guardarLiga (ligaBetplay:dict, LIGA_BASE:str):
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)

#Función para evaluar estadísticas del equipo
def estadisticaEquipo (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson (LIGA_BASE)
    totalGoles = {}
# Por cada equipo adquirir sus datos
    for equipoLocal, datosEquipo in ligaBetplay.items():
        if ('Partidos' in datosEquipo) and isinstance(datosEquipo['Partidos'],dict):
            for fechaPartido, partido in datosEquipo['Partidos'].items():
                if isinstance (partido,dict):
                    golesEquipoLocal = partido.get ('Goles Equipo Local', 0) #Obtener goles de equipo local
                    if (equipoLocal not in totalGoles):
                        totalGoles[equipoLocal] = 0
                    totalGoles[equipoLocal] += golesEquipoLocal #Sumar los goles del equipo visitante

                    equipoVisitante = partido.get('Equipo Visitante', '') 
                    golesEquipoVisitante = partido.get('Goles Equipo Visitante', 0) #Obtener goles equipo visitante
                    if (equipoVisitante not in totalGoles):
                        totalGoles[equipoVisitante] = 0
                    totalGoles[equipoVisitante] += golesEquipoVisitante #Sumar los goles del equipo visitante
    #Tomar goles por cada equipo
    print ("     GOLES POR EQUIPO      ")
    for equipo, goles in totalGoles.items():
        print (f'{equipo}: {goles} goles') #Imprimir por cada equipo los goles

    #Evaluar el equipo con mayor cantidad de goles
    equipoMaxGoles = max(totalGoles, key=totalGoles.get)
    masGoles = totalGoles[equipoMaxGoles]
    print (f'El equipo con más goles es {equipoMaxGoles} con {masGoles} goles')
    #Evaluar el equipo con menor cantidad de goles
    equipoMinGoles = min(totalGoles, key=totalGoles.get)
    minGoles = totalGoles[equipoMinGoles]
    print (f'El equipo con menos goles es {equipoMinGoles} con {minGoles} goles')

#Función para evaluar estadísticas por jugador
def estadisticasjugador (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    faltasPorJugador = {}
    # Por cada equipo adquirir sus datos
    for equipo, datosEquipo in ligaBetplay.items():
        if ('Jugadores' in datosEquipo) and isinstance(datosEquipo['Jugadores'],dict):
            #Por cada jugador adquirir sus datos
            for nomJugador, jugador in datosEquipo['Jugadores'].items():
                if isinstance (jugador,dict):
                    numFaltas = jugador.get ('Faltas Cometidas', 0)
                    if (nomJugador not in faltasPorJugador):
                        faltasPorJugador[nomJugador] = 0
                    faltasPorJugador[nomJugador] += numFaltas #Sumar faltas cometidas a cada jugador
    
    print ("   FALTAS POR JUGADOR    ")
    #Por cada jugador evaluar el nùmero de faltas cometidas en el torneo
    for nomJugador, numFaltas in faltasPorJugador.items():
        print (f'{nomJugador}: {numFaltas}')
    guardarLiga(ligaBetplay,LIGA_BASE)
    #Si el jugador tiene faltas    
    if (faltasPorJugador):
        #Evaluar el jugador con mayor cantidad de faltas
        jugadorMasFaltas = max(faltasPorJugador, key=faltasPorJugador.get)
        faltasCometidas = faltasPorJugador[nomJugador]
        print (f'El jugador con más faltas es {jugadorMasFaltas} con {faltasCometidas} faltas')
    #Si el jugador NO tiene faltas 
    else: 
        print ("No se han registrado faltas en el torneo")

    tarAmarillasPorJugador = {}
    #Por cada equipo evaluar sus datos
    for equipo, datosEquipo in ligaBetplay.items():
        if ('Jugadores' in datosEquipo) and isinstance(datosEquipo['Jugadores'],dict):
            #Por cada jugador evaluar las tarjetas amarillas
            for nomJugador, jugador in datosEquipo['Jugadores'].items():
                if isinstance (jugador,dict):
                    tarAmarilla = jugador.get ('Tarjeta Amarilla', 0)
                    if (nomJugador not in tarAmarillasPorJugador):
                        tarAmarillasPorJugador[nomJugador] = 0
                    tarAmarillasPorJugador[nomJugador] += tarAmarilla #Sumar tarjetas amarillas a cada jugador
 
    print ("   TARJETAS AMARILLAS POR JUGADOR    ")
    #Por cada jugador evaluar el nùmero de tarjetas amarillas en el torneo
    for nomJugador, tarAmarilla in tarAmarillasPorJugador.items():
        print (f'{nomJugador}: {tarAmarilla}')
    #Si el jugador tiene tarjetas amarillas
    if (tarAmarillasPorJugador):
        #Evaluar el jugador con mayor cantidad de tarjetas amarillas
        jugadorMasAmarillas = max(tarAmarillasPorJugador, key=tarAmarillasPorJugador.get)
        tarAmarillaObtenidas = tarAmarillasPorJugador[jugadorMasAmarillas]
        print (f'El jugador con más tajetas amarillas es {jugadorMasAmarillas} con {tarAmarillaObtenidas}.')
    #Si el jugador NO tiene tarjetas amarillas
    else: 
        print ("No se han registrado tarjetas amarillas en el torneo")
    guardarLiga(ligaBetplay,LIGA_BASE)


  


    