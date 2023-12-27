import numpy as np

from Full_Sep_SDP import FullSepSDP
from GD_SDP import GD_SDP
from partition_tools import generate_k_partitionable_partitions, generate_k_producible_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 31]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.5

    # print("----------- 4 part -------------")
    # partition_4_part = generate_k_partitionable_partitions(5, 4)
    # current_class = GD_SDP(5, 500, rho, partition_4_part, 1)
    # current_class.train(500)
    # p_value_4_part = current_class.sdp()
    # print("4 part:", p_value_4_part)

    # print("----------- 2 prod -------------")
    # partition_2_prod = generate_k_producible_partitions(5, 2)
    # current_class = GD_SDP(5, 200, rho, partition_2_prod, 1)
    # current_class.train(1000)
    # p_value_2_prod = current_class.sdp()
    # print("2 prod:", p_value_2_prod)

    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(5, 3)
    current_class = GD_SDP(5, 100, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)

    # print("----------- 3 prod -------------")
    # partition_3_prod = generate_k_producible_partitions(5, 3)
    # current_class = GD_SDP(5, 200, rho, partition_3_prod, 1)
    # current_class.train(1000)
    # p_value_3_prod = current_class.sdp()
    # print("3 prod:", p_value_3_prod)

    # print("----------- 2 part -------------")
    # partition_2_part = generate_k_partitionable_partitions(5, 2)
    # current_class = GD_SDP(5, 100, rho, partition_2_part, 1)
    # current_class.train(1000)
    # p_value_2_part = current_class.sdp()
    # print("2 part:", p_value_2_part)
