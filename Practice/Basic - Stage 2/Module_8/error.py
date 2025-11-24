import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
mutable_list = nums_list.copy()
some_dict = {1: 'text', 2: 'another text'}
mutable_dict = some_dict.copy()
uniq_nums = {1, 2, 3}
mutable_uniq_nums = uniq_nums.copy()
common_dict = {1: mutable_dict, 2: mutable_dict, 3: mutable_uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)
print(uniq_nums)
print(nums_list)
print(some_dict)