#Задача 4.
# Недоделка-2
# Вы всё так же работаете в конторе по разработке игр и смотрите программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.
#
# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако вас попросили немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится от него, мягко говоря, не по себе.
#
# Постарайтесь разделить логику кода на три отдельные логические части (функции):
#
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).
# Что нужно сделать
# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
#
# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
#
#
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10
#
#
# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#     second_n = int(input("\nВведите второе число: "))
#     second_num_count = 0
#     temp = second_n
#
#
#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("Во втором числе меньше четырёх цифр.")
#     else:
#         last_digit = second_n % 10
#         first_digit = second_n // 10 ** (second_num_count - 1)
#         between_digits = second_n % 10 ** (second_num_count - 1) // 10
#         second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('Изменённое второе число:', second_n)
#         print('\nСумма чисел:', first_n + second_n)
# Что оценивается
# Программа разбита на несколько функций.
# Выполнены условия по организации основного тела программы.
def count_numbers(num):
    result = 0
    while num > 0:
        result += 1
        num = num // 10
    return result
def change_number(num):
    count = count_numbers(num)
    last_digit = num % 10
    first_digit = num // 10 ** (count - 1)
    between_digits = num % 10 ** (count - 1) // 10
    return last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit

def main():
    while True:
        try:
            first_num = int(input('Введите число не меньше 100: '))
            second_num = int(input('Введите число не меньше 1000: '))
            if count_numbers(first_num) < 3 or count_numbers(second_num) < 4:
                print("Неподходящее число. Попробуйте ещё раз.")
                continue
        except ValueError:
            print('Ошибка! Нужно ввести целые числа')
            continue
        break
    first_changed_number = change_number(first_num)
    second_changed_number = change_number(second_num)
    print(f'Измененное первое число: {first_changed_number}')
    print(f'Измененное второе число: {second_changed_number}')
    print('\nСумма чисел:', first_changed_number + second_changed_number)

main()