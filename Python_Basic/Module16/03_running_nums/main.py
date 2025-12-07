def num_validator(message):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print('Ошибка! Требуется ввести число')
            continue
        return num
def move_list(data, num):
    """Сдвигает список вправо, если указан положительный сдвиг, влево, если отрицательный.
    Также работает со сдвигом, превышающим длинну списка"""
    num %= len(data)
    return data[-num:] + data[:-num]

def main():
    start_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    input_msg = 'Сдвиг: '
    rotate = num_validator(input_msg)
    print(f'Изначальный список: {start_list}')
    print(f'Сдвинутый список: {move_list(start_list, rotate)}')

if __name__ == '__main__':
    main()
