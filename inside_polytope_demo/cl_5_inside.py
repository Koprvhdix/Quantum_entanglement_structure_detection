import numpy as np

from ML_PIC import ML_PIC
from inside_polytope_demo.compute import compute_all_5_qubit
from partition_tools import generate_k_partitionable_partitions

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 15, 19, 28]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.25

    compute_all_5_qubit(rho)
