import os

IGNORE = {'.git', '__pycache__', '.venv', 'venv', '.idea', 'node_modules', '.pytest_cache'}

def dir_validator(path: str) -> list[str] | None:
    """
    Проверяет наличие и доступ к искомой директории
    :param path: абсолютный путь до директории
    :return: список содержимого директории
    """
    try:
        return os.listdir(path)
    except NotADirectoryError:
        print(f'{path} не является директорией')
        return []
    except PermissionError:
        print(f'Нет доступа к директории: {path}')
        return []

class FileManager:
    def __init__(self, path) ->  None:
        self.path = path
        self.tree = self._build_tree(self.path)

    def _build_tree(self, path: str, level: int = 0) -> dict:
        """
        Строит дерево вложенных папок относительно переданного пути
        :param path: путь, корень дерева
        :param level: глубина вложенности
        :return: готовое дерево(словарь) со структурой папок/файлов
        """
        items = dir_validator(path)
        if not items:
            return {}
        items = [item for item in items if item not in IGNORE]
        dirs = sorted(item
                      for item in items
                      if os.path.isdir(os.path.join(path, item)))
        files = sorted(item
                       for item in items
                       if os.path.isfile(os.path.join(path, item)))
        tree = {
            path: {
                'level': level,
                'subdirs': [],
                'files': [(name, os.path.join(path, name)) for name in files],
            }
        }

        for dir_name in dirs:
            dir_path = os.path.join(path, dir_name)
            tree[path]['subdirs'].append((dir_name, dir_path))
            subtree = self._build_tree(dir_path, level + 1)
            tree.update(subtree)

        return tree

    def _print_tree(self, path: str) -> None:
        """
        Рекурсивно обходит дерево и печатает его структуру
        :param path: точка, относительно которой делается обход
        """
        if path not in self.tree:
            return

        node = self.tree[path]
        level = node['level']

        for file_name, file_path in node['files']:
            size = os.path.getsize(file_path)
            print(f'{"\t" * level}📄 {file_name} - {round(size / 1024, 2)} Кб')
        for dir_name, dir_path in node['subdirs']:
            print(f'{"\t" * level}📂 {dir_name}')
            self._print_tree(dir_path)
    def show_dir_items(self) -> None:
        self._print_tree(self.path)

    def find_file_or_directory(self, name: str) -> None:
        """
        Ищет указанный файл или папку в структуре папок/файлов
        :param name: название искомого элемента
        """
        found_files = []
        found_dirs = []

        for path, node in self.tree.items():
            for file_name, file_path in node['files']:
                if file_name == name:
                    found_files.append((file_name, file_path))
            for dir_name, dir_path in node['subdirs']:
                if dir_name == name:
                    found_dirs.append((dir_name, dir_path))

        if found_files:
            print('Найдены файлы:')
            for found_name, found_path in found_files:
                size = os.path.getsize(found_path)
                print(f'\t📄 {found_name}({found_path}) - {round(size / 1024, 2)} Кб')
        if found_dirs:
            print('Найдены папки:')
            for found_name, found_path in found_dirs:
                print(f'\t📂 {found_name}({found_path})')

        if not found_files and not found_dirs:
            print(f'Файл или папка с именем {name} не найдены')

def main():
    path_to_project = os.path.abspath(os.path.join('..', '..'))
    manager = FileManager(path_to_project)
    manager.show_dir_items()
    manager.find_file_or_directory('Module 6')
    manager.find_file_or_directory('contacts.py')

if __name__ == '__main__':
    main()