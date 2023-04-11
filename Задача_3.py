'''
    Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
    Если год является високосным, то выведите YES, иначе выведите NO.
    Напомним, что в соответсвии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, 
    а также если он кратен 400.
    Input: 2016
    Output: YES
'''
# Вариант 1
year = int(input("Введите год: "))

# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print("YES")
# else:
#     print("NO")

# Вариант 2
# if (year % 400 == 0):
#     print("YES")
# elif (year % 4 == 0 and year % 100 != 0):
#     print("YES")
# else:
#     print("NO")

# Вариант 3
# print(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

# Улучшенный вариант
res = "Yes" if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) else "No"
print(res)