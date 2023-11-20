import numpy as np

from GD_SDP import GD_SDP
from inside_polytope_demo.compute import compute_all_5_qubit
from partition_tools import generate_k_producible_partitions, generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 15, 19, 28]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.25

    # compute_all_5_qubit(rho)
    print("----------- 3 part -------------")
    partition_3_part = generate_k_partitionable_partitions(5, 3)
    current_class = GD_SDP(5, 100, rho, partition_3_part, 1)
    current_class.train(1000)
    p_value_3_part = current_class.sdp()
    print("3 part:", p_value_3_part)
