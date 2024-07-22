

def is_prime(func):
    def wrapper(a, b, c):
        n = a + b + c
        l = []
        for i in range(1, 10):
            if n % i == 0:
                l.append(i)
        if len(l) > 2:
            return "Составное"
        else:
            return "Простое"
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 3, 6))
