from modelos.entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self._bodega = bodega
        self._cepas = cepas
        self._partidas = partidas

    def obtenerBodega(self):
        from vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self._bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self._cepas]

    def obtenerPartidas(self):
        return self._partidas

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "partidas": self.obtenerPartidas()
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()

