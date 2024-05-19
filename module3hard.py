data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    sum_ = 0
    for item in data:
        if isinstance(item, list | tuple | set):
          sum_ += calculate_structure_sum(item)
        if isinstance(item, dict):
          for i in item:
            sum_ += len(i)
          sum_ += sum(item.values())
        if isinstance(item, int):
          sum_ += item
        if isinstance(item, str):
          sum_ += len(item)
    return sum_

result = calculate_structure_sum(data_structure)
print(result)
