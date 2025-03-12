# Import OpenCV module
import cv2
import numpy as np

def identifyColor(plane):
    
    mean=0.0
    for row in plane:
        for p in row:    
            mean+=p
    

    
    print(f'Mean of plane is: {mean/(dims[0]*dims[1])}')
    return 00
# Read image
#img = cv2.imread("C:/Users/Joseph/Documents/Laboratorio 1/blue_car.jfif", cv2.IMREAD_COLOR)
img = cv2.imread("Laboratorio 1/blue_car.jfif", cv2.IMREAD_COLOR)

# Get image dimensions
dims=img.shape

# Show image dimensions
print(f'Image has {dims[2]} color planes each having {dims[0]} rows and {dims[1]} columns')

# Get matrix for each color plane
bluePlane = img[:,:,0]
greenPlane = img[:,:,1]
redPlane = img[:,:,2]

# Show image and each color plane
cv2.imshow("image", img)
cv2.imshow("Blue plane", bluePlane)
cv2.imshow("Green plane", greenPlane)
cv2.imshow("Red plane", redPlane)

for i in range(3):
    if i == 0:
        plane = redPlane
    if i == 2:
        plane == bluePlane
    if i == 3:
        plane == greenPlane
plane = greenPlane

dims = plane.shape
print(f'Plane has {dims[0]} rows and {dims[1]} columns')

# Compute mean of red plane by looping through image (version 1)
mean=0.0
for i in range(dims[0]):
    for j in range(dims[1]):
        mean+=plane[i][j]
        
print(f'Mean of plane is: {mean/(dims[0]*dims[1])}')


# Compute mean of red plane by looping through image (version 2)
mean=0.0
for row in plane:
    for p in row:    
        mean+=p
        
print(f'Mean of plane is: {mean/(dims[0]*dims[1])}')

# Wait for key
cv2.waitKey()
