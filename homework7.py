my_dict = {'Andrew' : 2002, 'Arthur' : 2001, 'Maxim' : 2003}
print(my_dict)
print(my_dict['Andrew'])
my_dict['John'] = 1958
my_dict['Bred'] = 2072
del my_dict['Andrew']
print(my_dict)

my_set = {1, 1, 2, 3, '1', True}
print(my_set)
my_set.add(5)
my_set.add('George Washington')
my_set.discard(1)
print(my_set)
