from partition_tools import generate_k_stretchable_partitions
from tools import compute

if __name__ == "__main__":
    N = 5

    P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
         ['10011', '11100']]

    # print("(-4)-str")
    # compute(P, generate_k_stretchable_partitions(N, -4))
    print("(-2)-str")
    compute(P, generate_k_stretchable_partitions(N, -2))
    print("(-1)-str")
    compute(P, generate_k_stretchable_partitions(N, -1))
    print("0-str")
    compute(P, generate_k_stretchable_partitions(N, 0))
    print("1-str")
    compute(P, generate_k_stretchable_partitions(N, 1))
    print("2-str")
    compute(P, generate_k_stretchable_partitions(N, 2))
