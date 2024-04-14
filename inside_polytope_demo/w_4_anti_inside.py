import numpy as np

from Full_Sep_SDP import FullSepSDP
from GD_SDP import GD_SDP
from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions

if __name__ == "__main__":
    # rho_1 = np.zeros((16, 16))
    #
    # indices = [1, 2, 4, 8]
    # for index in indices:
    #     for index2 in indices:
    #         rho_1[index, index2] = 0.25
    #
    # rho_2 = np.zeros((16, 16))
    # indices = [7, 11, 13, 14]
    # for index in indices:
    #     for index2 in indices:
    #         rho_2[index, index2] = 0.25
    #
    # p = 0.5
    # rho = p * rho_1 + (1 - p) * rho_2

    rho = np.zeros((16, 16))
    indices = [1, 2, 4, 8]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.25

    # partition_4_part = generate_k_partitionable_partitions(4, 4)
    # current_class = FullSepSDP(4, 1000, rho, partition_4_part, 1)
    # current_class.train(1000)
    # p_value_full_sep = current_class.sdp()
    # print("Full Sep:", p_value_full_sep)

    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(4, 3)
    current_class = GD_SDP(4, 300, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)

    print("----------- 2 prod -------------")
    partition_2_prod = generate_k_producible_partitions(4, 2)
    current_class = GD_SDP(4, 300, rho, partition_2_prod, 1)
    current_class.train(2000)
    p_value_2_prod = current_class.sdp()
    print("2 prod:", p_value_2_prod)

    print("----------- 2 part -------------")
    partition_2_part = generate_k_partitionable_partitions(4, 2)
    current_class = GD_SDP(4, 300, rho, partition_2_part, 1)
    current_class.train(1000)
    p_value_2_part = current_class.sdp()
    print("2 part:", p_value_2_part)

    print("----------- Summary -------------")
    # print("full sep:", p_value_full_sep)
    print("3 part:", p_value_3_part)
    print("2 prod:", p_value_2_prod)
    print("2 part:", p_value_2_part)