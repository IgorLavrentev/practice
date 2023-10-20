import random

# создание 10 файлов
fi_1 = open('1.txt', 'wt')
fi_2 = open('2.txt', 'wt')
fi_3 = open('3.txt', 'wt')
fi_4 = open('4.txt', 'wt')
fi_5 = open('5.txt', 'wt')
fi_6 = open('6.txt', 'wt')
fi_7 = open('7.txt', 'wt')
fi_8 = open('8.txt', 'wt')
fi_9 = open('9.txt', 'wt')
fi_10 = open('10.txt', 'wt')

# запись трёх случайных чисел в каждый файл
fi_1.write(str(random.randint(1, 100)) + '\n')
fi_1.write(str(random.randint(1, 100)) + '\n')
fi_1.write(str(random.randint(1, 100)))

fi_2.write(str(random.randint(1, 100)) + '\n')
fi_2.write(str(random.randint(1, 100)) + '\n')
fi_2.write(str(random.randint(1, 100)))

fi_3.write(str(random.randint(1, 100)) + '\n')
fi_3.write(str(random.randint(1, 100)) + '\n')
fi_3.write(str(random.randint(1, 100)))

fi_4.write(str(random.randint(1, 100)) + '\n')
fi_4.write(str(random.randint(1, 100)) + '\n')
fi_4.write(str(random.randint(1, 100)))

fi_5.write(str(random.randint(1, 100)) + '\n')
fi_5.write(str(random.randint(1, 100)) + '\n')
fi_5.write(str(random.randint(1, 100)))

fi_6.write(str(random.randint(1, 100)) + '\n')
fi_6.write(str(random.randint(1, 100)) + '\n')
fi_6.write(str(random.randint(1, 100)))

fi_7.write(str(random.randint(1, 100)) + '\n')
fi_7.write(str(random.randint(1, 100)) + '\n')
fi_7.write(str(random.randint(1, 100)))

fi_8.write(str(random.randint(1, 100)) + '\n')
fi_8.write(str(random.randint(1, 100)) + '\n')
fi_8.write(str(random.randint(1, 100)))

fi_9.write(str(random.randint(1, 100)) + '\n')
fi_9.write(str(random.randint(1, 100)) + '\n')
fi_9.write(str(random.randint(1, 100)))

fi_10.write(str(random.randint(1, 100)) + '\n')
fi_10.write(str(random.randint(1, 100)) + '\n')
fi_10.write(str(random.randint(1, 100)))

# закрытие файлов
fi_1.close()
fi_2.close()
fi_3.close()
fi_4.close()
fi_5.close()
fi_6.close()
fi_7.close()
fi_8.close()
fi_9.close()
fi_10.close()


for i in range(2):
    a = random.randint(1, 11)
    b = random.randint(1, 11)

# функция, которая возвращает сумму шести чисел
def sum_six(x, y):
    summ = 0
    if x == 1 or y == 1:
        fi_1 = open('1.txt', 'rt')
        s = fi_1.readline()
        while s != '':

#  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_1.close()
                return print('Error ValueError')

            summ += int(s.rstrip())
            s = fi_1.readline()    
        fi_1.close()

    if x == 2 or y == 2:
        fi_2 = open('2.txt', 'rt')
        s = fi_2.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_2.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_2.readline()
        fi_2.close()        

    if x == 3 or y == 3:
        fi_3 = open('3.txt', 'rt')
        s = fi_3.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_3.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_3.readline()
        fi_3.close()  

    if x == 4 or y == 4:
        fi_4 = open('4.txt', 'rt')
        s = fi_4.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_4.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_4.readline()
        fi_4.close()  

    if x == 5 or y == 5:
        fi_5 = open('5.txt', 'rt')
        s = fi_5.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_5.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_5.readline()
        fi_5.close()  

    if x == 6 or y == 6:
        fi_6 = open('6.txt', 'rt')
        s = fi_6.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_6.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_6.readline()
        fi_6.close()  

    if x == 7 or y == 7:
        fi_7 = open('7.txt', 'rt')
        s = fi_7.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_7.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_7.readline()
        fi_7.close()  

    if x == 8 or y == 8:
        fi_8 = open('8.txt', 'rt')
        s = fi_8.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_8.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_8.readline()
        fi_8.close() 

    if x == 9 or y == 9:
        fi_9 = open('9.txt', 'rt')
        s = fi_9.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_9.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_9.readline()
        fi_9.close() 

    if x == 10 or y == 10:
        fi_10 = open('10.txt', 'rt')
        s = fi_10.readline()
        while s != '':

        #  исключительные ситуации
            try:
                int(s)
            except ValueError:
                fi_10.close()
                return print('Error ValueError')
            
            summ += int(s.rstrip())
            s = fi_10.readline()
        fi_10.close() 


    if x == y:
        summ *=  2
    return print(summ)

sum_six(a, b)