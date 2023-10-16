##Задание 12.5.8
import random

# формируем массив
list_1 = []
for i in range(10):
    list_1.append(random.randint(1,50))

# функция сортировки массива
def Sorting_array(list1):
    for k in range(9):
        for j in range(9-k):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
# выводим на экран массив
print(Sorting_array(list_1)) 
