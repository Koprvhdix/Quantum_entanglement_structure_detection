import numpy as np

from Full_Sep_SDP import FullSepSDP
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((64, 64))

    indices = [1, 2, 4, 8, 16, 32]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 1 / 6

    print("----------- full sep -------------")
    partition_6_part = generate_k_partitionable_partitions(6, 6)
    current_class = FullSepSDP(6, 1000, rho, partition_6_part, 1)
    current_class.train(1000)
    p_value_full_sep = current_class.sdp()
    print("Full Sep:", p_value_full_sep)
