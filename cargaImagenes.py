import cv2
import numpy as np

#Cargar la imagen a color
IRGB=cv2.imread('venom.jpg')
print(IRGB)
print(IRGB.shape)

print("Modificacion del archivo en la rama main")
print(len(IRGB))
