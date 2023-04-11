# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер билета: "))
a = (n//100000)
b = (n//10000) - a*10
c = (n//1000) - a*100 - b*10
s1 = a + b + c 
d = (n//100) - a*1000 - b*100 - c*10
e = (n%100)//10
f = n%10
# print(f"{a} {b} {c} {d} {e} {f}")
s2 = d + e + f
if s1 == s2: 
    print(f"{n} -> YES")
else: 
    print(f"{n} -> NO")