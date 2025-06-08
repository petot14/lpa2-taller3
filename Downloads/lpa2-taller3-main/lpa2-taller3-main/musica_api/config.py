"""
Módulo de configuración de la aplicación.
Define las diferentes configuraciones para entornos de desarrollo, pruebas y producción.
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env si existe
load_dotenv()

class Config:
    """Configuración base para la aplicación."""
    # Configuración de la base de datos
    # FIXME: la ubicación de la base de datos no funciona
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///instance/musica.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() == 'true'
    
    # Configuración de la API
    API_TITLE = os.getenv('API_TITLE', 'API de Música')
    API_VERSION = os.getenv('API_VERSION', '1.0')
    
    # Otras configuraciones generales
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-predeterminada')

class DevelopmentConfig(Config):
    """Configuración para entorno de desarrollo."""
    DEBUG = True
    
class TestingConfig(Config):
    """Configuración para entorno de pruebas."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///musica_test.db'
    
class ProductionConfig(Config):
    """Configuración para entorno de producción."""
    DEBUG = False
    # En producción, asegurarse de tener una clave secreta fuerte
    SECRET_KEY = os.getenv('SECRET_KEY')
    
# Mapeo de configuraciones por entorno
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Obtener configuración según el entorno
def get_config(config_name=None):
    """
    Obtiene la configuración según el entorno especificado en las variables de entorno o parámetro.
    
    Args:
        config_name (str): Nombre de configuración ('development', 'testing', 'production', 'default').
                           Si es None, usa la variable FLASK_ENV o 'development' por defecto.
    
    Returns:
        object: Clase de configuración según el entorno.
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    return config_by_name.get(config_name, config_by_name['default'])

