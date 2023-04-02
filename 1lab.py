#f(x)=tg(2x)*sec(2x)
#Область допустимых значений:{sec(2x) != 0, x !=(k + 1/2)*pi, k::Z}
#Ввод не из области значений вызовет панику программы. Можно избежать с помощью try:...except:

import math
def lab1():
    # Вычисление функции для заданных констант
    x_const = 1.5
    f_const = math.tan(2 * x_const) + 1 / math.cos(2 * x_const)
    return(f'Вычисление для x = {x_const}: f(x) = {f_const:.4f}')

    # Вычисление функции для введенных пользователем данных
    x_user = float(input('Введите значение x: '))
    f_user = math.tan(2 * x_user) + 1 / math.cos(2 * x_user)
    return (f'Вычисление для x = {x_user}: f(x) = {f_user:.4f}')