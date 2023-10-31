import os.path
from PIL import Image, ImageDraw, ImageColor, ImageFont


# функция получает на вход два типа (расширения) графических форматов
def form(extension_one, extension_two):
    files_list = []
    files_list_end = []
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk('.'):
        files_list += files

    # формирование списка с файлами заданного расширения
    for i in range (len(files_list)):
        name = files_list[i]
        if name[-(len(extension_one)):] == extension_one:
            files_list_end.append(name)

    # конвертация в другой формат
    for j in range(len(files_list_end)):
        im = Image.open(files_list_end[j])
        word = files_list_end[j]
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)

        # рисование в центре изображения незаполненного квадрата, внутри которого написаны две строчки
        draw = ImageDraw.Draw(im)
        sz = im.size
        draw.rectangle([sz[0]/2 - 100,sz[1]/2 - 100, sz[0]/2 + 100,sz[1]/2 + 100])
        font = ImageFont.truetype("arial.ttf", 35)
        draw.text((sz[0]/2 - 40, sz[1]/2 - 40), 'Hello,\nWorld!', font=font, fill="blue")
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)
        os.remove(files_list_end[j])

# пример форматов файлов
extension_1 = 'JPEG'
extension_2 = 'png'

# вызов функции
form(extension_1, extension_2)