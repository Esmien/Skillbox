import os
from utils import dir_validator


BYTES = 1024


def read_dir(path: str, items: list[str]) -> tuple[int, int, int] | None:
    """
    Считает количество файлов и подкаталогов в указанном каталоге
    :param path: абсолютный путь до директории
    :param items: список содержимого директории
    :return: кортеж из количества файлов, директорий и общей суммы размеров файлов
    """
    count_files = 0
    count_dirs = 0
    total_size = 0

    dirs = [item for item in items
            if os.path.isdir(os.path.join(path, item))]
    files = [(item, os.path.getsize(os.path.join(path, item)))
             for item in items
             if os.path.isfile(os.path.join(path, item))]
    count_files += len(files)
    count_dirs += len(dirs)
    total_size += sum(size for _, size in files)

    for dir_ in dirs:
        dir_path = os.path.join(path, dir_)
        subdir_items = dir_validator(dir_path)
        if subdir_items is not None:
            result = read_dir(dir_path, subdir_items)
            count_files += result[0]
            count_dirs += result[1]
            total_size += result[2]

    return count_files, count_dirs, total_size

def main():
    size_name = 'Байт'

    while True:
        dir_path = os.path.join(os.sep, input('Введите путь до папки: '))
        items = dir_validator(dir_path)
        if items is None:
            continue
        count_files, count_dirs, total_size = read_dir(dir_path, items)
        break


    if BYTES ** 1 <= total_size <= BYTES ** 2:
        total_size = round(total_size / BYTES, 2)
        size_name = 'К' + size_name
    elif BYTES ** 2 <= total_size <= BYTES ** 3:
        total_size = round(total_size / BYTES ** 2, 2)
        size_name = 'М' + size_name
    elif BYTES ** 3 <= total_size <= BYTES ** 4:
        total_size = round(total_size / BYTES ** 3, 2)
        size_name = 'Г' + size_name


    print(f'Читаю каталог {dir_path}')
    print(f'Количество файлов: {count_files}')
    print(f'Количество подкаталогов: {count_dirs}')
    print(f'Общий размер каталога: {total_size} {size_name}')

if __name__ == '__main__':
    main()