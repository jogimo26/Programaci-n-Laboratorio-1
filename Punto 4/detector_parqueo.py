import cv2  
import numpy as np  

ref_bordes = 965  


def identifySpot(image):
    assert image is not None
    edges = cv2.Canny(image, 100, 200) 
    bordes = np.sum(edges) / 255 
    print("Cantidad de bordes:", bordes)  

    if bordes > ref_bordes:  
        return "Ocupado"
    else:  
        return "Disponible"

camara = cv2.VideoCapture(0)  # Activa la cámara

while True:
    _, imagen = camara.read()  # Captura la imagen
    cv2.imshow("parqueadero", imagen)  # Muestra lo que ve la cámara

    tecla = cv2.waitKey(1)  # Espera una tecla

    if tecla == 27:  # Si presiona ESC, cierra todo
        break
    elif tecla == 32:  # Si presiona ESPACIO, analiza la imagen
        estado = identifySpot(imagen)  # Verifica si el puesto está ocupado
        print("El puesto está:", estado)  # Muestra el resultado

camara.release()  
cv2.destroyAllWindows()
