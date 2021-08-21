import cv2

carregarAlgoritmo = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

img = cv2.cvtColor(cv2.imread("imagens/time_corinthians.jpg"), cv2.COLOR_BGR2RGB)  # abro a imagem com imread que faza leiturada imagem

# transformando a imagem em cinza
# a documentação do opencv recomenda que se utilze a imagem na tonalidade de cinza, pois a porcentagem de acerto é maior
imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = carregarAlgoritmo.detectMultiScale(imagem_cinza)

print(faces)

for (x, y, l, a) in faces:
    cv2.rectangle(img, (x, y), (x + l, x + a), (0,255,0), 2)
cv2.imshow("Faces", img)
cv2.waitKey()
