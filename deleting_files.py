import os.path

def catalog_deletion(catalog):
    directories_list = [] # список каталогов
    files_list = [] # список файлов
    folder = catalog # католог, который нужно удалить

    # Проверка: существует ли каталог
    existence = os.path.isdir(catalog)
    if existence != True:
        return print('Каталога не существует')

    
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk(folder):
        directories_list += dirs
        files_list += files
   

    if directories_list == []:
        # удаление файлов
        for i in range(len(files_list)): # удаление файлов
            os.remove(f'{folder}/{files_list[i]}')

        # удаление каталога
        os.rmdir(catalog)

        # вывод результата
        return print('Каталог успешно удален')
    else:
        return print('Каталог не удален')

catalog = 'test/test1.1' # пример
catalog_deletion(catalog) # вызов функции