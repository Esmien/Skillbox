import random
tuple_1 = tuple(random.randint(0, 6) for _ in range(10))
tuple_2 = tuple(random.randint(-5, 1) for _ in range(10))
tuple_3 = tuple_1 + tuple_2
zeros = tuple_3.count(0)
print(tuple_3)
print(zeros)