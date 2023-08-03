import os
import time
import cv2

# Abre a câmera
cap = cv2.VideoCapture(0)

print("Sorria, irei tirar uma foto sua!")

# Inicia a contagem regressiva
for i in range(3, 0, -1):
    print("Tirando a foto em ", str(i))
    time.sleep(1)

# Tira a foto
ret, frame = cap.read()

# Salva o caminho absoluto da pasta em que o código está localizado
caminho_pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Combinar o caminho absoluto com o nome da foto para criar o caminho completo do arquivo
caminho_completo_foto = os.path.join(caminho_pasta_atual, "foto.jpg")

# Salva a foto
cv2.imwrite(caminho_completo_foto, frame)

# Fecha a câmera
cap.release()