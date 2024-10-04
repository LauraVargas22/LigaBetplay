'''
Funcion para implementar en el proyecto Liga Betplay 
para el registro del cuerpo técnico.
By Mariana Vargas
'''
import os
import json
import modulos.mensajes as m
import modulos.salir as s
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


def addPlantelCT (LIGA_BASE:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    nomEquipo = input ('Ingrese el nombre del equipo a buscar: ').capitalize()
    if (len(ligaBetplay)> 0):
        for equipo in ligaBetplay:
            if (nomEquipo in equipo):
                addCuerpoTecnico (LIGA_BASE,nomEquipo)
                break
        else:
            print (m.msgEquipo)
            os.system ('pause')
    else: 
        os.system ('cls')
        print (m.msgAdvice)
        os.system ('pause')

def addCuerpoTecnico (LIGA_BASE:str,nomEquipo:str):
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    isaddCT = True
    while (isaddCT):
        os.system ('cls')
        nombreCT = input ("Ingrese el nombre del miembro del Cuerpo Técnico: ").capitalize()

        if 'Tecnicos' not in ligaBetplay[nomEquipo]:
            ligaBetplay[nomEquipo]['Tecnicos'] = {}

        if nombreCT in ligaBetplay[nomEquipo]['Tecnicos']:
            print ("El nombre ingresado ya se encuentra registrado")
            os.system ('pause')
        else:
            cargo = input(f'Ingrese el cargo de {nombreCT} en el cuerpo técnico: ')
            Tecnicos = {
                'Nombre': nombreCT,
                'Cargo': cargo
            }
            ligaBetplay[nomEquipo]['Tecnicos'][nombreCT] = Tecnicos
            guardarLiga(ligaBetplay,LIGA_BASE)
            print (f'El miembro del cuerpo técnico {nombreCT} está registrado en el equipo {nomEquipo}')

            isaddCT = s.validateAnswer('¿Desea agregar otro integrante S(Si) N(No)?')

def mostrarCT (LIGA_BASE:str):
    print("CUERPO TÉCNICO REGISTRADOS:")
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    if (len(ligaBetplay)== 0):
        print (m.msgAdvice)
        return
    
    for nomEquipo, datosEquipo in ligaBetplay.items():
        print (f"Equipo: {nomEquipo}")
        if 'Tecnicos' in datosEquipo and datosEquipo['Tecnicos']:
            for nombreCT, detallesCT in datosEquipo['Tecnicos'].items():
                cargo = detallesCT.get ('Cargo', '')
                print (f' -Nombre: {nombreCT}, Cargo: {cargo}')
        else:
            print ("El equipo no tiene cuerpo técnico registrado")

def removeCT (LIGA_BASE):
    os.system ('cls')
    print ("EQUIPOS REGISTRADOS")
    ligaBetplay = cargarLigaJson(LIGA_BASE)
    equipos = re.equiposRegistrados (LIGA_BASE)
    print (equipos)
    equipo = input ('Ingrese el equipo a eliminar jugadores: ').capitalize()
    if (equipo in ligaBetplay):
        tecnicoEliminar = mostrarCT(LIGA_BASE)
        print (tecnicoEliminar)
        tecnicoEliminar = input ('¿Cuál integrante desea eliminar?_').capitalize()
        if tecnicoEliminar in ligaBetplay[equipo]['Tecnicos']:
            if s.validateAnswer (m.msgDelete):
                ligaBetplay[equipo]['Tecnicos'].pop(tecnicoEliminar)
                print (f'Integrante cuerpo técnico {tecnicoEliminar} ha sido eliminado')
                guardarLiga(ligaBetplay,LIGA_BASE)
            else:
                print (m.msgCancel)
        else:
            print (m.msgJugador)
    else:
        print (m.msgEquipo)


