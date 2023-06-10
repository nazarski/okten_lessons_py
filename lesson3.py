from abc import ABC, abstractmethod


# Створити клас Rectangle:

class Rectangle:
    # -він має приймати дві сторони x, y
    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x

    def square(self) -> int:
        return self.y * self.x

    # -описати поведінку на арифметични методи:

    # + сумма площин двох екземплярів класу
    def __add__(self, other):
        return self.square() + other.square()

    # - різниця площин двох екземплярів класу
    def __sub__(self, other):
        return self.square() - other.square()

    # == площин на рівність
    def __eq__(self, other):
        return self.square() == other.square()

    # != площин на не рівність
    def __ne__(self, other):
        return self.square() != other.square()

    # >, < меньше більше
    def __lt__(self, other):
        return self.square() < other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    # при виклику метода len() підраховувати сумму сторін
    def __len__(self):
        return self.x + self.y


#

square = Rectangle(4, 4)
rectangle = Rectangle(2, 6)


# print(square.square())
# print(rectangle.square())
# print(square + rectangle)
# print(square - rectangle)
# print(square == rectangle)
# print(square != rectangle)
# print(square < rectangle)
# print(square > rectangle)
# print(len(square))
# print(len(rectangle))

# ###############################################################################
#
# створити класс Human(name, age)
class Human:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name


# створити два класси Prince і Cinderella які наслідуються від Human:
# у попелюшки має бути ім'я, вік, розмір ноги
class Cinderella(Human):
    _counter: int = 0

    def __init__(self, name: str, age: int, foot_size: int, ):
        super().__init__(name, age)
        self.foot_size = foot_size

    # в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
    def __new__(cls, *args, **kwargs):
        cls._counter += 1
        return super().__new__(cls)

    # також має бути метод классу який буде виводити це значення
    @classmethod
    def get_count(cls) -> int:
        return cls._counter

    def __str__(self):
        return f"It's {self.name}, she's {self.age} y.o"


# у принца має бути ім'я, вік, та розмір знайденого черевичка,
class Prince(Human):
    def __init__(self, name: str, age: int, found_size: int, ):
        super().__init__(name, age)
        self.found_size = found_size

    # а також метод котрий буде приймати список попелюшок, та шукати ту саму
    def find_the_only_one(self, cinderella_list: list[Cinderella]) -> Cinderella | None:
        for i in cinderella_list:
            if i.foot_size == self.found_size:
                return i
        return None


prince = Prince('Charming', 44, 45)
cinderella_list = [Cinderella('Fiona', 71, 33), Cinderella('Calliope', 11, 43), Cinderella('Cassiope', 112, 45),
                   Cinderella('Marta', 32, 27), ]

print(prince.find_the_only_one(cinderella_list))


#
# ###############################################################################
#

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable, ):
    def print(self):
        print(self.name)

    def __init__(self, name: str):
        self.name = name


class Magazine(Printable):
    def print(self):
        print(self.name)

    def __init__(self, name: str):
        self.name = name


# 3) Створити клас Main в якому буде:
class Main:
    # - змінна класу printable_list яка буде зберігати книжки та журнали
    _printable_list: list[Printable] = []

    # - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що
    # передають є класом Book або Magazine інакше ігрнорувати додавання
    @classmethod
    def add(cls, other: Printable):
        if isinstance(other, Printable):
            cls._printable_list.append(other)

    # - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
    @classmethod
    def show_all_magazines(cls):
        for printable in cls._printable_list:
            if isinstance(printable, Magazine):
                printable.print()

    # - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
    @classmethod
    def show_all_books(cls):
        for printable in cls._printable_list:
            if isinstance(printable, Book):
                printable.print()


Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine2'))
Main.add(Book('book1'))
Main.add(Magazine('magazine3'))

Main.show_all_magazines()
Main.show_all_books()