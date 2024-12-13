# LIGA BETPLAY

## Descripción: 
Mediante este proyecto se hace uso Python, permitiendo al usuario realizar la simulación de un torneo registrando equipos, jugadores, programar partidos, registrar el resultado de cada uno de los partidos y así mismo visualizar algunas estadísticas en torno a los resultados obtenidos.

## Características:
### Menú Principal:
En el menú principal se encontrar las opciones básicas de funcionalidad, las cuales son:

**** MENÚ ****
    1. Equipos.
    2. Plantel.
    3. Programar Partidos.
    4. Registrar Resultado / Fecha.
    5. Estadísticas Torneo
    6. Salir

A cada una se puede acceder por medio del numeral en la consolo, lo cual le permite al usuario redirigirse a submenús de acuerdo a la selección.

### Equipos:
En este menú se permite al usuario registrar equipos, visualizar los equipos registrados y eliminar Equipos. Para la realización de cada una de las opciones se tiene en cuenta la información almacenada en el archivo JSON, la implementación de este se realiza de esta manera: 
```
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
```
### Plantel:
En segundo lugar, en el menú plantel se puede registrar tanto miembros del cuerpo técnico como jugadores con su dorsal y posición, almacenandose de igual manera en el archivo JSON, así mismo se puede visualizar jugadores y miembros del cuerpo técnico que se encuentran registrados o si se desea eliminar a algunos de ellos.

### Programar Partidos:
En el tercero se podrá pogramar partidos teniendo en cuenta los equipos que se encuentren registrados, de lo contrario no se podrá realizar la planeación del partido con su fecha, además se podrá ver partidos programados con información adicional como fecha, equipo visitante y local.

### Registrar Resultados:
En el registro de resultados se solicitará la fecha en la cual fue programado el partido para así registrar resultados, incluyendo faltas, tarjetas y número de goles, lo cual se podrá visualizar en otro menú.

### Estadísticas:
Por último lugar, de acuerdo a la información ingresada en los resultados el programa realiza algunos datos estadísticos con respecto a la misma, por un lado encontramos estadísticas por equipo en donde se puede observar el número de goles por equipo y haciendo uso de las funciones max() y min() se evalúa el equipo con mayor y menor cantidad de goles anotados.
Por otro lado, en las estadísticas por jugador se pueden observar las faltas y tarjetas amarillas cometidas por jugador, para así evaluar el jugador con más tarjetas amarillas.

En cada uno de los menús se le da la opción al usuario regresar al menú principal y en el caso del menú principal se le permite salir del programa.