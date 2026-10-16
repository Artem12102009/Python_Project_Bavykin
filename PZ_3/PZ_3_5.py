a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

c = a + b

if c % 5 == 0:
    c += 1
else:
    c -= 2

print(c)