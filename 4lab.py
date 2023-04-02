import math
def lab4():
    s1 = (lambda r, h: math.pi * r * (r + math.sqrt(r ** 2 + h ** 2)))(float(input("Введите радиус первого конуса: ")),float(input("Введите высоту первого конуса: ")))
    s2 = (lambda r, h: math.pi * r * (r + math.sqrt(r ** 2 + h ** 2)))(float(input("Введите радиус второго конуса: ")),float(input("Введите высоту второго конуса: ")))
    s3 = (lambda r, h: math.pi * r * (r + math.sqrt(r ** 2 + h ** 2)))(float(input("Введите радиус третьего конуса: ")),float(input("Введите высоту третьего конуса: ")))
    max_s = max(s1, s2, s3)

    if max_s == s1:
        print("Площадь поверхности первого конуса максимальна.")
    elif max_s == s2:
        print("Площадь поверхности второго конуса максимальна.")
    else:
        print("Площадь поверхности третьего конуса максимальна.")