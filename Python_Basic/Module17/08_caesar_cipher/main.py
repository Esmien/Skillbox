from utils import num_validator

def cipher(data, k):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(alphabet[(alphabet.index(char) + k) % len(alphabet)]
                    if char in alphabet
                    else char
                    for char in data)

def main():
    text = input('Введите сообщение: ').lower()
    shift = num_validator('Введите сдвиг(положительное число - вправо, отрицательное - влево): ')
    print(cipher(text, shift))

if __name__ == '__main__':
    main()