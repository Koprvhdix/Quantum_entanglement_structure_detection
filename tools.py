from fractions import Fraction

from quantum_state_value_pair import QuantumStateValuePairDict

import pandas as pd


def get_quantum_state_of_p(P):
    p_state_set = set()
    for quantum_pair in P:
        p_state_set.add(quantum_pair[0])
        p_state_set.add(quantum_pair[1])
    return p_state_set


def m_n_part(m, n, part):
    result = str()
    start_index = 0
    for index in part:
        result += m[start_index: index - 1]
        result += n[index - 1]
        start_index = index
    result += m[start_index:]
    return result


def phi_quantum_list(quantum_list, N):
    index_set = set()
    for i in range(N):
        is_same = True
        for quantum in quantum_list:
            if quantum[i] != quantum_list[0][i]:
                is_same = False
                break
        if is_same:
            index_set.add(i)
    return index_set


def compute_coefficient_of_p_quantum_state(P, N):
    state_pair_dict = dict()
    for quantum_pair in P:
        if quantum_pair[0] not in state_pair_dict:
            state_pair_dict[quantum_pair[0]] = list()
        if quantum_pair[1] not in state_pair_dict:
            state_pair_dict[quantum_pair[1]] = list()
        state_pair_dict[quantum_pair[0]].append(quantum_pair[1])
        state_pair_dict[quantum_pair[1]].append(quantum_pair[0])

    for quantum in state_pair_dict:
        for a in range(1, len(state_pair_dict[quantum])):
            pass

    quantum_coefficient_dict = dict()
    return quantum_coefficient_dict


def compute(P, Gamma):
    qs_candidate_list = list()

    for partition in Gamma:
        partition_candidate_list = list()
        partition_candidate_list.append(dict())
        partition_candidate_list[0]['Partitions'] = partition.partition_by_str
        for quantum_pair in P:
            quantum_state_set = set()
            for part in partition.partition_by_list:
                quantum_state_set.add(".".join(sorted([m_n_part(quantum_pair[0], quantum_pair[1], part),
                                                       m_n_part(quantum_pair[1], quantum_pair[0], part)])))
            temp_quantum_state_list = list(quantum_state_set)
            for i in range(len(temp_quantum_state_list)):
                if i == len(partition_candidate_list):
                    partition_candidate_list.append(dict())
                    partition_candidate_list[i]['Partitions'] = ""
                partition_candidate_list[i][".".join(sorted(quantum_pair))] = temp_quantum_state_list[i]
        for line in partition_candidate_list:
            qs_candidate_list.append(line)

    qs_candidate = pd.DataFrame(qs_candidate_list)
    print(qs_candidate.to_csv())

    # p_qsv_dict = compute_P_upper_bound(qs_candidate_list, P)
    # partition_qsv_list = list()
    #
    # for partition_qs in qs_candidate_list:
    #     result_list = list()
    #     recursion_part_qsv(partition_qs, 0, QuantumStateValuePairDict(), p_qsv_dict, result_list, p_state_set)
    #     partition_qsv_list.append(result_list)
    #
    current_qsv_list = list()
    #
    # for part_qsv in partition_qsv_list:
    #     current_qsv_list = union_max_list_optimize(current_qsv_list, part_qsv, p_state_set)

    return current_qsv_list


def select_quantum_from_candidate(qs_candidate_list, quantum_coefficient_dict, k_comb):
    qsv_list = list()
    pass

# def union_max_list_optimize(current_qsv_list, part_qsv, p_state_set):
#     if len(current_qsv_list) == 0:
#         for qsv in part_qsv:
#             current_qsv_list.append(qsv)
#     else:
#         temp_qsv_list = list()
#         for qsv_1 in part_qsv:
#             for qsv_2 in current_qsv_list:
#                 optimize_add_qsv(temp_qsv_list, qsv_1.union_max(qsv_2), p_state_set)
#         current_qsv_list = temp_qsv_list
#     return current_qsv_list
#
#
# def compute_P_upper_bound(qs_candidate_list, P):
#     p_set = [".".join(sorted([item[0], item[1]])) for item in P]
#
#     p_qsv_dict = QuantumStateValuePairDict()
#     for partition_qs in qs_candidate_list:
#         partition_qsv_dict = QuantumStateValuePairDict()
#         for qs in partition_qs:
#             if len(qs) == 1 and qs[0] in p_set:
#                 temp_qsv_dict = QuantumStateValuePairDict()
#                 state_1 = qs[0].split(".")[0]
#                 state_2 = qs[0].split(".")[1]
#                 temp_qsv_dict.add_pair(state_1, Fraction(1, 2))
#                 temp_qsv_dict.add_pair(state_2, Fraction(1, 2))
#                 partition_qsv_dict = partition_qsv_dict.union_add(temp_qsv_dict)
#         p_qsv_dict = p_qsv_dict.union_max(partition_qsv_dict)
#
#     return p_qsv_dict
#
#
# def qsv_compare_q(current_qsv_dict, p_qsv_dict, p_state_set):
#     for key in p_state_set:
#         if key in current_qsv_dict.quantum_state_value_dict:
#             if key not in p_qsv_dict.quantum_state_value_dict:
#                 return True
#             elif current_qsv_dict.quantum_state_value_dict[key] > p_qsv_dict.quantum_state_value_dict[key]:
#                 return True
#     return False
#
#
# def recursion_part_qsv(partition_qs, current_index, current_qsv_dict, p_qsv_dict, result_list, p_state_set):
#     if qsv_compare_q(current_qsv_dict, p_qsv_dict, p_state_set):
#         return
#
#     if current_index == len(partition_qs):
#         optimize_add_qsv(result_list, current_qsv_dict, p_state_set)
#         return
#
#     for qs in partition_qs[current_index]:
#         temp_dict = QuantumStateValuePairDict()
#         state_1 = qs.split(".")[0]
#         state_2 = qs.split(".")[1]
#         temp_dict.add_pair(state_1, Fraction(1, 2))
#         temp_dict.add_pair(state_2, Fraction(1, 2))
#         recursion_part_qsv(partition_qs, current_index + 1, current_qsv_dict.union_add(temp_dict), p_qsv_dict,
#                            result_list, p_state_set)
#
#
# def optimize_add_qsv(qsv_list, current_qsv_dict, p_state_set):
#     if len(qsv_list) == 0:
#         qsv_list.append(current_qsv_dict)
#         return
#
#     qsv_list_count = Fraction(0, 1)
#     qsv_list_key_number = 0
#     for key in qsv_list[0].quantum_state_value_dict:
#         if key in p_state_set:
#             continue
#         else:
#             qsv_list_count += qsv_list[0].quantum_state_value_dict[key]
#             qsv_list_key_number += 1
#
#     current_qsv_count = Fraction(0, 1)
#     current_qsv_key_number = 0
#     for key in current_qsv_dict.quantum_state_value_dict:
#         if key in p_state_set:
#             continue
#         else:
#             current_qsv_count += current_qsv_dict.quantum_state_value_dict[key]
#             current_qsv_key_number += 1
#
#     if current_qsv_count < qsv_list_count:
#         qsv_list.clear()
#         qsv_list.append(current_qsv_dict)
#         return
#     elif current_qsv_count > qsv_list_count:
#         return
#
#     if current_qsv_key_number > qsv_list_key_number:
#         qsv_list.clear()
#         qsv_list.append(current_qsv_dict)
#         return
#     elif current_qsv_key_number < qsv_list_key_number:
#         return
#
#     for qsv in qsv_list:
#         if qsv == current_qsv_dict:
#             return
#
#     qsv_list.append(current_qsv_dict)
