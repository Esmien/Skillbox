def selection_sort(my_list):
    for min_index in range(len(my_list)):
        for curr_index in range(min_index, len(my_list)):
            if my_list[curr_index] < my_list[min_index]:
                my_list[min_index], my_list[curr_index] = my_list[curr_index], my_list[min_index]
    return my_list

my_list = [9, 5, 8, 4, 3, 7, 1]
print(selection_sort(my_list))