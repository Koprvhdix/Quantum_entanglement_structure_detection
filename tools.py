import random
from fractions import Fraction

from quantum_state_value_pair import QuantumStateValuePairDict

import pandas as pd

from itertools import product


def min_union(M):
    combination_list = list()
    min_union_len = float('inf')
    for combination in product(*M):
        union_set = set().union(*combination)
        if len(union_set) < min_union_len:
            min_union_len = len(union_set)
            combination_list.clear()
            combination_list.append(combination)
        elif len(union_set) == min_union_len:
            combination_list.append(combination)
    return combination_list


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


def compute(P, Gamma):
    qs_candidate_list = list()

    # compute the candidate matrix
    for partition in Gamma:
        partition_candidate_list = dict()
        partition_candidate_list['Partitions'] = partition.partition_by_str
        for quantum_pair in P:
            quantum_state_set = set()
            for part in partition.partition_by_list:
                quantum_state_set.add(".".join(sorted([m_n_part(quantum_pair[0], quantum_pair[1], part),
                                                       m_n_part(quantum_pair[1], quantum_pair[0], part)])))
            partition_candidate_list[".".join(sorted(quantum_pair))] = list(quantum_state_set)
        qs_candidate_list.append(partition_candidate_list)

    # select the only one choice
    qs_candidate = pd.DataFrame(qs_candidate_list)
    column_pair_dict = dict()
    for column in qs_candidate.columns:
        if column == "Partitions":
            continue
        column_pair_set = set()
        for pair_list in qs_candidate[column]:
            if len(pair_list) == 1:
                column_pair_set.add(pair_list[0])
            if len(pair_list) == 2 and column in pair_list:
                column_pair_set.add(pair_list[0] if column == pair_list[1] else pair_list[1])
        column_pair_dict[column] = column_pair_set

    # 计算 P 的系数
    union_max = dict()
    for index, line in qs_candidate.iterrows():
        union_add = dict()
        for column in qs_candidate.columns:
            if column == "Partitions":
                continue
            if len(line[column]) == 1 and line[column][0] == column:
                quantum = column.split(".")
                if quantum[0] not in union_add:
                    union_add[quantum[0]] = 0
                if quantum[1] not in union_add:
                    union_add[quantum[1]] = 0
                union_add[quantum[0]] += Fraction(1, 2)
                union_add[quantum[1]] += Fraction(1, 2)
        for key in union_add:
            if key not in union_max:
                union_max[key] = 0
            if union_max[key] < union_add[key]:
                union_max[key] = union_add[key]

    union_pair_list = list()
    columns_list = list()
    # 选取最小集合
    for column in qs_candidate.columns:
        if column == "Partitions":
            continue

        union_pair_set = set()
        need_to_cover_list = list()
        for pair_list in qs_candidate[column]:
            pair_set = set(pair_list)
            if column in pair_set:
                pair_set.remove(column)
            if pair_set & column_pair_dict[column] == set():
                union_pair_set = union_pair_set.union(pair_set)
                need_to_cover_list.append(pair_set)

        if union_pair_set != set():
            for pair_count in range(1, len(union_pair_set)):
                current_result = list()
                select_n_sub(list(union_pair_set), list(), 0, 0, pair_count, current_result)
                # 检查是否能盖住
                current_min_pair_list = list()
                for pair_set in current_result:
                    cover_index = set()
                    for pair in pair_set:
                        for i in range(len(need_to_cover_list)):
                            if pair in need_to_cover_list[i]:
                                cover_index.add(i)
                    if len(cover_index) == len(need_to_cover_list):
                        current_min_pair_list.append(list(column_pair_dict[column]) + pair_set)
                if len(current_min_pair_list) > 0:
                    union_pair_list.append(current_min_pair_list)
                    columns_list.append(column)
                    break
        else:
            union_pair_list.append([list(column_pair_dict[column])])
            columns_list.append(column)

    min_union_pair_list = min_union(union_pair_list)
    for min_union_pair in min_union_pair_list:
        temp_candidate = qs_candidate.copy()
        select_best_choice(min_union_pair, temp_candidate, columns_list, union_max)


def select_n_sub(candidate, current_list, index, current, n, result_list):
    if current == n:
        result_list.append(current_list)
        return
    for temp_index in range(index, len(candidate)):
        select_n_sub(candidate, current_list + [candidate[temp_index]], temp_index + 1, current + 1, n, result_list)


def select_best_choice(min_union_pair, qs_candidate, columns_list, union_max):
    qs_candidate = qs_candidate.drop('Partitions', axis=1)
    for col in qs_candidate.columns:
        # 获取限定范围
        r = min_union_pair[columns_list.index(col)]
        # 应用函数，删除不在限定范围内的值
        qs_candidate[col] = qs_candidate[col].apply(lambda x: [i for i in x if i in r])

    # can select one of them
    best_choices_list = list()
    for a in range(len(qs_candidate.values)):
        choices = list(product(*qs_candidate.values[a]))
        current_best_choices = list()
        min_value = float('inf')
        for choice in choices:
            choice_list = list(choice)
            qs_result = handle_choice(choice_list)

            condition = True
            for key, value in union_max.items():
                if key in qs_result and value < qs_result[key]:
                    condition = False
                    break

            if condition:
                value = max(qs_result.values())
                if value < min_value:
                    current_best_choices.clear()
                    current_best_choices.append(choice_list)
                    min_value = value
                elif value == min_value:
                    current_best_choices.append(choice_list)
        print(min_value)
        best_choices_list.append(current_best_choices)

    result_1 = dict()
    for best_choice in best_choices_list:
        result_1 = merge_dicts(result_1, handle_choice(best_choice[random.randint(0, len(best_choice) - 1)]))

    result_2 = dict()
    for best_choice in best_choices_list:
        result_2 = merge_dicts(result_2, handle_choice(best_choice[random.randint(0, len(best_choice) - 1)]))

    print(len(result_1.keys()), sum(result_1.values()), len(result_2.keys()), sum(result_2.values()))


def handle_choice(choice_list):
    result_dict = dict()
    for pair in choice_list:
        state_1, state_2 = pair.split('.')
        result_dict[state_1] = result_dict.get(state_1, 0) + Fraction(1, 2)
        result_dict[state_2] = result_dict.get(state_2, 0) + Fraction(1, 2)
    return result_dict

def merge_dicts(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        if key in result:
            result[key] = max(result[key], value)
        else:
            result[key] = value
    return result
