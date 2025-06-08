"""
Script principal para ejecutar la aplicación Flask.
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env si existe
load_dotenv()

from musica_api import create_app  # <-- Importa después de cargar el .env

# Crear la aplicación con configuración según el entorno
app = create_app()

if __name__ == "__main__":
    # Obtener puerto del ambiente o usar 5000 por defecto
    port = int(os.getenv("PORT", 5000))
    
    # Determinar si se debe usar modo debug
    debug = os.getenv("FLASK_ENV", "development") == "development"
    
    # Ejecutar aplicación
    app.run(host="0.0.0.0", port=port, debug=debug)
