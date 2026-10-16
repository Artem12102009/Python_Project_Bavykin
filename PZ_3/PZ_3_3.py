a = int(input("Введите двухзначное число: "))

d1 = a // 10
d2 =  a % 10

if (d1 + d2) % 2 == 0:
    a += 2
else:
    a -= 2

print(a)