## Deteccion de placas vehiculares usando OpenCV y EasyOCR

Este proyecto utiliza OpenCV y EasyOCR para detectar las letras de fotos de placas vehiculares

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install opencv-python easyocr
```

## Archivos a colocar:

```bash
imagen1= "placa_q.jpg"
imagen2= "placa_4.jpg"
```
Modificar dependiendo de la ruta de la foto que quieras analizar

## Uso
1. Ejecutar el programa
2. Se procesaran las fotos
3. Se mostraran las fotos procesadas
4. Se mostrara el texto detectado y su nivel de confianza

## Estructura del proyecto
- deteccionPlacas.py: Script principal
- placa_q.jpg y placa_4.jpg: Fotos de ejemplo

## Ejemplo de salida

```nginx
EasyOCR encontró en placa 1:
  - 'ABC123'  (confianza: 0.98)

EasyOCR encontró en placa 2:
  - 'XYZ789'  (confianza: 0.95)
```

## Notas 
- La detección puede variar según la calidad y orientación de la imagen.
- Puedes ajustar los parámetros de GaussianBlur, adaptiveThreshold y OCR para mejores resultados.
- Si el codigo se quiere correr en Google Colab se deben de cambiar algunas cosas:
  - Agregar: from google.colab.patches import cv2_imshow
  - Cambiar cv2.imshow() por cv2_imshow()

## Creditos 
- OpenCV
- EasyOCR
