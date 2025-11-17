from utils import num_validator
num = num_validator('Введите число: ', 0)
result = {i: i**2 for i in range(1, num +1)}
for key, value in result.items():
    print(f'{key}^2 = {value}')