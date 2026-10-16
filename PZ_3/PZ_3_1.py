a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

c = a * b

if c < 0:
    c *= 8
else:
    c *= 1.5

print(c)