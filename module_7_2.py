
def custom_write(file_name, strings):
    string_number = 1
    result = {}
    file = open(file_name, "w+", encoding="utf-8")
    for string in strings:
        result[(string_number, file.tell())] = string
        file.write(string+"\n")
        string_number += 1
    file.close()
    return result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)



