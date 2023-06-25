import copy
import itertools

from partition import Partition
from partition_tools import all_partition, generate_k_stretchable_partitions
from tools import compute

if __name__ == "__main__":
    N = 10
    quantum_state = [''.join(['1' if i == j else '0' for j in range(10)]) for i in range(10)]
    print(quantum_state)
    P = [list(item) for item in itertools.combinations(quantum_state, 2)]
    print(P)

    Gamma_list = generate_k_stretchable_partitions(N, -1)
    compute(P, Gamma_list)
