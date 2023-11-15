from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable

if __name__ == "__main__":
    N = 6

    P = [['000000', '111111']]

    compute_all_stretchable(P, N)
    compute_all_producible(P, N)
    compute_all_partitionable(P, N)
