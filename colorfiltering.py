import cv2
import numpy as np
from matplotlib import pyplot as plt

# Caminho para a pasta
caminho_pasta = '/seu/caminho/aqui'
arquivo = 'basegrande.jpg'

frame = cv2.imread(f"{caminho_pasta}/{arquivo}")

img = frame

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue = np.array([147,71,20])
upper_blue = np.array([255,178,127])

lower_yellow = np.array([91, 147, 150])
upper_yellow = np.array([204, 255, 251])

mask1 = cv2.inRange(img,lower_blue,upper_blue)
mask2 = cv2.inRange(img,lower_yellow,upper_yellow)

mask = cv2.bitwise_or(mask1,mask2)

color_image = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
