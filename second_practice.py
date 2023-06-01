from math import factorial


def f_t():
    N = int(input())
    sq = round(1.555555, 3)
    print(f'Квадратный корень из номера бригады равен: \n{sq}')
def s_t():
    N = int(input())
    G = int(input())
    H = G - N

    for i in ['+', '*']:
        print(f'{N}{i}{G}{i}{H}')
        exec(f'print({N}{i}{G}{i}{H})')

    for i in [N, G, H]:
        print(f'{N}-{G}-{H}')
        exec(f'print({N}-{G}-{H})')

    for i in [N, G, H]:
        print(f'{N}/{G}/{H}')
        exec(f'print({N}/{G}/{H})')
def t_t():
    last_name = input('Введи фамилию\n')
    student = ' - студент'
    full = last_name + student
    print(f'{full}\n{len(full)}')
def fth_t():
    last_name = input('Введи фамилию\n')
    print(f'Фамилия студента в обратном порядке {last_name[::-1]}, количество слов - {factorial(len(last_name))}')