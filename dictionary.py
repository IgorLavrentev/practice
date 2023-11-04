import random

# Задание 1
# 100 самых популярных глаголов в английском языке
verbs = ['be', 'have', 'do', 'say', 'go', 'can', 'get', 'would', 'make', 
       'know', 'will', 'think', 'take', 'see', 'come', 'could', 'want',
       'look', 'use', 'find', 'give', 'tell', 'work', 'may', 'should', 'call',
       'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep',
       'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'might', 'show', 
       'hear', 'play', 'run', 'move', 'like', 'live', 'believe', 'hold', 'bring',
       'happen', 'must', 'write', 'provide', 'sit', 'stand', 'lose', 'pay',
       'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 
       'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read',
       'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 
       'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die',
       'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain']

# список со значениями от 1 до 100
list_one = [ ]
for g in range(1, 101):
    list_one.append(g)
dictionary_one = {}

# заполняем словарь: 100 случайных пар ключ + строка
for i in range(100):
    dictionary_one[list_one[i]] = random.choice(verbs)

# считываем по ключам все значения и выводим
for j in range(1, len(dictionary_one) + 1):
    print(dictionary_one.get(j))

# затем удаляем все пары
for k in range(1, len(dictionary_one) + 1):
    del dictionary_one[k]


# Задание 2

# генерация списка с числами в диапазоне от 1 до 10
list_of_values = []
for q in range(15):
    random_number = random.randint(1, 10)
    list_of_values.append(random_number)

# генерация числа N
n = random.randint(1, 3)

def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} # создание словаря с ключами от 1 до 10
    final_list = [] # создание итогового (возвращаемого) списка 
    for w in range(len(list_of_val)): # подсчёт повторений каждого числа
        if list_of_val[w] == 1:
            dictionary_of_numbers[1] = dictionary_of_numbers[1] + 1
        if list_of_val[w] == 2:
            dictionary_of_numbers[2] = dictionary_of_numbers[2] + 1
        if list_of_val[w] == 3:
            dictionary_of_numbers[3] = dictionary_of_numbers[3] + 1
        if list_of_val[w] == 4:
            dictionary_of_numbers[4] = dictionary_of_numbers[4] + 1
        if list_of_val[w] == 5:
            dictionary_of_numbers[5] = dictionary_of_numbers[5] + 1
        if list_of_val[w] == 6:
            dictionary_of_numbers[6] = dictionary_of_numbers[6] + 1
        if list_of_val[w] == 7:
            dictionary_of_numbers[7] = dictionary_of_numbers[7] + 1
        if list_of_val[w] == 8:
            dictionary_of_numbers[8] = dictionary_of_numbers[8] + 1
        if list_of_val[w] == 9:
            dictionary_of_numbers[9] = dictionary_of_numbers[9] + 1
        if list_of_val[w] == 10:
            dictionary_of_numbers[10] = dictionary_of_numbers[10] + 1

    for e in range(1, len(dictionary_of_numbers) + 1): # добавление в итоговый список всех значений, превышающих N
        if dictionary_of_numbers.get(e) > n_1:
            final_list.append(e)

    return final_list

# вызов функции
number_of_repetitions(list_of_values, n)