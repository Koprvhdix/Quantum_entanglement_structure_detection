import numpy as np

from GD_SDP import GD_SDP
from inside_polytope_demo.compute import compute_all_4_qubit
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((16, 16))

    indices = [0, 15]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.5

    # compute_all_4_qubit(rho)
    print("----------- 2 part -------------")
    partition_2_part = generate_k_partitionable_partitions(4, 2)
    current_class = GD_SDP(4, 300, rho, partition_2_part, 1)
    current_class.train(1500)
    p_value_2_part = current_class.sdp()
    print("2 part:", p_value_2_part)