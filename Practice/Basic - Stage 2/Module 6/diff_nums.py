def get_nums(string: str) -> str:
    return ''.join(set(num
                for num in string.replace(' ', '')
                if '0' <= num <= '9'))

def main():
    string = input('Введите строку: ')
    result = get_nums(string)
    if result:
        print(f'Различные цифры строки: {result}')
    else:
        print('Цифры не найдены')
if __name__ == '__main__':
    main()