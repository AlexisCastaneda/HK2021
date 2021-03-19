import cv2
import numpy as np

#Cargar la imagen a color
IRGB=cv2.imread('venom.jpg')
print(IRGB)
print(IRGB.shape)


print("Lineas agregadas en la ramaDos")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)

