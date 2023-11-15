import numpy as np

from ML_PIC import ML_PIC
from partition_tools import generate_k_producible_partitions

if __name__ == "__main__":
    rho = np.zeros((16, 16))

    indices = [0, 3, 12, 15]
    value = [0.5, 0.5, 0.5, -0.5]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = value[indices.index(index)] * value[indices.index(index2)]

    partition_2_prod = generate_k_producible_partitions(4, 1)
    current_class = ML_PIC(4, 1000, rho, partition_2_prod, 1, 0.001)
    current_class.train(1000)
    current_class.sdp()
