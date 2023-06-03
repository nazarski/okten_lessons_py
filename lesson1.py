# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
st:str = 'as 23 fdfdg544' #введена строка
# 2,3,5,4,4        #вивело в консолі.

digits = []
for i in st:
   if i.isdigit():
       digits.append(i)

result = ','.join(digits)
print(result)


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
# так як вони написані
# наприклад:
st = 'as 23 fdfdg544 34'  # введена строка
#   23, 544, 34              #вивело в консолі


tempChar = ''
result = []
for char in st:
    if char.isdigit():
        tempChar += char
    elif tempChar:
        result.append(tempChar)
        tempChar = ''
if tempChar:
    result.append(tempChar)

print(','.join(result))

# #################################################################################

# list comprehension

# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
listChars = []
for char in greeting:
    listChars.append(char.upper())
print(listChars)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
listSqDigits = []
for i in range(50):
    if i % 2:
        listSqDigits.append(i ** 2)
print(listSqDigits)


# function

# - створити функцію яка виводить ліст
def show_list(list_to_print):
    print(list_to_print)


show_list(['cc', 'ppp', 'fff'])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def find_max(num1, num2, num3):
    max_num = max(num1, num2, num3)
    print(max_num)
    return max_num


find_max(1, 9, 18)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def find_max_and_min(*args):
    min_num = min(args)
    max_num = max(args)
    print("Найбільше число:", max_num)
    return min_num


find_max_and_min(1, 9, 18)


# - створити функцію яка повертає найбільше число з ліста
def find_max_from_list(num_list):
    return max(num_list)


max_num = find_max_from_list([1, 9, 18, 33, 66])
print(max_num)


# - створити функцію яка повертає найменьше число з ліста

def find_min_from_list(num_list):
    return min(num_list)


min_num = find_min_from_list([1, 9, 18, 33, 66])
print(max_num)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def find_sum_from_list(num_list):
    return sum(num_list)


sum_num = find_sum_from_list([1, 9, 18, 33, 66])
print(max_num)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def find_avg_from_list(num_list):
    return find_sum_from_list(num_list) / len(num_list)


avg_num = find_avg_from_list([1, 9, 18, 33, 66])
print(max_num)

# ################################################################################################
# 1)Дан list:
raw_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
raw_min = min(raw_list)
unique_list = list(set(raw_list))
for i in range(3, len(raw_list), 4):
    raw_list[i] = 'X'


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def draw_square(side: int) -> str:
    square_string = '*' * side + '\n'
    for num in range(side - 2):
        square_string += '*' + ' ' * (side - 2) + '*' + '\n'
    square_string += '*' * side
    return square_string


square = draw_square(16)

print(square)


# 3) вывести табличку множення за допомогою цикла while

def show_multiplication_table():
    multiplication = ''
    row = 1
    while row < 11:
        basic_number = 1
        while basic_number < 10:
            num = basic_number * row
            space = '  ' if num < 10 else ' '
            multiplication += ' ' + str(num) + space
            basic_number += 1
            row += 1
            multiplication += '\n'
            print(multiplication)


# 4) переробити це завдання під меню


def menu() -> str:
    print(
        '1. Знайти min число в лісті',
        '2. Видалити всі дублікати',
        '3. Замінити кожне четверте значення на "Х"',
        '4. Вивести елемент ліста, який ближче всього до середнього значення ліста',
        '5. Вихід',
        sep='\n'
    )
    return input('Зробіть свій вибір: ')


list_to_process = [1, 33, 52, 664, 6, 224, 667, 77, 77, 33, 1]


def choose_action():
    selection = menu()
    match selection:
        case '1':
            value = find_min_from_list(list_to_process)
            print(value)
        case '2':
            value = list(set(list_to_process))
            print(value)
        case '3':
            temp_list = list_to_process.copy()
            for index in range(3, len(temp_list), 4):
                temp_list[index] = 'X'
            print(temp_list)
        case '4':
            avg = find_avg_from_list(list_to_process)
            value = min(list_to_process, key=lambda x: abs(x - avg))
            print(value)
        case _:
            print('Виходю')


choose_action()
