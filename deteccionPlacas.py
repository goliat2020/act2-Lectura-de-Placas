import cv2
import easyocr
from google.colab.patches import cv2_imshow

imagen1= "/content/placa_q.jpg"
imagen2= "/content/placa_4.jpg"

def detectar_letras_centrales(ruta_imagen):
    # Carga de la imagen
    imagen_original = cv2.imread(ruta_imagen)
    if imagen_original is None:
        raise ValueError("No se pudo cargar la imagen. Verifica la ruta y el formato.")

    # Conversión a escala de grises
    gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gris, (5,5), 0)

    th = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    blockSize=15,
    C=4
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=5)


    return closing


placa1 = detectar_letras_centrales(imagen1)
placa2 = detectar_letras_centrales(imagen2)

cv2_imshow(placa1)
cv2_imshow(placa2)

reader = easyocr.Reader(['en','es'], gpu=False)  # ajustar idiomas según necesidad
results = reader.readtext(placa1,
                          detail=1,
                          paragraph=False,
                          contrast_ths=0.05,
                          adjust_contrast=0.7)

results2 = reader.readtext(placa2,
                          detail=1,
                          paragraph=False,
                          contrast_ths=0.05,
                          adjust_contrast=0.7)

print("EasyOCR encontró:")
for _, text, prob in results:
    print(f"  - '{text}'  (confianza: {prob:.2f})")

for _, text, prob in results2:
    print(f"  - '{text}'  (confianza: {prob:.2f})")