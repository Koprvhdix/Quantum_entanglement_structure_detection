import copy
import itertools

from partition import Partition
from partition_tools import generate_k_stretchable_partitions, max_partition_set
from tools import compute


def all_partition(elements):
    partition_list = list()
    partition_list.append([elements])
    if len(elements) == 1:
        return partition_list

    for count in range(0, len(elements) - 1):
        for item in itertools.combinations(elements[1:], count):
            the_part = list(item) + [elements[0]]
            the_last = copy.deepcopy(set(elements))
            the_last.difference_update(the_part)
            partition_list.extend([partition + [the_part] for partition in all_partition(list(the_last))])

    return partition_list


def max_type(key_set):
    remove_set = set()
    for key in key_set:
        item_list = [int(x) for x in key.split('|')]
        for i in range(len(item_list)):
            for j in range(i + 1, len(item_list)):
                new_item_list = item_list[0:i] + [item_list[i] + item_list[j]] + item_list[i+1:j] + item_list[j+1:]
                new_item_list = sorted(new_item_list)
                new_type = "|".join([str(item) for item in new_item_list])
                if new_type in key_set:
                    remove_set.add(key)
                    break
            if key in remove_set:
                break

    for key in remove_set:
        key_set.remove(key)


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
