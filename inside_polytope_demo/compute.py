from ML_PIC import ML_PIC
from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions

import numpy as np
from scipy.special import comb
from itertools import combinations


def generate_dicke_state(n, k):
    # 初始化量子态
    state = np.zeros(2 ** n)

    # 生成所有可能的 k 个 1 的位置
    positions = list(combinations(range(n), k))

    # 对于每一种可能，将对应的量子态加到总态上
    for pos in positions:
        # 生成一个量子态
        temp_state = np.zeros(n)
        for p in pos:
            temp_state[p] = 1
        # 将这个量子态转换为十进制数，并在总态上加上对应的量子态
        index = int(''.join(map(str, temp_state.astype(int))), 2)
        state[index] = 1

    # 归一化
    state /= np.sqrt(comb(n, k))

    # 计算密度矩阵
    density_matrix = np.outer(state, state.conj())

    return density_matrix


def compute_all_4_qubit(rho):
    partition_3_part = generate_k_partitionable_partitions(4, 3)
    current_class = ML_PIC(4, 300, rho, partition_3_part, 1)
    current_class.train(400)
    p_value = current_class.sdp()
    print("3 part:", p_value)

    partition_list = generate_k_producible_partitions(4, 2)
    current_class = ML_PIC(4, 600, rho, partition_list, 1)
    current_class.train(400)
    p_value = current_class.sdp()
    print("2 prod:", p_value)

    partition_list = generate_k_partitionable_partitions(4, 2)
    current_class = ML_PIC(4, 300, rho, partition_list, 1)
    current_class.train(400)
    p_value = current_class.sdp()
    print("2 part:", p_value)