from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable

if __name__ == "__main__":
    N = 5

    P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
         ['10011', '11100']]

    compute_all_stretchable(P, N)
    compute_all_producible(P, N)
    compute_all_partitionable(P, N)
