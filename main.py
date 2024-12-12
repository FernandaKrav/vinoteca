
import tkinter as tk
import threading


from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine


from vinoteca import Vinoteca
from app.models.models import Base
from app.gui.gui import VinotecaGUI
from app.recursos.recursos import *  

def iniciar_flask():
    """Función para iniciar el servidor Flask en un hilo separado"""
    Vinoteca.inicializar()

    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    api = Api(app)
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    
    @app.route('/test')
    def test():
        return {"mensaje": "Prueba de caracteres: á, é, í, ó, ú, ñ"}

    app.run(debug=False)  

def iniciar_gui():
    """Función para iniciar la interfaz gráfica"""
    root = tk.Tk()
    app = VinotecaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    
    engine = create_engine('sqlite:///vinoteca.db')
    Base.metadata.create_all(engine)
    
    
    flask_thread = threading.Thread(target=iniciar_flask)
    flask_thread.daemon = True  
    flask_thread.start()
    
    
    iniciar_gui()
