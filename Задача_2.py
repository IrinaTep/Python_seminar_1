class_a = int(input("Сколько учеников в классе A: "))
class_b = int(input("Сколько учеников в классе B: "))
class_c = int(input("Сколько учеников в классе C: "))

# res = -(-class_a // 2 + -class_b // 2 + -class_c // 2)
# print(res)

# print(round(class_a // 2 + class_b // 2 + class_c // 2))  --- ???

# res = (class_a//2) + (class_b//2) + (class_c//2) + (class_a%2) + (class_b%2) + (class_c%2)
# print(res)

print((class_a + 1)//2 + (class_b + 1)//2 + (class_c + 1)//2)

# import math
# print(f"Нужно {math.ceil(class_a/2) + math.ceil(class_b/2) + math.ceil(class_c/2)} парт")