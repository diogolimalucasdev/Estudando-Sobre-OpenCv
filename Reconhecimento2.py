from mtcnn import MTCNN
from PIL import Image  # biblioteca para manipular imagens
from os import listdir  # pra poder listar diretorio
from os.path import isdir  # pra perguntar seaquilo que esta sendo lido é um diretorio ou nao
from numpy import asarray  # pra ode converter uma imagem pil em array

detector = MTCNN()


def extrair_face(arquivo, size=(160, 160)):  # size é o tamanho padrão da imagem

    img = Image.open(arquivo)  # caminho completo da imagem

    img = img.convert("RGB")  # converter em RGB a imagem

    array = asarray(img)  # vai pegar a imagem e transformar em numpy

    results = detector.detect_faces(array)

    x1, y1, width, height = results[0]['box ']  # x1 e y1 é o canto esquerdo do rosto perto da sombrancelha

    x2 = x1 + width  # com isso eu pego toda extensao da testa
    y2 = y1 + height  # com isso eu pego toda altura do rosto

    face = array[y1:y2, x1:x2]  # comando do numpy subrai um quadrado da imagem original

    image = Image.fromarray(face)
    image = image.resize(size)
    return image


def load_images(directory_src, directory_target):
    for subdir in listdir(directory_src):
        path = directory_src + subdir + "\\"

        path_tg = directory_target + subdir + "\\"

        if not isdir(path):
            continue
