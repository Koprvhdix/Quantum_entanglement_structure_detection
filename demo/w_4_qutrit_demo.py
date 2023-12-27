import itertools

from partition_tools import generate_k_producible_partitions
from tools import compute

if __name__ == "__main__":
    N = 4
    quantum_state = [['0001', '0002'], ['0010', '0020'], ['0100', '0200'], ['1000', '2000']]
    result = []
    for a, b in itertools.combinations(quantum_state, 2):
        result.extend(itertools.product(a, b))

    P = list()
    for item in result:
        P.append(list(item))

    Gamma_stretchable = generate_k_producible_partitions(N, 2)
    compute(P, Gamma_stretchable, dim=3)
