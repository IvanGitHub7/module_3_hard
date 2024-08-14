data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    sum_ = 0
    for i in args:
        if isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, (int, float)):
            sum_ += i
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for j in i.items():
                sum_ += calculate_structure_sum(j)
    return sum_
    
result = calculate_structure_sum(data_structure)
print(result)