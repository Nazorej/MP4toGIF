import imageio

# Чтение видеофайла
reader = imageio.get_reader('input.mp4')

# Получение FPS и размеров видео
fps = reader.get_meta_data()['fps']
size = reader.get_meta_data()['source_size']

# Создание writer для записи GIF
writer = imageio.get_writer('output.gif', fps=fps, size=size)

# Проход по каждому кадру в видео
for i, frame in enumerate(reader):
    writer.append_data(frame)

# Закрытие writer
writer.close()
