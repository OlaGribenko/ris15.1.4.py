# два вида файлов:
# текстовые (.txt, .html)
# бинарные (изображения, аудио, видео)

#открытие и закрытие файла
# open(file, mode)

#путь файла: фбсолютый (c://) и относительный

myfile = open('WebinarPractice.txt', 'r')
file = myfile.read()
print(file)
myfile.close()