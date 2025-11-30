import os


LIB_PATH = os.path.abspath(os.path.join('..', 'Module_7'))
OUTPUT_FILENAME = os.path.abspath(os.path.join('.', 'scripts.txt'))

def get_data(filename_path: str) -> list[str]:
    """
    Считывает данные из файла
    :param filename_path: путь к файлу
    :return: список строк из файла с форматированием
    """
    with open(filename_path, 'r', encoding='utf-8') as f:
        file = [os.path.basename(filename_path) + '\n', '*' * 40 + '\n']
        file.extend(f.readlines())
        file.append('\n' + '*' * 40 + '\n')
        return file

def write_data(filename_path: str, data: list[str]) -> None:
    """
    Записывает данные в файл
    :param filename_path: путь к файлу
    :param data: данные для записи
    """

    with open(filename_path, 'w', encoding='utf-8') as f:
        f.writelines(data)

def get_files(lib_path: str) -> list[str]:
    """
    Получает список файлов в директории
    :param lib_path: путь к директории
    :return: список файлов в директории
    """
    return [file for file in os.listdir(lib_path)
             if os.path.isfile(os.path.join(lib_path, file)) and file.endswith('.py')]

def main():
    files = get_files(LIB_PATH)
    all_data = []
    for index, file in enumerate(files, start=1):
        file_data = get_data(os.path.join(LIB_PATH, file))
        all_data.append(str(index) + '. ')
        all_data.extend(file_data)
        all_data.append('\n')
    write_data(OUTPUT_FILENAME, all_data)

if __name__ == '__main__':
    main()