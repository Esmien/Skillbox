horizontal = '-'
vertical = '|'
row = 'O'
print(horizontal * 10)
for _ in range(4):
    print(vertical, end='')
    print(row * 8, end='')
    print(vertical)
print(horizontal * 10)