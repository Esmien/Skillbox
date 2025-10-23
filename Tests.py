def check_number(number):
    return count_number_len(number) > 4

def count_number_len(x):
    count = 0
    while x:
        count += 1
        x //= 10

x = 1234
if check_number(x):
    print("1")
else:
    print("2")