Integrantes
1.	Mario Fernando Cerna Najera (creación del prompt, esctrutura del proyecto en entorno)
2.	Blanky Marisol Lopez Marroquin (Configuración de roboflow y obteción de api’s) 
3.	Naser Daniel Martinez Morales (interacción con modelo IA, ayuda a esctruturar 

El proyecto=
IA a utilizar:
Claude
API a utilizar:
Roboflow, tomó esta decisión por la razón que fue la que más se nos aconsejó luego de este prompt:
PROMPT PARA ELEGIR API
te comento, estoy realizando un proyecto en pyton en el por medio de mi Cámara web de mi laptop deberá identificar si hay una persona y cuantas personas hay.
para eso nos recomendaron las siguientes api’s para la detección de personas y objetos: 
•	Clarifai  
•	Roboflow  
•	Google Cloud Vision API  
•	Azure Computer Vision  
•	Hugging Face
Necesito que me ayudes a identificar cuál de las api’s es la más recomendada para 
mi proyecto y por qué debo usar esa.

# 👁‍🗨 Proyecto Python + Roboflow: ¡Detectando Personas en Tiempo Real!

## 🧠 ¿De qué trata este proyecto?

Este proyecto fue una emocionante combinación de *inteligencia artificial, **visión por computadora* y *Python, donde creamos una aplicación capaz de **detectar personas en tiempo real usando la cámara web de una laptop. Gracias al poder de la **API de Roboflow*, nuestro programa puede reconocer personas en imágenes capturadas al instante, de forma rápida y precisa.

¿El resultado? Un sistema sencillo, funcional y eficiente para detección de personas, ideal como base para futuros proyectos de seguridad, conteo de personas, o automatización de tareas visuales.

---

## 🛠 ¿Cómo funciona?

1. *Encendemos la cámara web* de la laptop y capturamos una imagen.
2. *Enviamos esa imagen a la API de Roboflow*, que analiza lo que hay en ella.
3. *Recibimos un resultado en JSON*, donde se indican los objetos detectados.
4. *Contamos cuántas personas fueron reconocidas*, según el modelo de Roboflow.

---

## 🔧 Tecnologías y herramientas

- *Python* 🐍
- *OpenCV* para el acceso a la cámara (cv2)
- *Requests* para comunicarse con la API
- *Roboflow API* para la detección de objetos

---

## ⚙ Configuración básica del sistema

```python
ROBOFLOW_API_KEY = "AbCdEfGhIjKlMnOpQrStUvWxYz"  # Clave de tu cuenta Roboflow
ROBOFLOW_MODEL_ID = "coco/3"                      # Modelo preentrenado para detectar personas
ROBOFLOW_API_URL = f"https://detect.roboflow.com/{ROBOFLOW_MODEL_ID}"
CONFIDENCE_THRESHOLD = 0.4                        # Umbral de confianza
CAMERA_INDEX = 0                                  # Índice de la webcam