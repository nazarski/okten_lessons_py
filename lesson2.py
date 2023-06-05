# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


def notebook():
    todo_list: list = []

    def add_todo(todo: str) -> list:
        todo_list.append(todo)
        return todo_list

    def get_all():
        return todo_list

    return add_todo, get_all


add_func, get_func = notebook()

print(get_func())
add_func('Todo todo')
print(get_func())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number: int) -> str:
    str_num = str(number)
    length = len(str_num)
    result = []
    for i in range(length):
        result.append(str_num[i] + '0' * (length - 1 - i))
    return ' + '.join(result)


expanded_numbers = expanded_form(8445)
print(expanded_numbers)


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

def decorator(func):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print('*' * 32)
        func()
        print('*' * 4 + 'Func was called ' + str(count) + ' times' + '*' * 4)

    return inner


@decorator
def print_first():
    print('First')


@decorator
def print_second():
    print('Second')


print_first()
print_first()
print_first()
print_second()
print_first()
print_second()


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]


def generate_list(max_num: int) -> list:
    result_list = []
    temp_list = []
    list_length = 1
    for i in range(1, max_num, 2):
        temp_list.append(i)
        if len(temp_list) == list_length:
            result_list.append(temp_list)
            list_length += 1
            temp_list = []
    return result_list


print(generate_list(50))


# прога, що виводить кількість кожного символа з введеної строки, наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
def count_chars():
    string_to_check = input('Give a string!: ')
    char_to_count = input('Now, what char i shall count?: ')
    counter = 0
    for char in string_to_check:
        if char == char_to_count:
            counter += 1

    print('We found ' + str(counter) + ' matches')


count_chars()
