import os.path
from zipfile import ZipFile


# функция получает на вход два параметра: имя файла архива и расширение файла
def archive(name_a, file_e):
    archive_name = name_a # название архива
    file_extension = file_e # расширение файлов для поиска
    list_names = [] # список файлов с заданным расширением

    # проверка, корректен ли архив
    with ZipFile(archive_name) as testzip:
        if testzip.testzip() != None:
            return print('Архив не корректен')
    
    # сканирование текущего каталога в поисках файлов с заданным расширением
    with ZipFile(archive_name) as testzip:
        list_names_all = testzip.namelist()

    for i in range(len(list_names_all)):
        fi = list_names_all[i]
        if fi[-(len(file_extension)): ] == file_extension:
            list_names.append(fi)

    # извлечение файла из архива в текущий каталог
    for j in range(len(list_names)):
        with ZipFile(archive_name) as testzip:
            testzip.extract(list_names[j])

    # создание нового архива
    ZipFile("new_test.zip", "w")

    # добавление в архив файлов с заданным расширением
    for k in range(len(list_names)):
        with ZipFile('new_test.zip', 'a') as testzip:
            testzip.write(list_names[k])
    
    # удаление файлов и каталогов с заданным расширением из текущей директории 
    for d in range(len(list_names)):
        if list_names[d].find('/') != -1:
            way_and_name = list_names[d]
            os.remove(way_and_name[:list_names[d].find('/')] + '/' + way_and_name[list_names[d].find('/') + 1:])
            os.rmdir(way_and_name[:list_names[d].find('/')])
        else:
            os.remove(list_names[d])
    
    print(f'Создание нового архива с файлами "{file_extension}" завершено!')

name_a = 'test.zip' # пример названия архива 
file_e = 'txt' # пример названия расширения файлов
archive(name_a, file_e) # вызов функции