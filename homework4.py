immutable_var = (1, '1', True, [1, 2], (1, 2, 3))
print(immutable_var)
#immutable_var[0] = 200; Кортежи являются не изменямым типом данных, поэтому данное присваивание ошибочно
mutable_list = [1 , '2', True, (1, 4), [2, 3]]
mutable_list[0] = 2
mutable_list[1] = '1'
mutable_list[2] = False
mutable_list[3] = [1, 4]
mutable_list[4] = (3, 2)
print(mutable_list)