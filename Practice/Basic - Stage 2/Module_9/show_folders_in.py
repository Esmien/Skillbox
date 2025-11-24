import os

IGNORE = {'.git', '__pycache__', '.venv', 'venv', '.idea', 'node_modules', '.pytest_cache'}

def show_folders_in(project: str, level=0) -> None:
    """
    Выводит в консоль все содержимое каталога, рекурсивно обходя подкаталоги
    :param project: абсолютный путь до каталога
    :param level: уровень вложенности(для форматирования вывода)
    """
    try:
        items = os.listdir(project)
    except NotADirectoryError:
        return
    except PermissionError:
        print(f'Нет доступа к директории: {project}')
        return

    if not items:
        return
    dirs_and_files = [(item, os.path.join(project, item))
                       for item in items
                       if item not in IGNORE]
    directories = sorted((name, path)
                         for name, path in dirs_and_files
                         if os.path.isdir(path))
    files = sorted(name
                   for name, path in dirs_and_files
                   if os.path.isfile(path))

    for name, path in directories:
        print(f'{"\t" * level}📂 {name}')
        show_folders_in(path, level + 1)
    for f in files:
        f_path = os.path.join(project, f)
        size = os.path.getsize(f_path)
        print(f'{"\t" * level}📄 {f} - {round(size / 1024, 2)} Кб')

def main():
    path_to_project = os.path.abspath(os.path.join('..', '..'))
    show_folders_in(path_to_project)

if __name__ == '__main__':
    main()