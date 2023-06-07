from tools import compute

from partition_tools import generate_k_stretchable_partitions

if __name__ == "__main__":
    N = 5

    P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
         ['10011', '11100']]

    # print("-4")
    # compute(P, generate_k_stretchable_partitions(N, -4))
    # print()
    # print()
    # print()
    print("-2")
    compute(P, generate_k_stretchable_partitions(N, -2))
    print()
    print()
    print()
    print("-1")
    compute(P, generate_k_stretchable_partitions(N, -1))
    print()
    print()
    print()
    print("0")
    compute(P, generate_k_stretchable_partitions(N, 0))
    print()
    print()
    print()
    print("1")
    compute(P, generate_k_stretchable_partitions(N, 1))
    print()
    print()
    print()
    print("2")
    compute(P, generate_k_stretchable_partitions(N, 2))