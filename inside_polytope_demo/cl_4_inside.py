import numpy as np

from ML_PIC import ML_PIC
from inside_polytope_demo.compute import compute_all_4_qubit
from partition_tools import generate_k_producible_partitions, generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((16, 16))

    indices = [0, 3, 12, 15]
    value = [0.5, 0.5, 0.5, -0.5]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = value[indices.index(index)] * value[indices.index(index2)]

    compute_all_4_qubit(rho)