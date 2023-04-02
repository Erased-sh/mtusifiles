def lab5():
    email = input("Введите адрес электронной почты: ")

    if "@" in email:
        username, domain = email.split("@")
        if username != '' and domain != '':
            print("Адрес электронной почты верен")
        else:
            print("Ошибка: неверный формат адреса электронной почты")
    else:
        print("Ошибка: неверный формат адреса электронной почты")
    lab5task2(email)

def lab5task2(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in string.lower():
        if char in vowels:
            count += 1
    print("Количество гласных букв в строке:", count)