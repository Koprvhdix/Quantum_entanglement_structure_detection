from fractions import Fraction

from partition import Partition
from quantum_state_value_pair import QuantumStateValuePairDict


def max_partition_set(partitions_set):
    remove_list = list()
    for partition_1 in partitions_set:
        for partition_2 in partitions_set:
            if partition_1 <= partition_2 and partition_1 != partition_2:
                remove_list.append(partition_1)
                break

    for partition in remove_list:
        partitions_set.remove(partition)


def recursion_generate_partitions(filter_func):
    def inner(partitions_set, part_index_of_item, current_partite, partite_number, k):
        if current_partite == partite_number:
            current_partition = list()
            for part_index in range(partite_number):
                # the max number of parts is partite_number
                temp_part = list()
                for partite in range(partite_number):
                    # get the part index of every partite
                    if part_index_of_item[partite] == part_index:
                        temp_part.append(partite + 1)
                if len(temp_part) != 0:
                    current_partition.append(temp_part)

            current_partition = Partition(current_partition, partite_number)
            if current_partite in partitions_set:
                return

            filter_func(partitions_set, current_partition, k)
            return

        for i in range(current_partite + 1):
            part_index_of_item[current_partite] = i
            inner(partitions_set, part_index_of_item, current_partite + 1, partite_number, k)

    return inner


def generate_k_stretchable_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_stretchable_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    return partitions_set


@recursion_generate_partitions
def filter_k_stretchable_partitions(partitions_set, current_partition, k):
    if current_partition.stretchable > k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)


def generate_k_producible_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_producible_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    return partitions_set


@recursion_generate_partitions
def filter_k_producible_partitions(partitions_set, current_partition, k):
    if current_partition.producible > k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)


def generate_k_partitionable_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_partitionable_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    return partitions_set


@recursion_generate_partitions
def filter_k_partitionable_partitions(partitions_set, current_partition, k):
    if current_partition.partitionable < k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)


def m_n_part(m, n, part):
    result = str()
    start_index = 0
    for index in part:
        result += m[start_index: index - 1]
        result += n[index - 1]
        start_index = index
    result += m[start_index:]
    return result


def compute(P, Gamma):
    quantum_state_value_pair_dict = QuantumStateValuePairDict()

    for partition in Gamma:
        qsv_partition = QuantumStateValuePairDict()
        for quantum_pair in P:
            quantum_state_set = set()
            for part in partition.partition_by_list:
                quantum_state_set.add(m_n_part(quantum_pair[0], quantum_pair[1], part))
                quantum_state_set.add(m_n_part(quantum_pair[1], quantum_pair[0], part))
            if quantum_pair[0] in quantum_state_set and quantum_pair[1] in quantum_state_set and len(
                    quantum_state_set) != 2:
                quantum_state_set.remove(quantum_pair[0])
                quantum_state_set.remove(quantum_pair[1])
            temp_pair = QuantumStateValuePairDict()
            for key in quantum_state_set:
                temp_pair.add_pair(key, Fraction(1, len(quantum_state_set)))
            qsv_partition = qsv_partition.union_add(temp_pair)

        quantum_state_value_pair_dict = quantum_state_value_pair_dict.union_max(qsv_partition)

    return quantum_state_value_pair_dict
