from lib2to3.pgen2.token import LPAR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos

with open('data/Listado-Instituciones-Educativas.csv') as File:
    # Separar cada columna del CSV
    read = csv.reader(File, delimiter='|')
    # Salto del encabezado del csv
    next(read)
    # Lista que guardara cada linea del CSV
    listaP = []
    #Ciclo para recorrer cada linea
    for x in read:
        #Almacenamiento de las columnas que nos sirven (Codigo y Provincia)
        auxProvincia = x[2] + "|" + x[3]
        # Agregar la variable anterior a la lista
        listaP.append(auxProvincia)
    # Eliminar duplicados de la lista
    listaP = list(set(listaP))
    # Ciclo para agregar cada provincia
    for x in listaP:
        # Creacion de cada objeto de tipo provincia
        prov = Provincia(codigo = x.split("|")[0], provincia = x.split("|")[1])
        # Agregar a la base la provincia
        session.add(prov)
# Guardar los cambios 
session.commit()