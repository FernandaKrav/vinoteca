from modelos.entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        vinos = Vinoteca.obtenerVinos()
        return [vino for vino in vinos if self in vino.obtenerCepas()]

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos())
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": [vino.obtenerNombre() for vino in self.obtenerVinos()]
        }
