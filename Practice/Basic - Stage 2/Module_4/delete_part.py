nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 3
b = 7
nums = nums[:a] + nums[b + 1:]
print(nums)