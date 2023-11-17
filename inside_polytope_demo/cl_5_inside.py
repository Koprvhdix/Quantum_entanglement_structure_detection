import numpy as np

from inside_polytope_demo.compute import compute_all_5_qubit

if __name__ == "__main__":
    rho = np.zeros((32, 32))

    indices = [0, 15, 19, 28]
    for index in indices:
        for index2 in indices:
            rho[index, index2] = 0.25

    compute_all_5_qubit(rho)
