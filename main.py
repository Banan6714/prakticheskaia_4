# Вывести все числа, которые делятся на 7, но не делятся на 5 (от 1 до N)

while True:
    try:
        N = int(input("Введите наибольшее значение диапазона(N): "))
        break
    except ValueError:
        print("Введите число!")

x = 1
if N >= x:
    while x <= N:
        if x % 7 == 0:
            if x % 5 != 0:
                print(x)
                x = x + 1
            else:
                x = x + 1
        else:
            x = x + 1
else:
    print("N не должен быть меньше 1!")
