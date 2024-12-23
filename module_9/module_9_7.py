def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                res = 'Составное'
            else:
                res =  'Простое'
            print(res)
            return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
