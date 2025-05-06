import cv2
#Instalar easyocr antes de ejecutar el codigo
import easyocr

#Asignar las rutas de las imagenes
imagen1= "/content/placa_q.jpg"
imagen2= "/content/placa_4.jpg"

def detectar_letras_centrales(ruta_imagen):
    # Carga de la imagen
    imagen_original = cv2.imread(ruta_imagen)
    if imagen_original is None:
        raise ValueError("No se pudo cargar la imagen. Verifica la ruta y el formato.")

    # Conversión a escala de grises
    gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    #Aplicar el gaussian blur
    blur = cv2.GaussianBlur(gris, (5,5), 0)

    #Aplicar el threshold
    th = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    blockSize=15,
    C=4
    )
    
    #Definir el kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    
    #Cambiar la morfologia de la imagen
    closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=5)


    return closing

#Llamar a la funcion por cada imagen
placa1 = detectar_letras_centrales(imagen1)
placa2 = detectar_letras_centrales(imagen2)

#Mostrar las imagenes 
cv2.imshow(placa1)
cv2.imshow(placa2)

#Definir el lector
reader = easyocr.Reader(['en','es'], gpu=False)  # ajustar idiomas según necesidad

#Procesar los resultados
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

#Imprimir los resultados
print("EasyOCR encontró:")
for _, text, prob in results:
    print(f"  - '{text}'  (confianza: {prob:.2f})")

for _, text, prob in results2:
    print(f"  - '{text}'  (confianza: {prob:.2f})")