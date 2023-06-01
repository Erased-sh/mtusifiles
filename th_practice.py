def f_t():
    pass1 = input('Введите пароль\n')
    pass2 = input('Повторите пароль\n')

    if pass1 != pass2:
        print('Пароль не принят')
    else:
        print('Пароль принят')
def s_t():
    num = int(input('Введи число\n'))
    if num % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')

def th_t():
    num = input('Введи четырёхзначное число\n')
    if int(num[0]) + int(num[3]) == int(num[1]) - int(num[2]):
        print('ДА')
    else:
        print('НЕТ')
def fo_t():
    age = int(input('Введи возраст\n'))

    if age <= 13:
        print('детство')
    elif age >= 14 and age <= 24:
        print('молодость')
    elif age >= 25 and age <= 59:
        print('зрелость')
    else:
        print('старость')
def fi_t():
    num1 = int(input('Введи число\n'))
    num2 = int(input('Введи число\n'))
    num3 = int(input('Введи число\n'))

    if num3 - num2 == num2 - num1:
        print('YES')
    else:
        print('NO')
def si_t():
    num1 = int(input('Введи число\n'))
    num2 = int(input('Введи число\n'))
    num3 = int(input('Введи число\n'))

    fin = 0

    for i in [num1, num2, num3]:
        if i > 0:
            fin += i
    print(fin)
def se_t():
    year = int(input('Введите год\n'))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('YES')
    else:
        print('NO')
def e_t():
    num = int(input('Введите число\n'))

    if num >= -7 and num < 4:
        print('Число вне промежутка 1')
    else:
        print('Число в промежутке 1')

    if num >= 0 and num < 3:
        if num >= 27 and num <= 45:
            print('Число в промежутке 2')
        print('Число вне промежутка 2')
    print('Число вне промежутка 2')
def n_t():
    column1 = int(input())
    row1 = int(input())

    column2 = int(input())
    row2 = int(input())

    def chess():
        if column1 == column2 and row1 == row2:
            return 'NO'
        if abs(column1 - column2) <= 1:
            if abs(row1 - row2) <= 1:
                return 'YES'
        return 'NO'

    print(chess())
