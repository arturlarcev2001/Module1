

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = [len(x[0])-len(x[1]) for x in zp if len(x[0])!=len(x[1])]
second_result = [len(first[x]) == len(second[x]) for x in range(len(first))]
print(first_result)
print(second_result)