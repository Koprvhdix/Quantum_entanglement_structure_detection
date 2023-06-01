from itertools import product

def min_union(M):
    min_union_set = set()
    min_union_len = float('inf')
    for combination in product(*M):
        union_set = set().union(*combination)
        if len(union_set) < min_union_len:
            min_union_set = union_set
            min_union_len = len(union_set)
    return min_union_set

# 示例
M = [[[1, 2], [3, 4]], [[2, 3], [4, 5]], [[3, 4], [5, 6]]]
result = min_union(M)
print(result)

def pair_to_qs(pair_list):
    qs_set = set()
    for pair in pair_list:
        qs_set.add(pair.split(":"))
    return list(qs_set)

data = [['a.b', 'c.d'], ['e.f', 'g.h']]
result = [[elem for s in row for elem in s.split('.')] for row in data]
print(result)