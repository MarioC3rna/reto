import cv2
from config import CAMERA_INDEX

def capturar_imagen():
    """
    Captura una imagen desde la cámara web.
    
    Returns:
        tuple: (imagen, path_imagen) si la captura fue exitosa,
               (None, None) si hubo un error.
    """
    # Inicializar la cámara
    camara = cv2.VideoCapture(CAMERA_INDEX)
    
    if not camara.isOpened():
        print("Error: No se pudo abrir la cámara")
        return None, None
    
    # Capturar un frame
    ret, frame = camara.read()
    
    # Liberar la cámara
    camara.release()
    
    if ret:
        # Guardar la imagen temporalmente
        path_imagen = "captura_temporal.jpg"
        cv2.imwrite(path_imagen, frame)
        return frame, path_imagen
    else:
        print("Error: No se pudo capturar la imagen")
        return None, None

def mostrar_imagen(imagen, titulo="Imagen"):
    """
    Muestra una imagen en una ventana.
    
    Args:
        imagen: La imagen a mostrar
        titulo: Título de la ventana
    """
    cv2.imshow(titulo, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()