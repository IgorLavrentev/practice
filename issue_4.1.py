import os.path

# три параметра функции: путь к каталогу, расширение файла и булев флажок
def two_roster(way, extension, flag):
    if flag == True:
        final_list = [] # итоговый список
        directories_list = [] # список каталогов
        files_list = [] # список файлов
        files_list_end = [] # список файлов с заданным расширением
        file_extension = extension # расшириение искомых файлов

    # поиск фйлов и подкаталогов в каталоге
        for root, dirs, files in os.walk(way):
            directories_list += dirs
            files_list += files

    # формирование списка с файлами заданного расширения
        for i in range (len(files_list)):
            name = files_list[i]
            if name[-(len(file_extension)):] == file_extension:
                files_list_end.append(name)

        # объединение списков файлов и каталогов
        final_list.append(files_list_end)
        final_list.append(directories_list)

        # вывод на экран игогового списка со списком файлов и каталогов
        print(final_list)
    else: pass

path = 'test' # пример пути

two_roster(path, 'txt', True)