import requests
from config import ROBOFLOW_API_KEY, ROBOFLOW_API_URL, CONFIDENCE_THRESHOLD

def detectar_personas(imagen_path):
    """
    Detecta personas en una imagen usando la API de Roboflow.
    
    Args:
        imagen_path: Ruta del archivo de imagen a analizar
        
    Returns:
        int: Número de personas detectadas
    """
    # Preparar la URL con la API key
    url = f"{ROBOFLOW_API_URL}?api_key={ROBOFLOW_API_KEY}"
    
    try:
        # Abrir y enviar la imagen
        with open(imagen_path, 'rb') as imagen_archivo:
            response = requests.post(url, files={"file": imagen_archivo})
        
        # Verificar si la petición fue exitosa
        if response.status_code != 200:
            print(f"Error en la API: {response.status_code}")
            return 0
        
        # Obtener los resultados
        resultado = response.json()
        
        # Contar las detecciones de personas
        personas_detectadas = 0
        for prediccion in resultado.get('predictions', []):
            # Verificar si es una persona y si supera el umbral de confianza
            if (prediccion.get('class') == 'person' and 
                prediccion.get('confidence', 0) >= CONFIDENCE_THRESHOLD):
                personas_detectadas += 1
        
        return personas_detectadas
        
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
        return 0

def procesar_deteccion(imagen_path):
    """
    Procesa la detección y devuelve información formateada.
    
    Args:
        imagen_path: Ruta de la imagen a procesar
        
    Returns:
        str: Mensaje con el resultado de la detección
    """
    num_personas = detectar_personas(imagen_path)
    
    if num_personas == 0:
        return "No se detectaron personas en la imagen."
    elif num_personas == 1:
        return "Se detectó 1 persona en la imagen."
    else:
        return f"Se detectaron {num_personas} personas en la imagen."