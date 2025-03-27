import cv2
import numpy

# Resolución de la imagen (En x,y)
dimx = 680
dimy = 480

# Puntos (en x,y) para el cuadrado
iniciocuad = (240,140)
fincuad = (440,340)

# Se hace la imagen por medio de una matriz llena de ceros, usando la función numpy.zeros(). Se usa el tipo de datos uint8 porque va desde 0 a 255 para representar de negro a blanco
img = numpy.zeros((dimy,dimx), numpy.uint8)

# Se hace el rectángulo
cv2.rectangle(img,iniciocuad,fincuad,255,-1)

# Mostrar la imagen
cv2.imshow("imagen",img)

# Final, espera a que se presione cualquier tecla y se cierran todas las ventanas
cv2.waitKey()
cv2.destroyAllWindows()
