## Этот файл предназначен для тестирования testing.py 
import unittest
from testing import Sorting_array

list_first = [4,3,2,1,5,6,7,8,9,10]
list_second = [48493498384928,3,2,1,5,6,7,8,9,4]
list_three = [4,3,2,1,5,6,7,8,9,10] # например может быть ошибка при таком массиве [4,3,2,1,5,6,7,8,9,'э']

class MyTests(unittest.TestCase):

    def test1(self): # проверка результата функции с известным значением
        self.assertEqual(Sorting_array(list_first), [1,2,3,4,5,6,7,8,9,10])

    def test2(self): # проверка результата функции с известным достаточно большим значением 
        self.assertEqual(Sorting_array(list_second), [1,2,3,4,5,6,7,8,9,48493498384928])

    def test3(self):  # проверка того, что в массиве только данные типа 'int'
        for i in range(len(list_three)):      
            self.assertTrue(int(list_three[i]))

    def test4(self):  # проверка того, что первый элемент меньше последнего
        list_sort = Sorting_array(list_first)
        self.assertTrue(list_sort[0] < list_sort[9])

if __name__ == '__main__':
    unittest.main()