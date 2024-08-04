import numpy as np
import math as m

a =  np.array([[1, 2, 3],
               [4, 5, 6]])

def end_line():
    print()

def liner():
    for x in range(20):
        print("*", end="")
    end_line()

def case1():
    global a
    print(f'We create an array "a" with 2 row, and 6 elems')
    for row in a:   
        print(f'row: {row}')
        for col in row:
            print(f'col: {col}')


def case2():
    global a
    print(f'Size of an array is {a.size}')
    print(f'{a.dtype} int" for integer, "32" for 32-bit')


def case3():
    numpy_array_range = np.arange(4)
    print(f'Numpy range function numpy.arange(4) -> {numpy_array_range}')


def case4():
    print("Let's try to sort numpy array")
    print("First create an array")
    some_arr = np.array([2, 4, 1, 5, 7, 15, 3])
    print(f"We have an unsorted array {some_arr}")
    print(f"It is now sorted {np.sort(some_arr)}")


def case5():
    print("We can even concatenate two arrays")
    print("Let's create two arrays")
    array_1, array_2 = np.array([1, 2, 3]), np.array([4, 5, 6])
    print(f"For example: array_1 = {array_1} and array_2 = {array_2}")
    print(f"It is now concatenated {np.concatenate((array_1, array_2))}")


def case6():
    print("Let's see if we can use lambda function on numpy arrays")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Create a array arr = {arr}")
    print(f"Now we need an annonymous function 'square'")
    square = lambda x: x * x
    new_arr = list(map(square, arr))
    print(f'We have an new_arr = {new_arr}')
    print(f'And the type of new_arr is {type(new_arr)}, yes it\' now a \'class list\'')
    
    
def case7():
    print("Last case of my project")
    print("And now let's try to use numpy array functions as in python")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"arr.max() = {arr.max()}, arr.min() = {arr.min()}, arr.sum = {arr.sum()}")

cases = [case1, case2, case3, case4, case5, case6, case7]

if __name__ == "__main__":
    for case in cases:
        liner()
        case()
        end_line()
