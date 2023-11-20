import numpy as np

from Full_Sep_SDP import FullSepSDP
from GD_SDP import GD_SDP
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 31]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.5

    # print("----------- 4 part -------------")
    # partition_4_part = generate_k_partitionable_partitions(5, 4)
    # current_class = GD_SDP(5, 200, rho, partition_4_part, 1)
    # current_class.train(1500)
    # p_value_4_part = current_class.sdp()
    # print("4 part:", p_value_4_part)

    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(5, 3)
    current_class = GD_SDP(5, 200, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)
