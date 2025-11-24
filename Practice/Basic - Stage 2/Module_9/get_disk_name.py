import os

def get_disk_name() -> str:
    """Возвращает название корневой директории, с которой запущен этот файл
            Returns: имя диска
    """
    script_path = os.path.abspath(__file__)
    disk = os.path.splitdrive(script_path)[0]
    return disk + os.path.sep

def main() -> None:
    """Точка входа в программу"""
    root_name = get_disk_name()
    print('Корень диска:', root_name)

if __name__ == '__main__':
    main()