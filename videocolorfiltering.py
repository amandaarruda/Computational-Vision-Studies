import cv2 
import numpy as np 

# Caminho para a pasta onde está a imagem
caminho_pasta = '/seu/caminho/aqui'
arquivo = 'bases.mp4'

cap = cv2.VideoCapture(f"{caminho_pasta}/{arquivo}")

while(1): 
    _, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    # Definindo os intervalos de cores azul e amarelo
    lower_blue = np.array([135, 68, 32])
    upper_blue = np.array([255, 178, 127])

    lower_yellow = np.array([110, 167, 176])
    upper_yellow = np.array([182, 224, 229])

    # Criando máscaras para as cores azul e amarelo
    mask1 = cv2.inRange(frame, lower_blue, upper_blue)
    mask2 = cv2.inRange(frame, lower_yellow, upper_yellow)

    # Combinando as máscaras usando a operação bitwise OR
    mask = cv2.bitwise_or(mask1, mask2)

    result = cv2.bitwise_and(frame, frame, mask = mask) 

    cv2.imshow('frame', frame) 
    cv2.imshow('mask', mask) 
    cv2.imshow('result', result) 
    
    cv2.waitKey(0)

cv2.destroyAllWindows() 
cap.release() 
