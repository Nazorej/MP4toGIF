import cv2

# Открытие видеофайла
video = cv2.VideoCapture('input.mp4')

# Получение FPS
fps = video.get(cv2.CAP_PROP_FPS)

# Получение ширины и высоты видео
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f'FPS: {fps}')
print(f'Width: {width}, Height: {height}')
