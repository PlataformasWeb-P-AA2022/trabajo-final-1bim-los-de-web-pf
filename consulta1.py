from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import *
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
# Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553
establecimientos = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Parroquia.codigo == 110553).all()
print("Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553")
for e in establecimientos:
    print(e, "\n")

# Todos los establecimientos de la provincia del Oro.
establecimientos = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Provincia.provincia == 'EL ORO').all()
print("Todos los establecimientos de la provincia de Loja.")
for e in establecimientos:
    print(e, "\n")

# Todos los establecimientos del cantón de Portovelo.
establecimientos = session.query(Establecimiento).join(Parroquia, Canton).filter(Canton.canton == 'PORTOVELO').all()
print("Todos los establecimientos del cantón de Loja.")
for e in establecimientos:
    print(e, "\n")

# Todos los establecimientos del cantón de Zamora.
establecimientos = session.query(Establecimiento).join(Parroquia, Canton).filter(Canton.canton == 'ZAMORA').all()
print("Todos los establecimientos del cantón de Loja.")
for e in establecimientos:
    print(e, "\n")