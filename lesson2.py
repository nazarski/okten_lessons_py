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
