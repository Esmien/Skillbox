def num_validator(message, min_value = 34, max_value = 45):
    """Валидирует ввод. Нельзя ввести что-либо, кроме чисел от 34 до 45 в качестве размера роликов"""
    while True:
        try:
            num = int(input(message))
            if not (min_value <= num <= max_value):
                print(f'Ошибка! Нужно ввести положительное число({min_value} - {max_value})')
                continue
            return num
        except ValueError:
            print(f'Ошибка! Требуется ввести число({min_value} - {max_value})')
def count_of_luckers(skates, people):
    """Сортирует оба входных списка по возрастанию и сравнивает их попарно. Если Нога маленькая, берем следующего человека под ролики,
    если ролики малы, то подбираем дальше ролики под человека"""
    count = 0
    skate_index = 0
    people_index = 0
    skates_sorted = sorted(skates)
    people_sorted = sorted(people)

    while people_index < len(people_sorted) and skate_index < len(skates):
        if skates_sorted[skate_index] == people_sorted[people_index]:
            count += 1
            people_index += 1
            skate_index += 1
        elif skates_sorted[skate_index] < people_sorted[people_index]:
            skate_index += 1
        else:
            people_index += 1
    return count
def main():
    skates_list = []
    people = []
    cnt_skates = num_validator('Кол-во коньков: ', 1, 100)
    for i in range(1, cnt_skates + 1):
        skates_list.append(num_validator(f'Размер {i}-й пары: '))
    print()
    cnt_people = num_validator('Кол-во людей: ', 1, 150)
    for i in range(1, cnt_people + 1):
        people.append(num_validator(f'Размер ноги {i}-го человека: '))
    print(f'Наибольшее кол-во людей, которые могут взять ролики: {count_of_luckers(skates_list, people)}')

if __name__ == '__main__':
    main()