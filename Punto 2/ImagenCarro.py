# Importar módulo de OpenCV
import cv2

def identifyColor(img):
    # Obtener forma de la imagen
    dims = img.shape
    # Obtener los planos de color para la imagen. ":" implica opperaciones de "slice" en la matriz
    bluePlane = img[:,:,0]
    greenPlane = img[:,:,1]
    redPlane = img[:,:,2]
    # Inicializar las medias para cada plano de color
    redplanemean = 0
    blueplanemean = 0
    greenplanemean = 0
    # Encontrar las medias de cada plano por medio del siguiente bucle for
    for i in range(3):
        mean = 0.0
        if i == 0: # Plano de color rojo
            plane = redPlane
            for row in plane:
                for p in row:    
                    mean+=p
            print(f'Media del plano rojo: {mean/(dims[0]*dims[1])}')
            redplanemean += mean/(dims[0]*dims[1])
        if i == 1: # Plano de color azul
            plane = bluePlane
            for row in plane:
                for p in row:
                    mean += p
            print(f'Media del plano azul: {mean/(dims[0]*dims[1])}')
            blueplanemean += mean/(dims[0]*dims[1])
        if i == 2: # Plano de color verde
            plane = greenPlane
            for row in plane:
                for p in row:
                    mean += p
            print(f'Media del plano verde: {mean/(dims[0]*dims[1])}')
            greenplanemean += mean/(dims[0]*dims[1])
    # Identificar el color de la imagen por medio de la comparación de cada media de cada plano de color
    if blueplanemean > redplanemean and blueplanemean > greenplanemean:
        color = "Azul"
    elif redplanemean > blueplanemean and redplanemean > greenplanemean:
        color = "Rojo"
    elif redplanemean == blueplanemean and blueplanemean == greenplanemean:
        color = "Escala de grises"
    else:
        color = "Verde o Amarillo"
    return color

# Preguntar por la ruta de la imagen
imgpath = str(input("Ingrese el nombre y ruta relativa de la imagen, incluyendo la extensión de archivo: "))

# Leer imagen
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)

# Obtener dimensiones de la imagen
dims = img.shape

# Mostrar dimensiones de la imagen
print(f'La imagen tiene {dims[2]} planos de color, cada uno teniendo {dims[0]} filas y {dims[1]} columnas')

# Obtener la matriz para cada plano de color
bluePlane = img[:,:,0]
greenPlane = img[:,:,1]
redPlane = img[:,:,2]

# Mostrar imagen y cada plano de color
cv2.imshow("Imagen", img)
cv2.imshow("Plano azul", bluePlane)
cv2.imshow("Plano verde", greenPlane)
cv2.imshow("Plano rojo", redPlane)

# Identificar el color de la imagen
color = print(f"El color de la imagen es: {identifyColor(img)}")

# Esperar a que el usuario presione una tecla
cv2.waitKey()
