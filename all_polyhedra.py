import numpy as np

from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions
from tools import m_n_part

p = 0.47

rho = [[0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.25, 0.25, 0. ,  0.25, 0.  , 0.  , 0.   , 0.25 , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.25, 0.25, 0. ,  0.25, 0.  , 0.  , 0.   , 0.25 , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.25, 0.25, 0. ,  0.25, 0.  , 0.  , 0.   , 0.25 , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.25, 0.25, 0. ,  0.25, 0.  , 0.  , 0.   , 0.25 , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ],
  [ 0.0 , 0.  , 0.  , 0. ,  0.  , 0.  , 0.  , 0.   , 0.   , 0.  , 0. ,  0. ,  0.  , 0. ,  0. ,  0. ] ]

matrix = p * np.matrix(rho) + ((1 - p) / 16) * np.eye(16)

N = 4

k = 3

Gamma = generate_k_partitionable_partitions(N, k)

raw_P = list()

for i in range(15):
    for j in range(i + 1, 16):
        raw_P.append(["{:04b}".format(i), "{:04b}".format(j)])

print(raw_P)

P = list()

for item in raw_P:
    count = 0
    for i in range(len(item[0])):
        if item[0][i] != item[1][i]:
            count += 1
    if count == 2:
        P.append([item[0], item[1]])

print(P)

number_set = set()
# number_set.add((N ** 2) ** 2 + 1)
number_dict = dict()

h_index = 1

positive_number = set()
# positive_number.add((N ** 2) ** 2 + 1)
for partition in Gamma:
    for quantum_pair in P:
        pair_number_1 = int(quantum_pair[0], 2)
        pair_number_2 = int(quantum_pair[1], 2)
        number_set.add(pair_number_1 * (N ** 2) + pair_number_2)
        number_dict[pair_number_1 * (N ** 2) + pair_number_2] = [pair_number_1 + 1, pair_number_2 + 1]
        for part in partition.partition_by_list:
            number1 = int(m_n_part(quantum_pair[0], quantum_pair[1], part), 2)
            number2 = int(m_n_part(quantum_pair[1], quantum_pair[0], part), 2)
            number_set.add(number1 * (N ** 2) + number1)
            number_set.add(number2 * (N ** 2) + number2)
            positive_number.add(number1 * (N ** 2) + number1)
            positive_number.add(number2 * (N ** 2) + number2)
            number_dict[number1 * (N ** 2) + number1] = [number1 + 1, number1 + 1]
            number_dict[number2 * (N ** 2) + number2] = [number2 + 1, number2 + 1]

number_list = sorted(number_set)
print(number_list)
print(number_dict)

length = len(number_list)

result_set = set()
for i in positive_number:
    list_1 = [0] * length
    list_1[number_list.index(i)] = -1
    result_set.add("HalfSpace(" + str(list_1) + ", 0)")
    # list_2 = [0] * length
    # list_2[number_list.index(i)] = 1
    # result_set.add("HalfSpace(" + str(list_2) + ", 1)")

print("h_" + str(h_index) + " = hrep([" + (",".join(result_set)) + "])")
h_index += 1

partition_result_list = list()
for partition in Gamma:
    current_set = set()
    for quantum_pair in P:
        pair_number_1 = int(quantum_pair[0], 2)
        pair_number_2 = int(quantum_pair[1], 2)
        for part in partition.partition_by_list:
            list_1 = [0.0] * length
            list_1[number_list.index(pair_number_1 * (N ** 2) + pair_number_2)] = 1.0
            number1 = int(m_n_part(quantum_pair[0], quantum_pair[1], part), 2)
            number2 = int(m_n_part(quantum_pair[1], quantum_pair[0], part), 2)
            list_1[number_list.index(number1 * (N ** 2) + number1)] = -0.5
            list_1[number_list.index(number2 * (N ** 2) + number2)] = -0.5
            current_set.add("HalfSpace(" + str(list_1) + ", 0)")

    print("h_" + str(h_index) + " = hrep([" + (",".join(current_set)) + "])")
    h_index += 1

rho_list = [0.0] * length
for index_list in number_dict:
    x = number_dict[index_list][0] - 1
    y = number_dict[index_list][1] - 1
    rho_list[number_list.index(x * (N ** 2) + y)] = matrix[x, y]

next_number_set = set()
next_number_set.add((N ** 2) ** 2 + 1)

for i in range(1, h_index):
    print("p" + str(i) + " = polyhedron(h_" + str(i) + ", lib)")
    if i > 1:
        print("p_" + str(i) + " = intersect(p1, p" + str(i) + ")")

print("Pch = convexhull(" + ",".join(["p_" + str(i) for i in range(2, h_index)]) + ")")

print(rho_list)