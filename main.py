from pympler import asizeof

example1 = [1, 2, 3, 4, 5, 6]
example2 = [2, 4, 5, 6, 7, 8, 9, 0, 2, 3, 4, 5, 6, 7, 7, 3, 4, 5, 6, 7]
print(asizeof.asizeof(example1))
print(asizeof.asizeof(example2))