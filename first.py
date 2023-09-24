def number_of_words (n):
    word_count = 0
    if len(n) > 0 and n[0] != " ":
        word_count = 1
    for i in range(len(n)-1):
        if n[i] == " " and n[i + 1] != " ":
            word_count += 1
    return word_count

m = input("INPUT:")
print("Количество слов в строке:", number_of_words(m))