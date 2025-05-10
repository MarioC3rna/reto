"""
Programa principal para detectar personas en una imagen usando Roboflow
"""
import cv2
from camera import capturar_imagen, mostrar_imagen
from detector import procesar_deteccion

def main():
    print("=== Detector de Personas con Roboflow ===")
    print("Presiona ENTER para capturar una foto...")
    input()
    
    # Capturar imagen desde la cámara
    print("Capturando imagen...")
    imagen, path_imagen = capturar_imagen()
    
    if imagen is None:
        print("Error al capturar la imagen.")
        return
    
    print("Imagen capturada exitosamente.")
    
    # Mostrar la imagen capturada
    print("Mostrando imagen capturada (presiona cualquier tecla para continuar)...")
    mostrar_imagen(imagen, "Imagen Capturada")
    
    # Detectar personas
    print("Analizando imagen...")
    resultado = procesar_deteccion(path_imagen)
    
    # Mostrar resultado
    print("\n" + "="*30)
    print(resultado)
    print("="*30)

if __name__ == "__main__":
    main()