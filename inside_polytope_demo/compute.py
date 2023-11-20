from itertools import combinations

import numpy as np
from scipy.special import comb

from Full_Sep_SDP import FullSepSDP
from GD_SDP import GD_SDP
from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions


def generate_dicke_state(n, k):
    # Initialize the quantum state
    state = np.zeros(2 ** n)

    # Generate all possible positions of k ones
    positions = list(combinations(range(n), k))

    # For each possibility, add the corresponding quantum state to the total state
    for pos in positions:
        # Generate a quantum state
        temp_state = np.zeros(n)
        for p in pos:
            temp_state[p] = 1
        # Convert this quantum state to a decimal number and add the corresponding quantum state to the total state
        index = int(''.join(map(str, temp_state.astype(int))), 2)
        state[index] = 1

    # Normalize
    state /= np.sqrt(comb(n, k))

    # Calculate the density matrix
    density_matrix = np.outer(state, state.conj())

    return density_matrix


def compute_all_4_qubit(rho):
    print("----------- full sep -------------")
    partition_4_part = generate_k_partitionable_partitions(4, 4)
    current_class = FullSepSDP(4, rho, partition_4_part)
    p_value_full_sep = current_class.sdp()
    print("Full Sep:", p_value_full_sep)

    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(4, 3)
    current_class = GD_SDP(4, 300, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)

    print("----------- 2 prod -------------")
    partition_2_prod = generate_k_producible_partitions(4, 2)
    current_class = GD_SDP(4, 300, rho, partition_2_prod, 1)
    current_class.train(1000)
    p_value_2_prod = current_class.sdp()
    print("2 prod:", p_value_2_prod)

    print("----------- 2 part -------------")
    partition_2_part = generate_k_partitionable_partitions(4, 2)
    current_class = GD_SDP(4, 300, rho, partition_2_part, 1)
    current_class.train(1000)
    p_value_2_part = current_class.sdp()
    print("2 part:", p_value_2_part)

    print("----------- Summary -------------")
    print("full sep:", p_value_full_sep)
    print("3 part:", p_value_3_part)
    print("2 prod:", p_value_2_prod)
    print("2 part:", p_value_2_part)


def compute_all_5_qubit(rho):
    print("----------- full sep -------------")
    partition_5_part = generate_k_partitionable_partitions(5, 5)
    current_class = FullSepSDP(5, rho, partition_5_part)
    p_value_full_sep = current_class.sdp()
    print("Full Sep:", p_value_full_sep)

    print("----------- 4 part -------------")
    partition_4_part = generate_k_partitionable_partitions(5, 4)
    current_class = GD_SDP(5, 200, rho, partition_4_part, 1)
    current_class.train(1000)
    p_value_4_part = current_class.sdp()
    print("4 part:", p_value_4_part)

    print("----------- 2 prod -------------")
    partition_2_prod = generate_k_producible_partitions(5, 2)
    current_class = GD_SDP(5, 200, rho, partition_2_prod, 1)
    current_class.train(1000)
    p_value_2_prod = current_class.sdp()
    print("2 prod:", p_value_2_prod)

    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(5, 3)
    current_class = GD_SDP(5, 100, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)

    print("----------- 3 prod -------------")
    partition_3_prod = generate_k_producible_partitions(5, 3)
    current_class = GD_SDP(5, 200, rho, partition_3_prod, 1)
    current_class.train(1000)
    p_value_3_prod = current_class.sdp()
    print("3 prod:", p_value_3_prod)

    print("----------- 2 part -------------")
    partition_2_part = generate_k_partitionable_partitions(5, 2)
    current_class = GD_SDP(5, 200, rho, partition_2_part, 1)
    current_class.train(1000)
    p_value_2_part = current_class.sdp()
    print("2 part:", p_value_2_part)

    print("----------- Summary -------------")
    print("full sep:", p_value_full_sep)
    print("4 part:", p_value_4_part)
    print("2 prod:", p_value_2_prod)
    print("3 part:", p_value_3_part)
    print("3 prod:", p_value_3_prod)
    print("2 part:", p_value_2_part)
