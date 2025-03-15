import cv2
import numpy as np

# Función para verificar si el parqueo está ocupado
def identifySpot(path, reference):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Carga una imagen en escala de grises
    reference_image = cv2.imread(reference, cv2.IMREAD_GRAYSCALE)  # Carga la  imagen de referencia

 # Encuentra los bordes en la imagen que colocara el usuario
    edges = cv2.Canny(image, 100, 200) 
 # Bordes en la imagen de parqueadero vacio
    reference_edges = cv2.Canny(reference_image, 100, 200) 
 # Cuenta cuántos bordes tiene
    bordes = np.sum(edges)
    bordes_ref = np.sum(reference_edges)
    
# Comparara los bordes con la imagen que dio los bordes de referencia y esta dira si esta o cupado o disponible
    if bordes > bordes_ref:
        return "Ocupado"
    else:
        return "Disponible"

# Pide la imagen al usuario
path = input("Ingrese el nombre de la imagen: ")
reference = "empty.jfif"  #esta es la imagen de parqueo donde esta vacio, esta se toma de refrencia para las otras imagenes
# Muestra el resultado
print("El puesto de parqueo está:", identifySpot(path, reference))
