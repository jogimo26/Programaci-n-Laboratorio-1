# Import OpenCV module
import cv2

def identifyColor(img):
    # Get image shape
    dims=img.shape
    # Get the planes for the image. ":" implies slice operations in the matrix 
    bluePlane = img[:,:,0]
    greenPlane = img[:,:,1]
    redPlane = img[:,:,2]
    # Initialize the means for each color plane
    redplanemean = 0
    blueplanemean = 0
    greenplanemean = 0
    for i in range(3):
        mean = 0.0
        if i == 0:
            plane = redPlane
            for row in plane:
                for p in row:    
                    mean+=p
            print(f'Mean of red plane is: {mean/(dims[0]*dims[1])}')
            redplanemean += mean/(dims[0]*dims[1])
        if i == 1:
            plane = bluePlane
            for row in plane:
                for p in row:
                    mean += p
            print(f'Mean of blue plane is: {mean/(dims[0]*dims[1])}')
            blueplanemean += mean/(dims[0]*dims[1])
        if i == 2:
            plane = greenPlane
            for row in plane:
                for p in row:
                    mean += p
            print(f'Mean of green plane is: {mean/(dims[0]*dims[1])}')
            greenplanemean += mean/(dims[0]*dims[1])
    # Identify the image's color by comparing every mean of every color
    if blueplanemean > redplanemean and blueplanemean > greenplanemean:
        color = "Blue"
    elif redplanemean > blueplanemean and redplanemean > greenplanemean:
        color = "Red"
    elif redplanemean == blueplanemean and blueplanemean == greenplanemean:
        color = "Grayscale"
    else:
        color = "Green or Yellow"
    return color

# Ask for the image path
imgpath = str(input("Input the name and relative route of the image, including the file extension: "))

# Read image
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)

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

# Identify the image's color
color = print(f"The color of the image is: {identifyColor(img)}")

# Wait for key
cv2.waitKey()
