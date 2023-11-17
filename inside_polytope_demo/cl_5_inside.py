import numpy as np

from GD_SDP import GD_SDP
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 15, 19, 28]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.25

    partition_list = generate_k_partitionable_partitions(5, 4)
    # partition_list = generate_k_partitionable_partitions(5, 3)
    # partition_list = generate_k_partitionable_partitions(5, 2)
    current_class = GD_SDP(5, 300, rho, partition_list, 1)
    current_class.train(2000)
    current_class.sdp()
