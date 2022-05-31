
from asyncore import read
import csv
with open('data/Listado-Instituciones-Educativas.csv') as archivo:
    # Separar cada columna del CSV
    read = csv.reader(archivo, delimiter='|')
    # Salto del encabezado del csv
    # Lista que guardara cada linea del CSV
    listaP = []
    print(archivo)        