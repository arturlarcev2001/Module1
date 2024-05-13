
n = int(input('Введите число для поиска пар: '))
str_ = ''

for a in range(1, n):
    for b in range(a + 1, n):
        if n % (a + b) == 0 and a != b:
            str_ += str(a) + str(b)

print(str_)
