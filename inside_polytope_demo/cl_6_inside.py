import numpy as np

from Full_Sep_SDP import FullSepSDP
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((64, 64))

    indices = [0, 7, 11, 12, 48, 48 + 7, 48 + 11, 48 + 12]
    for index in indices:
        label_1 = 1
        if index in [48 + 11, 48 + 12]:
            label_1 *= -1
        for index2 in indices:
            label = label_1
            if index2 in [48 + 11, 48 + 12]:
                label *= -1
            rho[index, index2] = label * 1/8

    print("----------- full sep -------------")
    partition_6_part = generate_k_partitionable_partitions(6, 6)
    current_class = FullSepSDP(6, rho, partition_6_part)
    p_value_full_sep = current_class.sdp()
    print("Full Sep:", p_value_full_sep)
