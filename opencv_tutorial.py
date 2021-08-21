import numpy as np
import cv2  # trabalha com bgr, azul, verde e vermelho
from matplotlib import pyplot as plt  # biblioteca usada pra graficos e essa bilbioteca entende, vermelho, verde, azul


# por isso a cor fica estranha, ai usamos o converte color

def showImage(img):
    # convertendo a imagem, onde era
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # agora a imagem fica em rgb

    # aqui eu construo a imagem
    plt.imshow(img)

    # aqui eu exibo minha imagem com o grafico, pois assim eu csg indentificar os px
    plt.show()


def main():
    # aqui ele ja recebe minha imagem
    obj_img = cv2.imread("faces/diogo.jpg")

    # posso mandar a imagem ja em preto em branco
    # img = cv2.imread("faces/diogo.jpg", 0)  # assim a imagem fica em preto e branco colocando o 0 depois do 0

    # apresento a imagem chamando a função showImage
    showImage(obj_img)

    # print(obj_img.shape) #aqui ele nos mostra a altura, largura e quantidadee canais de cor
    altura, largura, canais_de_cor = obj_img.shape
    print(f"Dimensões da imagem: \n altura:{altura} \n largura: {largura} \n canais de cor:{canais_de_cor}")

    def getColor(img, x, y):
        return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

    def setColor(img, x, y, b, g, r):
        img.itemset((y, x, 0), b)
        img.itemset((y, x, 1), g)
        img.itemset((y, x, 2), r)

    # MANIPULANDO OS PIXELS DA IMAGEM, pecorrendo a imagem com o FOR.

    # O y é minha coluna, ou seja para cada coluna eu vou ate o final que é minha largura que é a linha
    # apos eu pecorrer minha coluna ate o final que é minha largura eu passo para linha de baixo

    for y in range(0, altura):
        for x in range(0, largura):
            # aqui eu mostro em cada posição, qual é minha cor, ou seja naquele pixel essa é a cor
            # print(f"posição X: {x}, Y: {y}, cor: {obj_img[y][x]} ")

            azul, verde, vermelho = getColor(obj_img, x, y)

            # setColor(obj_img, x, y, 0, 0, vermelho)
            # com isso eu posso determinar que cor eu quero fique definada
            # o primeiro 0 é o azul o segundo é verde e o segundo é o vermelho, se eu setar em 0 ele fica sem aquela cor

    # salvando a imagem modificada
    # cv2.imwrite("diogo_modificado_vermelho.png", obj_img)

    # recortando a imagem, a primeira virgula é meu y
    # 164 é minha posição incial em Y depois dos dois pontos é ate aonde eu vou,ou seja 164 mais 80
    # OBS no OPENCV, QUANDO ADICIONAMOS NO EIXO Y NOS DESCESMOS A IMAGEM E NAO SUBIMOS
    # dpois da virgula é meu eixo X

    eye_img = obj_img[164:164 + 80, 97:97 + 30]  # apenas um exemplo de corte
    showImage(eye_img)

    showImage(obj_img)


main()
