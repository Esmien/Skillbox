raw_menu = input('Доступное меню: ')
menu = ', '.join(raw_menu.split(';')).title()
print(menu)