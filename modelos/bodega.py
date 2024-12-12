import json
from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        vinos = Vinoteca.obtenerVinos()
        return [vino for vino in vinos if vino.obtenerBodega().obtenerId() == self.obtenerId()]

    def obtenerCepas(self):
        vinos = self.obtenerVinos()
        cepas = set()
        for vino in vinos:
            cepas.update(vino.obtenerCepas())
        return list(cepas)

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "vinos": len(self.obtenerVinos())
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "vinos": [vino.obtenerNombre() for vino in self.obtenerVinos()]
        }
