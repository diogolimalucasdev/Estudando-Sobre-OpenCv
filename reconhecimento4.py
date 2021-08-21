import cv2

video = cv2.VideoCapture(0)  # aqui eu inicio minha webcam, e coloco o 0 pois é minha camera padrão

while True:
    conectado, frame = video.read()

    #mostrar a imagem que ta na camera
    cv2.imshow('Video', frame )

    # para imagem ficar travada, para nao abrir e fechar logo e espero 1 para fechar
    #coloquei a letra 'q' pois ela na tabela asc é == 1
    if cv2.waitKey(1) == ord('q'):
        break
video.release() #pra liberar a captura
cv2.destroyWindow() #pra nao ficar salvo na memoria


