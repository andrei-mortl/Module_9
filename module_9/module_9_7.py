def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        is_prime = True
        if n < 2:
            return
        else:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print('Простое')
            else:
                print('Cоставное')
            return n
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
