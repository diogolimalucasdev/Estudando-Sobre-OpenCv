import cv2
import numpy as np

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

while True:
    _, frame = video.read()
    video_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(video_cinza, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        corte_cinza = video_cinza[y:y + h, x:x + w]

        corte_colorido = frame[y:y + h, x:x + w]
        cv2.imshow('video', corte_colorido)

    cv2.imshow('video2', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break

video.release()
cv2.destroyWindow()
