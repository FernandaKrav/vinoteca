import json
from app.models.models import Bodega, Cepa, Vino

class Vinoteca:
    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        bodegas = cls.__bodegas[:]
        return cls.__ordenarBodegas(bodegas, orden, reverso)

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        cepas = cls.__cepas[:]
        return cls.__ordenarCepas(cepas, orden, reverso)

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.__vinos[:]
        vinos = cls.__filtrarVinosPorAnio(vinos, anio)
        return cls.__ordenarVinos(vinos, orden, reverso)

    @classmethod
    def buscarBodega(cls, id):
        return cls.__buscarPorId(cls.__bodegas, id)

    @classmethod
    def buscarCepa(cls, id):
        return cls.__buscarPorId(cls.__cepas, id)

    @classmethod
    def buscarVino(cls, id):
        return cls.__buscarPorId(cls.__vinos, id)

    @classmethod
    def __filtrarVinosPorAnio(cls, vinos, anio):
        if anio is not None:
            return [vino for vino in vinos if anio in vino.obtenerPartidas()]
        return vinos

    @classmethod
    def __ordenarBodegas(cls, bodegas, orden, reverso):
        if orden == "nombre":
            return sorted(bodegas, key=lambda x: x.obtenerNombre(), reverse=reverso)
        elif orden == "vinos":
            return sorted(bodegas, key=lambda x: len(x.obtenerVinos()), reverse=reverso)
        return bodegas

    @classmethod
    def __ordenarCepas(cls, cepas, orden, reverso):
        if orden == "nombre":
            return sorted(cepas, key=lambda x: x.obtenerNombre(), reverse=reverso)
        return cepas

    @classmethod
    def __ordenarVinos(cls, vinos, orden, reverso):
        if orden == "nombre":
            return sorted(vinos, key=lambda x: x.obtenerNombre(), reverse=reverso)
        elif orden == "bodega":
            return sorted(vinos, key=lambda x: x.obtenerBodega().obtenerNombre(), reverse=reverso)
        elif orden == "cepas":
            return sorted(vinos, key=lambda x: len(x.obtenerCepas()), reverse=reverso)
        return vinos

    @classmethod
    def __buscarPorId(cls, lista, id):
        for elemento in lista:
            if elemento.obtenerId() == id:
                return elemento
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls):
        try:
            with open(cls.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            raise Exception("No se encontró el archivo de datos vinoteca.json")
        except json.JSONDecodeError:
            raise Exception("El archivo vinoteca.json tiene un formato inválido")

    @classmethod
    def __convertirJsonAListas(cls, lista):
        from modelos.bodega import Bodega
        from modelos.cepa import Cepa
        from modelos.vino import Vino

        cls.__bodegas = [Bodega(b["id"], b["nombre"]) for b in lista["bodegas"]]
        cls.__cepas = [Cepa(c["id"], c["nombre"]) for c in lista["cepas"]]
        cls.__vinos = [
            Vino(v["id"], v["nombre"], v["bodega"], v["cepas"], v["partidas"])
            for v in lista["vinos"]
        ]
