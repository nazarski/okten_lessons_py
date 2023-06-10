import json


# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з
# ліва записувати не потрібно)

emails = open('emails.txt')
gmails = open('gmails.txt', 'w')

for line in emails:
    if line.endswith('@gmail.com\n'):
        gmail = line.split('\t').pop()
        gmails.write(gmail)

emails.close()
gmails.close()

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
class ShopListElement:
    _id = 1

    def __init__(self, item_id: int, name: str, price: float):
        self.price = price
        self.name = name
        self.item_id = item_id

    def __str__(self):
        return f'{"*" * 20}\nShop list element:\nid: {self.item_id}\nName: {self.name}\nPrice: {self.price}' \
               f'\n{"*" * 20}\n'

    def to_dict(self):
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, this_dict):
        if cls._id < this_dict['id']:
            cls._id = this_dict['id']
        return cls(item_id=this_dict['id'], name=this_dict['name'], price=this_dict['price'], )

    @classmethod
    def new_id(cls) -> int:
        cls._id += 1
        return cls._id


with open('shop_list.json', 'r+') as json_file:
    shop_list_data = json.load(json_file)
shop_list = [ShopListElement.from_dict(item) for item in shop_list_data]


#  * вивід всіх покупок
def list_all_items():
    for ele in shop_list:
        print(ele)


#  * має бути змога додавати покупку в книгу
def add_to_list():
    name = input('What do you want to buy?:')
    price = input('How mush will it cost?:')
    print('...processing')
    new_item = ShopListElement(item_id=ShopListElement.new_id(), name=name, price=float(price))
    shop_list.append(new_item)
    new_shop_list_data = [item.to_dict() for item in shop_list]
    with open('shop_list.json', 'w') as new_json_file:
        json.dump(new_shop_list_data, new_json_file, indent=4)
    print(new_item)


# * має бути змога шукати по будь якому полю покупку
def find_by_field():
    print('What field we should be looking at?:\n'
          'Type "1" to search by id\n'
          'Type "2" to search by name\n'
          'Type "3" to search by price')
    field_to_search = input('Your option:')

    match field_to_search:
        case ('1'):
            item_id = input('What id i should look for?:')
            search_by_id(int(item_id))
        case ('2'):
            name = input('What name i should look for?:')
            search_by_name(name)
        case ('3'):
            price = input('What price i should look for?:')
            search_by_price(float(price))
        case _:
            print('Sorry, but I need a number 1, 2 or 3')


def search_by_id(search_id: int):
    for item in shop_list:
        if item.item_id == search_id:
            print(item)
            return
    else:
        print("No matching item found.")


def search_by_name(search_name: str):
    for item in shop_list:
        if item.name == search_name:
            print(item)
            return
    else:
        print("No matching item found.")


def search_by_price(search_price: float):
    for item in shop_list:
        if item.price == search_price:
            print(item)
            return
    else:
        print("No matching item found.")


# * має бути змога показати найдорожчу покупку
def show_most_expensive():
    item_with_max_price = max(shop_list, key=lambda item: item.price)
    print("Item with maximum price:")
    print(item_with_max_price)


# * має бути можливість видаляти покупку по id
def remove_from_list():
    remove_id = input('What item do you want to remove?:')
    print('...processing')

    for item in shop_list:
        if item.item_id == int(remove_id):
            shop_list.remove(item)
            break

    new_shop_list_data = [item.to_dict() for item in shop_list]
    with open('shop_list.json', 'w') as new_json_file:
        json.dump(new_shop_list_data, new_json_file, indent=4)
    print('done')


# (ну і меню на це все)
def shop_list_menu():
    print('Hello, you nave several options:\n'
          '1. List all items\n'
          '2. Add to book\n'
          '3. Search through book\n'
          '4. Show the most expensive item\n'
          '5. Delete item bu its id')

    option = input('Your choice:')
    match option:
        case '1':
            list_all_items()
        case '2':
            add_to_list()
        case '3':
            find_by_field()
        case '4':
            show_most_expensive()
        case '5':
            remove_from_list()
        case _:
            print("Oops, someone can't read")


shop_list_menu()
# Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]
