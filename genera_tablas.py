from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo = Column(String, primary_key=True)
    nombre = Column(String, nullable=false)
    nroDistrito = Column(String, nullable=false)
    sostenimiento = Column(String, nullable=false)
    tipo = Column(String, nullable=false)
    modalidad = Column(String, nullable=false)
    jornada = Column(String, nullable=false)
    acceso = Column(String, nullable=false)
    nroEstudiantes = Column(Integer, nullable=false)
    nroDocentes = Column(Integer, nullable=false)
    parroquia_id = Column(String, ForeignKey('parroquia.codigo'), primary_key=True)
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: nombre=%s - Numero de distrito=%s - Sostenimiento=%s - Tipo=%s - Modalidad=%s - Jornada=%s - Acceso=%s - Num. Estudiantes=%d - Num. Docenctes=%d"% (
                          self.nombre, 
                          self.nroDistrito,
                          self.sostenimiento,
                          self.tipo,
                          self.modalidad,
                          self.jornada,
                          self.acceso,
                          self.nroEstudiantes,
                          self.nroDocentes)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    codigo = Column(String, primary_key=True)
    parroquia = Column(String, nullable=False)
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    canton_id = Column(String, ForeignKey('canton.codigo'), primary_key=True)
    canton = relationship("Canton", back_populates="parroquias")

    def __repr__(self):
        return "Parroquia: codigo=%s - nombre=%s"%(
            self.codigo,
            self.parroquia
            )

class Canton(Base):
    __tablename__ = 'canton'
    codigo = Column(String, primary_key=True)
    canton = Column(String, nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    provincia_id = Column(String, ForeignKey('provincia.codigo'), primary_key=True)
    provincia = relationship("Provincia", back_populates="cantones")

    def __repr__(self):
        return "Canton: codigo=%s - nombre=%s"%(
            self.codigo,
            self.canton
            )


class Provincia(Base):
    __tablename__ = 'provincia'
    codigo = Column(String, primary_key=True)
    provincia = Column(String, nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigo=%s - nombre=%s"%(
            self.codigo,
            self.provincia
            )

Base.metadata.create_all(engine)
