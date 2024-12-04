def calculate_structure_sum(*args):
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
            total += i
        elif isinstance(i, str):
            total += len(i)
        elif isinstance(i, dict):
            total += calculate_structure_sum(*i.keys())
            total += calculate_structure_sum(*i.values())
        elif isinstance(i, (list, set, tuple)):
            total += calculate_structure_sum(*i)
    return total

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(data_structure))