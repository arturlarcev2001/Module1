

def apply_all_func(int_list, *functions):
    result = {}
    for f in functions:
        result [f.__name__] = f(int_list)
    return result
    
    
print(apply_all_func([1, 2, 3], max, min, len, sum, sorted))