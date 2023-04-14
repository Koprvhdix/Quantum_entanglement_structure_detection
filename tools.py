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
        union_max_list_optimize(current_qsv_list, part_qsv, p_state_set)

    # best_qsv_list = list()
    # best_qsv_list.append(Fraction(-1, 1))
    # recursion_best_qsv(partition_qsv_list, 0, QuantumStateValuePairDict(), best_qsv_list, p_state_set)

    return current_qsv_list


def union_max_list_optimize(current_qsv_list, part_qsv, p_state_set):
    if len(current_qsv_list) == 0:
        for qsv in part_qsv:
            current_qsv_list.append(qsv)
    else:
        temp_qsv_list = list()
        for qsv_1 in part_qsv:
            for qsv_2 in current_qsv_list:
                temp_qsv_list.append(qsv_1.union_max(qsv_2))
        current_qsv_list = temp_qsv_list

    optimize_qsv_list(current_qsv_list, p_state_set)


def remove_duplicate_qsv(qsv_list):
    remove_list = list()

    for i in range(len(qsv_list)):
        for j in range(i + 1, len(qsv_list)):
            if qsv_list[i] == qsv_list[j]:
                remove_list.append(qsv_list[i])
                break

    for qsv in remove_list:
        qsv_list.remove(qsv)


def optimize_qsv_list(qsv_list, p_state_set):
    if len(qsv_list) == 1:
        return

    remove_duplicate_qsv(qsv_list)

    remove_list = list()
    for i in range(len(qsv_list)):
        is_remove = True
        for j in range(len(qsv_list)):
            if i == j:
                continue
            for key in qsv_list[i].quantum_state_value_dict:
                if key in p_state_set:
                    continue
                if key not in qsv_list[j].quantum_state_value_dict or qsv_list[i].quantum_state_value_dict[key] < \
                        qsv_list[j].quantum_state_value_dict[key]:
                    is_remove = False
                    break
        if is_remove:
            remove_list.append(qsv_list[i])

    for qsv in remove_list:
        qsv_list.remove(qsv)


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
    for key in p_state_set:
        if key in current_qsv_dict.quantum_state_value_dict:
            if key not in p_qsv_dict.quantum_state_value_dict:
                return True
            elif current_qsv_dict.quantum_state_value_dict[key] > p_qsv_dict.quantum_state_value_dict[key]:
                return True
    return False


def recursion_part_qsv(partition_qs, current_index, current_qsv_dict, p_qsv_dict, result_list, p_state_set):
    if qsv_compare_q(current_qsv_dict, p_qsv_dict, p_state_set):
        return

    if current_index == len(partition_qs):
        result_list.append(current_qsv_dict)
        return

    for qs in partition_qs[current_index]:
        temp_dict = QuantumStateValuePairDict()
        state_1 = qs.split(".")[0]
        state_2 = qs.split(".")[1]
        temp_dict.add_pair(state_1, Fraction(1, 2))
        temp_dict.add_pair(state_2, Fraction(1, 2))
        recursion_part_qsv(partition_qs, current_index + 1, current_qsv_dict.union_add(temp_dict), p_qsv_dict,
                           result_list, p_state_set)


def recursion_best_qsv(partition_qsv_list, current_index, current_qsv, best_qsv_list, p_state_set):
    temp_score = Fraction(0, 1)
    for key in current_qsv.quantum_state_value_dict:
        if key not in p_state_set:
            temp_score += current_qsv.quantum_state_value_dict[key]

    if best_qsv_list[0] != Fraction(-1, 1) and temp_score > best_qsv_list[0]:
        return

    if current_index == len(partition_qsv_list):
        if best_qsv_list[0] == Fraction(-1, 1):
            best_qsv_list.append(current_qsv)
            best_qsv_list[0] = temp_score
        else:
            if temp_score == best_qsv_list[0]:
                best_qsv_list.append(current_qsv)
            elif temp_score < best_qsv_list[0]:
                best_qsv_list.clear()
                best_qsv_list.append(temp_score)
                best_qsv_list.append(current_qsv)
        return

    for qsv in partition_qsv_list[current_index]:
        recursion_best_qsv(partition_qsv_list, current_index + 1, current_qsv.union_max(qsv), best_qsv_list,
                           p_state_set)
