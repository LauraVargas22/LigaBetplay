'''
Proyecto Liga Betplay por medio de este programa se permitirá al usuario
registrar equipos del campeonato.
By Mariana Vargas 
'''

if (__name__=='__main__'):
    #Diccionario principal
    LIGA_BASE = 'data/ligaBetplay.json'
    #Modulos
    import os 
    import modulos.menus as m
    import modulos.mensajes as msg
    import modulos.salir as s
    import modulos.RegistrarEquipo as re
    import modulos.RegistrarJugadores as rj
    import modulos.RegistrarCuerpoTecnico as rct
    import modulos.ProgramarPartidos as pp
    import modulos.RegistrarResultados as rr
    import modulos.Estadísticas as es
    import modulos.customs as c

    isActive = True
    while (isActive):
        try:
            c.borrar_pantalla()
            print (msg.title)
            print (m.menuPrincipal)
            opcMenuP = int(input('Seleccione:_'))

            match opcMenuP:
                case 1:
                    print (msg.subtitle1)
                    isAddEquipo = True
                    while (isAddEquipo):
                        try:
                            c.borrar_pantalla() #os.system.('cls')
                            print (m.menu1)
                            opcMenu1 = int(input("Seleccione:_"))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausar_pantalla() #os.system('pause')
                            continue
                        else:
                            match opcMenu1:
                                case 1:
                                    re.addEquipo(LIGA_BASE)
                                    c.pausar_pantalla()
                                case 2:
                                    re.equiposRegistrados (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 3:
                                    re.removeEquipo (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 4:
                                    isAddEquipo = s.validateData(msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)
                                    c.pausar_pantalla()
                case 2:
                    print (msg.subtitle2)
                    isAddPlantel = True
                    while (isAddPlantel):
                        try:
                            c.borrar_pantalla()
                            print (m.menu2)
                            opcMenu2 = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausar_pantalla()
                            continue
                        else:
                            match opcMenu2:
                                case 1:
                                    isAddJugadores = True
                                    while (isAddJugadores):
                                        try:
                                            c.borrar_pantalla()
                                            print (m.menu2a)
                                            opcMenu2a = int (input('Seleccione:_'))
                                        except ValueError:
                                            print (msg.msgExcept)
                                            c.pausar_pantalla()
                                            continue
                                        else:
                                            match opcMenu2a:
                                                case 1:
                                                    rj.addPlantel (LIGA_BASE)
                                                    c.pausar_pantalla()
                                                case 2:
                                                   rj.jugadoresRegistrados (LIGA_BASE)
                                                   c.pausar_pantalla()
                                                case 3:
                                                    rj.removeJugadores (LIGA_BASE)
                                                    c.pausar_pantalla()
                                                case 4:
                                                    isAddJugadores = s.validateData (msg.msgRegresar)
                                                case _:
                                                    print (msg.msgCase)
                                case 2:
                                    isAddCT = True
                                    while (isAddCT):
                                        try:
                                            c.borrar_pantalla()
                                            print (m.menu2b)
                                            opcMenu2b = int (input('Seleccione:_'))
                                        except ValueError:
                                            print (msg.msgExcept)
                                            c.pausar_pantalla()
                                            continue
                                        else:
                                            match opcMenu2b:
                                                case 1:
                                                    rct.addPlantelCT (LIGA_BASE)
                                                    c.pausar_pantalla()
                                                case 2:
                                                   rct.mostrarCT (LIGA_BASE)
                                                   c.pausar_pantalla()
                                                case 3:
                                                    rct.removeCT (LIGA_BASE)
                                                    c.pausar_pantalla()
                                                case 4:
                                                    isAddCT = s.validateData (msg.msgRegresar)
                                                case _:
                                                    print (msg.msgCase)
                                case 3: 
                                    isAddPlantel = s.validateData (msg.msgRegresar)
                                case _:
                                    print  (msg.msgCase)
                                    c.pausar_pantalla()
                case 3:
                    print (msg.subtitle3)
                    isAddPartido = True
                    while (isAddPartido):
                        try:
                            c.borrar_pantalla()
                            print (m.menu3)
                            opcMenu3 = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausar_pantalla()
                            continue
                        else:
                            match opcMenu3:
                                case 1:
                                    pp.addPartido(LIGA_BASE)
                                    c.pausar_pantalla()
                                case 2:
                                    pp.mostrarPartidos (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 3:
                                    isAddPartido = s.validateData (msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)          
                case 4:
                    print (msg.subtitle4)
                    isAddResultados = True
                    while (isAddResultados):
                        try:
                            c.borrar_pantalla()
                            print (m.menu4)
                            opcMenu4 = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausar_pantalla()
                            continue
                        else:
                            match opcMenu4:
                                case 1:
                                    rr.registrarresultados (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 2:
                                    rr.mostrarResultados (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 3:
                                    isAddResultados = s.validateData (msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)
                                    c.pausar_pantalla()
                case 5:
                    print (msg.subtitle5)
                    isViewEstadísticas = True
                    while (isViewEstadísticas):
                        try:
                            c.borrar_pantalla()
                            print (m.menu5)
                            opcMenu5 = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausar_pantalla()
                            continue
                        else:
                            match opcMenu5:
                                case 1:
                                    es.estadisticaEquipo (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 2:
                                    es.estadisticasjugador (LIGA_BASE)
                                    c.pausar_pantalla()
                                case 3:
                                    isViewEstadísticas = s.validateData (msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)
                                    c.pausar_pantalla()
                case 6:
                    isActive = s.validateData(msg.msgInfo)
                case _:
                    print (msg.msgCase)
                    c.pausar_pantalla()

        except ValueError:
            print (msg.msgExcept)
            input ('Presione enter para continuar...')
            continue

