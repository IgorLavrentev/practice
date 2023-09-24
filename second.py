def minimum (n1, n2, n3):
    if n1 < n2 and n1 <n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    elif n3 < n1 and n3 < n2:
        return n3

m1 = int(input("INPUT:"))
m2 = int(input("INPUT:"))
m3 = int(input("INPUT:"))
print("Наименьшее из введённых чисел:", minimum (m1, m2, m3))
