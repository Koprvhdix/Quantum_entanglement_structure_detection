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
    qs_candidate_list = list()
    p_state_set = set()

    for partition in Gamma:
        partition_candidate_list = list()
        for quantum_pair in P:
            p_state_set.add(quantum_pair[0])
            p_state_set.add(quantum_pair[1])
            quantum_state_set = set()
            for part in partition.partition_by_list:
                quantum_state_set.add(".".join(sorted([m_n_part(quantum_pair[0], quantum_pair[1], part),
                                                       m_n_part(quantum_pair[1], quantum_pair[0], part)])))
            partition_candidate_list.append(list(quantum_state_set))
        qs_candidate_list.append(partition_candidate_list)

    p_qsv_dict = compute_P_upper_bound(qs_candidate_list, P)
    partition_qsv_list = list()

    for partition_qs in qs_candidate_list:
        result_list = list()
        recursion_part_qsv(partition_qs, 0, QuantumStateValuePairDict(), p_qsv_dict, result_list, p_state_set)
        partition_qsv_list.append(result_list)

    current_qsv_list = list()

    for part_qsv in partition_qsv_list:
        current_qsv_list = union_max_list_optimize(current_qsv_list, part_qsv, p_state_set)

    return current_qsv_list


def union_max_list_optimize(current_qsv_list, part_qsv, p_state_set):
    if len(current_qsv_list) == 0:
        for qsv in part_qsv:
            current_qsv_list.append(qsv)
    else:
        temp_qsv_list = list()
        for qsv_1 in part_qsv:
            for qsv_2 in current_qsv_list:
                optimize_add_qsv(temp_qsv_list, qsv_1.union_max(qsv_2), p_state_set)
        current_qsv_list = temp_qsv_list
    return current_qsv_list


def compute_P_upper_bound(qs_candidate_list, P):
    p_set = [".".join(sorted([item[0], item[1]])) for item in P]

    p_qsv_dict = QuantumStateValuePairDict()
    for partition_qs in qs_candidate_list:
        partition_qsv_dict = QuantumStateValuePairDict()
        for qs in partition_qs:
            if len(qs) == 1 and qs[0] in p_set:
                temp_qsv_dict = QuantumStateValuePairDict()
                state_1 = qs[0].split(".")[0]
                state_2 = qs[0].split(".")[1]
                temp_qsv_dict.add_pair(state_1, Fraction(1, 2))
                temp_qsv_dict.add_pair(state_2, Fraction(1, 2))
                partition_qsv_dict = partition_qsv_dict.union_add(temp_qsv_dict)
        p_qsv_dict = p_qsv_dict.union_max(partition_qsv_dict)

    return p_qsv_dict


def qsv_compare_q(current_qsv_dict, p_qsv_dict, p_state_set):
    if len((current_qsv_dict.quantum_state_value_dict.keys() - p_qsv_dict.quantum_state_value_dict.keys()) & p_state_set) > 0:
        return True

    for key in (p_qsv_dict.quantum_state_value_dict.keys() & current_qsv_dict.quantum_state_value_dict.keys()):
        if current_qsv_dict.quantum_state_value_dict[key] > p_qsv_dict.quantum_state_value_dict[key]:
            return True
    return False


def recursion_part_qsv(partition_qs, current_index, current_qsv_dict, p_qsv_dict, result_list, p_state_set):
    if qsv_compare_q(current_qsv_dict, p_qsv_dict, p_state_set):
        return

    if current_index == len(partition_qs):
        optimize_add_qsv(result_list, current_qsv_dict, p_state_set)
        return

    for qs in partition_qs[current_index]:
        temp_dict = QuantumStateValuePairDict()
        state_1 = qs.split(".")[0]
        state_2 = qs.split(".")[1]
        temp_dict.add_pair(state_1, Fraction(1, 2))
        temp_dict.add_pair(state_2, Fraction(1, 2))
        recursion_part_qsv(partition_qs, current_index + 1, current_qsv_dict.union_add(temp_dict), p_qsv_dict,
                           result_list, p_state_set)


def optimize_add_qsv(qsv_list, current_qsv_dict, p_state_set):
    if len(qsv_list) == 0:
        qsv_list.append(current_qsv_dict)
        return

    qsv_list_count = Fraction(0, 1)
    qsv_list_key_number = 0
    for key in qsv_list[0].quantum_state_value_dict:
        if key in p_state_set:
            continue
        else:
            qsv_list_count += qsv_list[0].quantum_state_value_dict[key]
            qsv_list_key_number += 1

    current_qsv_count = Fraction(0, 1)
    current_qsv_key_number = 0
    for key in current_qsv_dict.quantum_state_value_dict:
        if key in p_state_set:
            continue
        else:
            current_qsv_count += current_qsv_dict.quantum_state_value_dict[key]
            current_qsv_key_number += 1

    if current_qsv_count < qsv_list_count:
        qsv_list.clear()
        qsv_list.append(current_qsv_dict)
        return
    elif current_qsv_count > qsv_list_count:
        return

    if current_qsv_key_number > qsv_list_key_number:
        qsv_list.clear()
        qsv_list.append(current_qsv_dict)
        return
    elif current_qsv_key_number < qsv_list_key_number:
        return

    for qsv in qsv_list:
        if qsv == current_qsv_dict:
            return

    qsv_list.append(current_qsv_dict)


