import copy
import itertools

from partition import Partition
from partition_tools import all_partition
from tools import compute


if __name__ == "__main__":
    N = 10
    quantum_state = [''.join(['1' if i == j else '0' for j in range(10)]) for i in range(10)]
    print(quantum_state)
    P = [list(item) for item in itertools.combinations(quantum_state, 2)]
    print(P)

    partition_str_list = all_partition(list(range(1, 11)))
    young_diagrams = dict()
    for partition in partition_str_list:
        temp_partition = Partition(partition, N)
        if temp_partition.producible > 3:
            continue
        if temp_partition.type not in young_diagrams:
            young_diagrams[temp_partition.type] = list()
        young_diagrams[temp_partition.type].append(temp_partition)

    Gamma_list = list()
    key_set = set(young_diagrams.keys())
    max_type(key_set)
    for key in key_set:
        Gamma_list.extend(young_diagrams[key])

    print(len(Gamma_list))
    compute(P, Gamma_list)
