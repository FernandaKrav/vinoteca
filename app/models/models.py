from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Bodega(Base):
    __tablename__ = 'bodegas'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    region = Column(String(100))
    pais = Column(String(50))
    activa = Column(Boolean, default=True)
    vinos = relationship("Vino", back_populates="bodega")

class Cepa(Base):
    __tablename__ = 'cepas'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))
    tiempo_maduracion = Column(Integer)
    vinos = relationship("Vino", back_populates="cepa")

class Vino(Base):
    __tablename__ = 'vinos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    anio = Column(Integer)
    precio = Column(Float)
    stock = Column(Integer)
    bodega_id = Column(Integer, ForeignKey('bodegas.id'))
    cepa_id = Column(Integer, ForeignKey('cepas.id'))
    
    bodega = relationship("Bodega", back_populates="vinos")
    cepa = relationship("Cepa", back_populates="vinos")