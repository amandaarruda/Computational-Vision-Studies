import cv2
import numpy as np
from matplotlib import pyplot as plt

# Caminho para a pasta onde está a imagem
caminho_pasta = '/seu/caminho/aqui'
arquivo = 'basegrande.jpg'

# Lendo a imagem especificada no caminho definido anteriormente
frame = cv2.imread(f"{caminho_pasta}/{arquivo}")

# Convertendo a imagem para o espaço de cores HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Definindo os intervalos de cores azul e amarelo
lower_blue = np.array([135, 68, 32])
upper_blue = np.array([255, 178, 127])

lower_yellow = np.array([42, 132, 129])
upper_yellow = np.array([187, 226, 231])

# Criando máscaras para as cores azul e amarelo
mask1 = cv2.inRange(frame, lower_blue, upper_blue)
mask2 = cv2.inRange(frame, lower_yellow, upper_yellow)

# Combinando as máscaras usando a operação bitwise OR
mask = cv2.bitwise_or(mask1, mask2)

# Aplicando a máscara combinada à imagem original
color_image = cv2.bitwise_and(frame, frame, mask=mask)

# Exibindo a imagem resultante
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
