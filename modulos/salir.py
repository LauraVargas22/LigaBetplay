'''
Función para implementar en el proyecto Liga Betplay 
para la validación de opciones ingresadas por el usuario.
By Mariana Vargas 
'''
def validateData (message:str):
    global isAllow
    flagFunction = True
    opciones = ('N', 'S')
    accion = input (f'{message}').upper()
    if (accion not in opciones):
        print ('La opción ingresada no es válida.....')
        validateData ()
    elif (accion == 'N'):
        flagFunction = True
    elif ((accion) == 'S'):
        flagFunction = False
    return flagFunction

def validateAnswer (message:str):
    global isAllow
    flagFunction = True
    opciones = ('N', 'S')
    accion = input (f'{message}').upper()
    if (accion not in opciones):
        print ('La opción ingresada no es válida.....')
        validateData ()
    elif (accion == 'N'):
        flagFunction = False
    elif ((accion) == 'S'):
        flagFunction = True
    return flagFunction