import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8')

#photo[100:150, 200:280 ] = 189, 140, 175


cv2.rectangle(photo, (10, 10), (100, 100), (189, 140, 175), thickness=cv2.FILLED)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1] // 2, photo.shape[1] // 2), (255, 0, 0), thickness=3)
cv2.putText(photo, 'Meimun', (100,50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), thickness=2)



cv2. imshow('Na', photo)
cv2. waitKey(5*1000)
