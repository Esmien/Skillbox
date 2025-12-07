import os


INPUT_FILE_PATH = os.path.abspath(os.path.join('.', 'zen.txt'))

def reverse_file(file_path: str) -> None:
    """Выводит на экран строки файла в обратном порядке"""
    with open(file_path, 'r') as f:
        reversed_text = f.readlines()[::-1]
        for line in reversed_text:
            print(line.strip())

def main():
    reverse_file(INPUT_FILE_PATH)

if __name__ == '__main__':
    main()