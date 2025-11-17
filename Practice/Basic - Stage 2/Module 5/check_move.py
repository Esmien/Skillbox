def check_move_list(list1, list2):
    if len(list1) == len(list2):
        result = list1 * 2
        index = result.find(list2) #ищем подстроку 2 в удвоенной строке 1, если ок, то получаем индекс(сдвиг)
                                   #если не ок, то получаем -1
        if index != -1:
            return f"Первая строка получается из второй со сдвигом {index}"
    return "Первую строку нельзя получить из второй с помощью циклического сдвига."
first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
print(check_move_list(first_string, second_string))