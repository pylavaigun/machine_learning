import cv2
import numpy as np

bottom = np.zeros((500, 500, 3), dtype='uint8')
center_point = (bottom.shape[0] // 2, bottom.shape[1] // 2)
i = 10
radius = 0
while i >= 0:
    color_circle = tuple[0, 0, 255]
    radius_circle = i * 20
    if i % 2 == 0:
        color_circle = (255, 0, 0)
    else:
        color_circle = (0, 255, 0)
    darts_sector = cv2.circle(
        bottom,
        center=center_point,
        radius=radius_circle,
        color= tuple(color_circle),
        thickness=cv2.FILLED
    )
    print(f'На итерации № {i} Центр круга {center_point}, цвет RGB - {color_circle}')

    i -= 1
cv2.imshow('Na', bottom)
cv2.waitKey(0)
