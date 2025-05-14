"""
Módulo principal de inicialización de la aplicación Flask.
Configura la aplicación, las extensiones y registra los namespaces.
"""
from flask import Flask
from .extensions import api, db
from .resources import ns
from .config import get_config

def create_app(config_name=None):
    """
    Crea y configura la aplicación Flask con sus extensiones.
    
    Args:
        config_name (str): Nombre de la configuración a utilizar (default, development, testing, production).
                          Si es None, se utiliza la configuración según las variables de entorno.
    
    Returns:
        Flask: La aplicación Flask configurada y lista para usar.
    """
    # TODO: Crear la app Flask
    
    # Aplicar configuración según entorno
    # FIXME: Debe usar el método para leer la configuración
    config_obj = ""
    app.config.from_object(config_obj)
    
    # Inicialización de extensiones
    # TODO: las variables 'api' y 'db'
    
    # Registro de namespaces
    api.add_namespace(ns)
    
    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    return app

