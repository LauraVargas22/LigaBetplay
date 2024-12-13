import sys
import os
#Borrar pantalla de acuerdo al sistema operativo
def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")
#Pausar pantalla de acuerdo al sistema operativo
def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")