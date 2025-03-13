import cv2

img = cv2.imread("Laboratorio 1/blue_car.jfif", cv2.IMREAD_COLOR)
assert img is not None, "The image does not exist"
edges = cv2.Canny(img,100,200, L2gradient=True)

cv2.imshow("Border image", edges)

cv2.waitKey()
