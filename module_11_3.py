# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  # - Тип объекта.
  # - Атрибуты объекта.
  # - Методы объекта.
  # - Модуль, к которому объект принадлежит.
  # - Другие интересные свойства объекта, учитывая его тип (по желанию).


# Пример работы:
# number_info = introspection_info(42)
# print(number_info)

# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}


def introspection_info(obj):
    type_  = type(obj).__name__
    attributes = [atr for atr in dir(obj) if not callable(getattr(obj, atr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module_name = obj.__class__.__module__
    dict_ = {
            'type:': type_,
            'attributes:': attributes,
            'methods:':  methods,
            'module:': module_name
            }
    return dict_



class MyClass:
    a = 10
    def __init__(self):
        self.b = 0

objb = MyClass()

print(introspection_info(objb))




    
