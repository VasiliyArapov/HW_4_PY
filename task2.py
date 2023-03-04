# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке содержащим количество ягод на кустах.

list_1 = list(map(int, input().split()))
temp_sum = 0
max_sum = 0

for i in range(len(list_1) - 1):
    temp_sum = list_1[i] + list_1[i - 1] + list_1[i - 2]
    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
