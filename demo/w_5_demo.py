from partition_tools import generate_k_stretchable_partitions
from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable, compute

if __name__ == "__main__":
    N = 5
    P = [['00001', '00010'], ['00001', '00100'], ['00001', '01000'], ['00001', '10000'], ['00010', '00100'],
         ['00010', '01000'], ['00010', '10000'], ['00100', '01000'], ['00100', '10000'], ['01000', '10000']]

    # compute(P, generate_k_stretchable_partitions(N, 0))
    compute_all_stretchable(P, N)
    compute_all_producible(P, N)
    compute_all_partitionable(P, N)
