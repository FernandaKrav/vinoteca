from flask_restful import Resource, reqparse
from app.models.models import Bodega, Cepa, Vino
from vinoteca import Vinoteca

from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class RecursoBodega(Resource):
    def get(self, id):
        bodega = vinoteca.Vinoteca.buscarBodega(id)
        if isinstance(bodega, Bodega):
            return bodega.convertirAJSONFull(), 200  
        else:
            return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):
    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            bodegas = vinoteca.Vinoteca.obtenerBodegas(orden=orden, reverso=reverso == "si")
        else:
            bodegas = vinoteca.Vinoteca.obtenerBodegas()
        return [bodega.convertirAJSON() for bodega in bodegas], 200  


class RecursoCepa(Resource):
    def get(self, id):
        cepa = vinoteca.Vinoteca.buscarCepa(id)
        if isinstance(cepa, Cepa):
            return cepa.convertirAJSONFull(), 200  
        else:
            return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):
    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            cepas = vinoteca.Vinoteca.obtenerCepas(orden=orden, reverso=reverso == "si")
        else:
            cepas = vinoteca.Vinoteca.obtenerCepas()
        return [cepa.convertirAJSONFull() for cepa in cepas], 200  


class RecursoVino(Resource):
    def get(self, id):
        vino = vinoteca.Vinoteca.buscarVino(id)
        if isinstance(vino, Vino):
            return vino.convertirAJSONFull(), 200  
        else:
            return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):
    def get(self):
        try:
            anio = request.args.get("anio")
            if anio:
                anio = int(anio)
            orden = request.args.get("orden")
            if orden and orden not in ["nombre", "bodega", "cepas"]:
                return {"error": "Parámetro de ordenamiento inválido"}, 400

            reverso = request.args.get("reverso")
            vinos = vinoteca.Vinoteca.obtenerVinos(anio, orden=orden, reverso=reverso == "si")
            return [vino.convertirAJSON() for vino in vinos], 200  
        except ValueError:
            return {"error": "El año debe ser un número válido"}, 400
