

def personal_sum(numbers):
    sums = 0
    incorrect_data = 0
    for n in numbers:
        try:
            sums += n
        except TypeError:
            incorrect_data += 1
    return (sums, incorrect_data)
    

def calculate_average(numbers):
    try:
        try:
            sums = personal_sum(numbers)
            if isinstance(sums, tuple):
                aver = sums[0] / (len(numbers)-sums[1])
                return aver
            else:
                aver = sums / len(numbers)
                return aver
        except ZeroDivisionError:
            return 0
    except:
            return None

    
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

