import cv2
import numpy as np

ref_bordes = 965  # Este es el valor de referencia que sacamos previamente de la imagen del parqueadero vacío

# Función para verificar si el parqueo está ocupado
def identifySpot(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Cargamos la imagen que ingresa el usuario en escala de grises
    assert image is not None, "The image does not exist"

    # Aplicamos el detector de bordes Canny sobre la imagen
    # Los valores 100 y 200 son los umbrales inferior y superior que nos ayudan a definir los bordes detectados
    edges = cv2.Canny(image, 100, 200)  
    cv2.imshow("Bordes",edges)
    cv2.imshow("Imagen",image)

    # Se halla el promedio de bordes en la imagen
    bordes = np.sum(edges) / 255
    print("Promedio de bordes en la imagen ingresada:", bordes)

    # Comparamos la cantidad de bordes detectados con el valor de referencia que habíamos calculado antes
    # Si es mayor que el valor de referencia, entonces consideramos que está ocupado
    if bordes > ref_bordes:
        return "Ocupado"
    else:
        return "Disponible"

# Pedimos la imagen al usuario
path = input("Ingrese el nombre de la imagen: ")

# Mostramos el resultado final, indicando si el puesto de parqueo está ocupado o disponible
print("El puesto de parqueo está:", identifySpot(path))
cv2.waitKey()
