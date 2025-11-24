def get_power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * get_power(x, n - 1)

print(get_power(1.5, 5))