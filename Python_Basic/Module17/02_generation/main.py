from utils import num_validator
length = num_validator('Введите длину списка: ', 0)
result = [1 if i % 2 == 0 else i % 5 for i in range(length)]
print('Результат:', result)