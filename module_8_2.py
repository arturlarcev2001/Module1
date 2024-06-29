

class Integer(Exception):
    def __init__(self, message, extra_message):
        self.message = message
        self.extra_message = extra_message

class String(Exception):
    def __init__(self, message, extra_message):
        self.message = message
        self.extra_message = extra_message


def generate_raise(a):
    if isinstance(a, int):
        raise Integer(f"Использован целый тип аргумента", {"a": a})
    elif isinstance(a, str):
        raise String(f"Использован строковый тип аргумента", {"a": a})
    else:
        print("Нет исключений")


def try_func(func, value):
    try:
        func(value)
    except (Integer, String) as e:
        print(e.message)
        print(e.extra_message)
        print("Конец исключения")
    finally:
        print("---")

try_func(generate_raise, [])
