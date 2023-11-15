from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions
from tools import m_n_part

N = 3

k = 2

# P = [['000000', '111111']]

# P = [['0001', '0010'], ['0001', '0100'], ['0001', '1000'],
#      ['0010', '0100'], ['0010', '1000'], ['0100', '1000']]

# P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
#      ['10011', '11100']]

P = [['001', '010'], ['001', '100'], ['010', '100']]

# Gamma = generate_k_producible_partitions(N, k)
Gamma = generate_k_partitionable_partitions(N, k)

number_set = set()
number_set.add((N ** 2) ** 2 + 1)
number_dict = dict()

h_index = 1

positive_number = set()
positive_number.add((N ** 2) ** 2 + 1)
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

            # list_1[number_list.index(number1 * (N ** 2) + number1)] = -1
            # list_1[number_list.index(number2 * (N ** 2) + number2)] = -0.25
            # current_set.add("HalfSpace(" + str(list_1) + ", 0)")
            #
            # list_1[number_list.index(number1 * (N ** 2) + number1)] = -0.25
            # list_1[number_list.index(number2 * (N ** 2) + number2)] = -1
            # current_set.add("HalfSpace(" + str(list_1) + ", 0)")

    print("h_" + str(h_index) + " = hrep([" + (",".join(current_set)) + "])")
    h_index += 1

next_number_set = set()
next_number_set.add((N ** 2) ** 2 + 1)

for i in range(1, h_index):
    print("p" + str(i) + " = polyhedron(h_" + str(i) + ", lib)")
    if i > 1:
        print("p_" + str(i) + " = intersect(p1, p" + str(i) + ")")

print("Pch = convexhull(" + ",".join(["p_" + str(i) for i in range(2, h_index)]) + ")")

plane_set = set()
for quantum_pair in P:
    list_1 = [0.0] * length
    pair_number_1 = int(quantum_pair[0], 2)
    pair_number_2 = int(quantum_pair[1], 2)
    next_number_set.add(pair_number_1 * (N ** 2) + pair_number_2)

    # W 4
    # list_1[number_list.index(pair_number_1 * (N ** 2) + pair_number_2)] = -4.0
    # list_1[-1] = 1.0
    # plane_set.add("HyperPlane(" + str(list_1) + ", 0)")

    # W 3
    list_1[number_list.index(pair_number_1 * (N ** 2) + pair_number_2)] = -3.0
    list_1[-1] = 1.0
    plane_set.add("HyperPlane(" + str(list_1) + ", 0)")

    # GHZ
    # list_1[number_list.index(pair_number_1 * (N ** 2) + pair_number_2)] = -2.0
    # list_1[-1] = 1.0
    # plane_set.add("HyperPlane(" + str(list_1) + ", 0)")

    # CLUSTER
    # list_1[number_list.index(pair_number_1 * (N ** 2) + pair_number_2)] = -4.0
    # list_1[-1] = 1.0
    # plane_set.add("HyperPlane(" + str(list_1) + ", 0)")

    if pair_number_1 * (N ** 2) + pair_number_1 in number_set:
        next_number_set.add(pair_number_1 * (N ** 2) + pair_number_1)
        list_2 = [0.0] * length

        # # W 4
        # list_2[number_list.index(pair_number_1 * (N ** 2) + pair_number_1)] = 16.0
        # list_2[-1] = -3.0
        # plane_set.add("HyperPlane(" + str(list_2) + ", 1)")

        # W 3
        list_2[number_list.index(pair_number_1 * (N ** 2) + pair_number_1)] = 24.0
        list_2[-1] = -5.0
        plane_set.add("HyperPlane(" + str(list_2) + ", 1)")

        # GHZ
        # list_2[number_list.index(pair_number_1 * (N ** 2) + pair_number_1)] = 64.0
        # list_2[-1] = -31.0
        # plane_set.add("HyperPlane(" + str(list_2) + ", 1)")

        # CLUSTER
        # list_2[number_list.index(pair_number_1 * (N ** 2) + pair_number_1)] = 32.0
        # list_2[-1] = -7.0
        # plane_set.add("HyperPlane(" + str(list_2) + ", 1)")

    if pair_number_2 * (N ** 2) + pair_number_2 in number_set:
        next_number_set.add(pair_number_2 * (N ** 2) + pair_number_2)
        list_3 = [0.0] * length

        # W 4
        # list_3[number_list.index(pair_number_2 * (N ** 2) + pair_number_2)] = 16.0
        # list_3[-1] = -3.0
        # plane_set.add("HyperPlane(" + str(list_3) + ", 1)")

        # W 3
        list_3[number_list.index(pair_number_1 * (N ** 2) + pair_number_1)] = 24.0
        list_3[-1] = -5.0
        plane_set.add("HyperPlane(" + str(list_3) + ", 1)")

        # GHZ
        # list_3[number_list.index(pair_number_2 * (N ** 2) + pair_number_2)] = 64.0
        # list_3[-1] = -31.0
        # plane_set.add("HyperPlane(" + str(list_3) + ", 1)")

        # CLUSTER
        # list_3[number_list.index(pair_number_2 * (N ** 2) + pair_number_2)] = 32.0
        # list_3[-1] = -7.0
        # plane_set.add("HyperPlane(" + str(list_3) + ", 1)")

for i in range(len(number_list)):
    if number_list[i] not in next_number_set:
        list_4 = [0.0] * length

        # W 4
        # list_4[i] = 16.0
        # list_4[-1] = 1
        # plane_set.add("HyperPlane(" + str(list_4) + ", 1)")

        # W 3
        list_4[i] = 8.0
        list_4[-1] = 1
        plane_set.add("HyperPlane(" + str(list_4) + ", 1)")

        # GHZ
        # list_4[i] = 64.0
        # list_4[-1] = 1
        # plane_set.add("HyperPlane(" + str(list_4) + ", 1)")

        # CLUSTER
        # list_4[i] = 32.0
        # list_4[-1] = 1
        # plane_set.add("HyperPlane(" + str(list_4) + ", 1)")

pl_index = 1
for item in plane_set:
    print("pl_" + str(pl_index) + " = " + item)
    pl_index += 1

print("pl = hrep([" + ",".join(["pl_" + str(i) for i in range(1, pl_index)]) + "])")
print("Pint = intersect(Pch, pl)")
