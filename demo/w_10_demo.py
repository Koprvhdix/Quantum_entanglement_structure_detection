import itertools

from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable

if __name__ == "__main__":
    N = 10
    quantum_state = [''.join(['1' if i == j else '0' for j in range(10)]) for i in range(10)]
    print(quantum_state)
    P = [list(item) for item in itertools.combinations(quantum_state, 2)]
    print(P)

    compute_all_stretchable(P, N)
    compute_all_producible(P, N)
    compute_all_partitionable(P, N)
