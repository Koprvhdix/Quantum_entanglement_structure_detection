import numpy as np

from Full_Sep_SDP import FullSepSDP
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [1, 2, 4, 8, 16]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.2

    print("----------- full sep -------------")
    partition_5_part = generate_k_partitionable_partitions(5, 5)
    current_class = FullSepSDP(5, rho, partition_5_part)
    p_value_full_sep = current_class.sdp()
    print("Full Sep:", p_value_full_sep)

