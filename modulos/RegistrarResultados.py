'''
Funcion para implementar en el proyecto Liga Betplay 
para registrar los resultados de los partidos con sus respectivos puntos.
By Mariana Vargas
'''
import os
import json
import modulos.ProgramarPartidos as pp

def cargarLigaJson (LIGA_BASE:str) -> dict:
    if os.path.isfile(LIGA_BASE):
        with open(LIGA_BASE,'r') as f:
            return json.load(f)
    else:
        return{}
    
def guardarLiga (ligaBetplay:dict, LIGA_BASE:str):
    with open(LIGA_BASE,'w') as f:
        json.dump(ligaBetplay,f,indent=4)

def registrarresultados (LIGA_BASE):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    partidos = pp.mostrarPartidos (LIGA_BASE)
    print (partidos)
    equipoLocal = input("Ingrese el nombre del equipo local: ").capitalize()
    equipoVisitante = input("Ingrese el nombre del equipo visitante: ").capitalize()

    if (equipoLocal in ligaBetplay) and (equipoVisitante in ligaBetplay):
        fechaPartido = input ('Ingrese la fecha del partido (dd/mm/aaaa): ')
        if ('Partidos' in ligaBetplay[equipoLocal]) and (fechaPartido in ligaBetplay[equipoLocal]['Partidos']):
            partido = ligaBetplay[equipoLocal]['Partidos'][fechaPartido]
            #Goles Equipo Local
            golesEquipoLocal = int(input("Ingrese goles del equipo local: "))
            jugadoresEquipoLocal = ligaBetplay[equipoLocal].get('Jugadores', {})

            for i in range(golesEquipoLocal):
                nomJugador = input(f"Ingrese el nombre del jugador que anotó el gol {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoLocal):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoLocal}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que anotó el gol {i + 1}: ').capitalize()
                if 'Goles Anotados' not in jugadoresEquipoLocal[nomJugador]:
                    jugadoresEquipoLocal[nomJugador]['Goles Anotados'] = 0

                jugadoresEquipoLocal[nomJugador]['Goles Anotados'] += 1
                print (f'El gol fue registrado al jugador {nomJugador}')
            ligaBetplay[equipoLocal]['Partidos'][fechaPartido]['Goles Equipo Local'] = golesEquipoLocal
            partido['Goles Equipo Local'] = golesEquipoLocal
            #Tarjetas Amarillas Equipo Local
            tarjetasAmarillasL = int(input("Ingrese el número de tarjetas amarillas obtenidas: "))
            jugadoresEquipoLocal = ligaBetplay[equipoLocal].get('Jugadores', {})

            for i in range(tarjetasAmarillasL):
                nomJugador = input(f"Ingrese el nombre del jugador que obtuvo la tajeta amarilla {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoLocal):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoLocal}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que obtuvo la tarjeta amarilla{i + 1}: ').capitalize()

                if 'Tarjeta Amarilla' not in jugadoresEquipoLocal[nomJugador]:
                    jugadoresEquipoLocal[nomJugador]['Tarjeta Amarilla'] = 0
                
                jugadoresEquipoLocal[nomJugador]['Tarjeta Amarilla'] += 1
                print (f'La tarjeta amarilla fue registrada al jugador {nomJugador}')
            guardarLiga(ligaBetplay,LIGA_BASE)
            #Tarjetas Rojas Equipo Local
            tarjetasRojasL = int(input("Ingrese el número de tarjetas rojas obtenidas: "))
            jugadoresEquipoLocal = ligaBetplay[equipoLocal].get('Jugadores', {})

            for i in range(tarjetasRojasL):
                nomJugador = input(f"Ingrese el nombre del jugador que obtuvo la tajeta roja {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoLocal):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoLocal}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que obtuvo la tarjeta roja{i + 1}: ').capitalize()
                if 'Tarjeta Roja' not in jugadoresEquipoLocal[nomJugador]:
                    jugadoresEquipoLocal[nomJugador]['Tarjeta Roja'] = 0
                
                jugadoresEquipoLocal[nomJugador]['Tarjeta Roja'] += 1
                print (f'La tarjeta roja fue registrada al jugador {nomJugador}')
            #Faltas Equipo Local
            numFaltas = int(input("Ingrese el número de faltas cometidas: "))
            jugadoresEquipoLocal = ligaBetplay[equipoLocal].get('Jugadores', {})
            for i in range(numFaltas):
                nomJugador = input(f"Ingrese el nombre del jugador que cometió la falta {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoLocal):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoLocal}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que cometió la falta{i + 1}: ').capitalize()
                if 'Faltas Cometidas' not in jugadoresEquipoLocal[nomJugador]:
                    jugadoresEquipoLocal[nomJugador]['Faltas Cometidas'] = 0

                jugadoresEquipoLocal[nomJugador]['Faltas Cometidas'] += 1
                print (f'La falta fue registrada al jugador {nomJugador}')
            
            #Goles Equipo Visitante
            golesEquipoVisitante = int(input("Ingrese goles del equipo visitante: "))
            jugadoresEquipoVisitante = ligaBetplay[equipoVisitante].get('Jugadores', {})

            for i in range(golesEquipoVisitante):
                nomJugador = input(f'Ingrese el nombre del jugador que anotó el gol {i + 1}: ')

                while (nomJugador not in jugadoresEquipoVisitante):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoVisitante}')
                    nomJugador = input (f'Ingrese nuevamente el nombre del jugador que  anotó el gol {i+1}: ').capitalize()
                if 'Goles Anotados' not in jugadoresEquipoVisitante[nomJugador]:
                    jugadoresEquipoVisitante[nomJugador]['Goles Anotados'] = 0
                jugadoresEquipoVisitante[nomJugador]['Goles Anotados'] +=1
                print (f'El gol fue registrado al jugador {nomJugador}')

            partido['Goles Equipo Visitante'] = golesEquipoVisitante

            #Tarjetas Amarillas Equipo Visitante
            tarjetasAmarillasV = int(input("Ingrese el número de tarjetas amarillas obtenidas: "))
            jugadoresEquipoVisitante = ligaBetplay[equipoVisitante].get('Jugadores', {})

            for i in range(tarjetasAmarillasV):
                nomJugador = input(f"Ingrese el nombre del jugador que obtuvo la tajeta amarilla {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoVisitante):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoVisitante}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que obtuvo la tarjeta amarilla{i + 1}: ').capitalize()
                if 'Tarjeta Amarilla' not in jugadoresEquipoVisitante[nomJugador]:
                    jugadoresEquipoVisitante[nomJugador]['Tarjeta Amarilla'] = 0
                jugadoresEquipoVisitante[nomJugador]['Tarjeta Amarilla'] += 1
            print (f'La tarjeta amarilla fue registrada al jugador {nomJugador}')

            #Tarjetas Rojas equipo Visitante
            tarjetasRojasV = int(input("Ingrese el número de tarjetas rojas obtenidas: "))
            jugadoresEquipoVisitante = ligaBetplay[equipoVisitante].get('Jugadores', {})
            for i in range(tarjetasRojasV):
                nomJugador = input(f"Ingrese el nombre del jugador que obtuvo la tajeta roja {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoVisitante):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoVisitante}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que obtuvo la tarjeta roja{i + 1}: ').capitalize()
                if 'Tarjeta Roja' not in jugadoresEquipoVisitante[nomJugador]:
                    jugadoresEquipoVisitante[nomJugador]['Tarjeta Roja'] = 0
                jugadoresEquipoVisitante[nomJugador]['Tarjeta Roja'] += 1
                
                print (f'La tarjeta roja fue registrada al jugador {nomJugador}')
            #Faltas equipo Visitante
            numFaltas = int(input("Ingrese el número de faltas cometidas: "))
            jugadoresEquipoLocal = ligaBetplay[equipoVisitante].get('Jugadores', {})
            for i in range(numFaltas):
                nomJugador = input(f"Ingrese el nombre del jugador que cometió la falta {i+ 1}: ").capitalize()

                while (nomJugador not in jugadoresEquipoVisitante):
                    print (f'El jugador {nomJugador} no está registrado en el equipo {equipoVisitante}')
                    nomJugador = input(f'Ingrese nuevamente el nombre del jugador que cometió la falta{i + 1}: ').capitalize()
                if 'Faltas Cometidas' not in jugadoresEquipoVisitante[nomJugador]:
                    jugadoresEquipoVisitante[nomJugador]['Faltas Cometidas'] = 0
                jugadoresEquipoVisitante[nomJugador]['Faltas Cometidas'] += 1
                
                print (f'La falta fue registrada al jugador {nomJugador}')
                    
            print (F'El resultado del partido fue {equipoLocal}:{golesEquipoLocal} y {equipoVisitante}:{golesEquipoVisitante}')
        else:
            print ("No hay partidos programados en la fecha ingresada")
    else:
        print ("Error en los equipos ingresados, revise si están registrados.")
    guardarLiga(ligaBetplay,LIGA_BASE)

def mostrarResultados (lIGA_BASE:str):
    ligaBetplay = cargarLigaJson(lIGA_BASE)
    print ("RESULTADOS PARTIDOS")

    isFoundResultados = False
    for equipoLocal, datosEquipo in ligaBetplay.items():
        if 'Partidos' in datosEquipo and isinstance(datosEquipo['Partidos'],dict):
            for fechaPartido, partido in datosEquipo['Partidos'].items():
                if (partido['Goles Equipo Local'] is not None) and (partido['Goles Equipo Visitante'] is not None):
                    isFoundResultados = True
                    equipoVisitante = partido['Equipo Visitante']
                    golesEquipoLocal = partido['Goles Equipo Local']
                    golesEquipoVisitante = partido['Goles Equipo Visitante']
                    print (f'Fecha Partido {fechaPartido} entre {equipoLocal} y {equipoVisitante} \n {equipoLocal}:{golesEquipoLocal} \n {equipoVisitante}:{golesEquipoVisitante} ')
                    
    if not isFoundResultados:
        print ("No hay resultados registrados")
                
 