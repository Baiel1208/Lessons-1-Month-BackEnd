# HW #1
# задания 1

# 1) Что произойдет при вводе следующих команд. Напишите ответ в виде комментария.
# Например:
int("578")  # строка 579 из string превратится в integer
print(int)
int(673.3123)  # строка 673.3123 из float превратится в integer
print(int)
float(512)  # строка 512 из integer превратится в float
print(float)
int(float(str(192)))  # строка 192 из integer превратится в float
print(int)
float(173) + 5  # строка 192 из integer превратится в float
print(float)
str(193.000000000001)  # строка 193.000000000001  из float превратится в float
print(str)
# задания 2
# 2) Что такое конкатенация?
# Конкатенация — метод, который позволяет объединить несколько строк в одну.
# Объясните следующие две строки кода:
print(('Calling ') + str(911))  # объединяется как: Calling 911

print('abc' + 'xyz')  # объединяется как: abcxyz

# задания 3
# 3)Какие переменные можно складывать(без изменения их типа данных) и что при этом получится?

a = 589
b = 932.901
c = 'Hello world'
d = '892.01'

print(a, b, c, d)  # выйдет 589 932.901 Hello world 892.01

# Дополнительное задание:
# 4) Напишите одну строку кода, которая использует только вышеуказанные
# переменные, и после которой print(a, b, c, d) выведет следующее: Hello world589 892.01932.901589 1481.01

cc = 'Hello world'
aa = 589
dd = '892.01'
bb = 932.901
ee = 1481.01
a = cc+str(aa)
b = dd+str(bb)+str(aa)
c = ee
print(a, b, c)