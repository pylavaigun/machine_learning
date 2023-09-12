import cv2
import numpy as np



cap = cv2.VideoCapture('videos/video_test.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)


