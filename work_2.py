class Cat:  # класс кошек
    def __init__(
        self, Cat_name, Cat_mass, Cat_frequency):
        self.name = Cat_name # имя
        self.mass = Cat_mass# масса
        self.frequency = Cat_frequency # частота мурлыканья

# создаем файл
file_10 = open('file_10.txt', 'wt')
file_10.write('Барсик 5.0 75' + '\n')
file_10.write('Шкипер 6.0 75' + '\n')
file_10.write('Тося 4.0 80')
file_10.close()


# считываем файл
file_10 = open('file_10.txt', 'rt')
# создаем список для объектов класса кошек 
list_2 = []

s = file_10.readline()
while s != '':
    print(s.rstrip())
    list_1 = s.split()

    #  исключительные ситуации
    try:
        float(list_1[1])
        int(list_1[2])
    except ValueError:
        file_10.close()
        print('Error ValueError')
        break
    My_Cat = Cat(list_1[0], list_1[1], list_1[2])  # создание обекта класса Cat
    list_2.append(My_Cat)
    s = file_10.readline()
