from abc import ABC

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    def establecerNombre(self, nombre):
        self._nombre = nombre

    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre

    def __eq__(self, other):
        if isinstance(other, EntidadVineria):
            return self._id == other.obtenerId()
        return False

    def __hash__(self):
        return hash(self._id)
