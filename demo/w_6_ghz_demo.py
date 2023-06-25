from partition_tools import generate_k_stretchable_partitions
from tools import compute

if __name__ == "__main__":
    N = 6
    P = [['000000', '111111'], ['000001', '111111'], ['000010', '111111'], ['000100', '111111'], ['001000', '111111'],
         ['010000', '111111'], ['100000', '111111'], ['000010', '000001'], ['000100', '001000'], ['010000', '100000']]

    # print("-4")
    # compute(P, generate_k_stretchable_partitions(N, -4))
    # print()
    # print()
    # print("-2")
    # compute(P, generate_k_stretchable_partitions(N, -2))
    # print()
    # print()
    # print("-1")
    # compute(P, generate_k_stretchable_partitions(N, -1))
    # print()
    # print()
    print("0")
    compute(P, generate_k_stretchable_partitions(N, 0))
    print()
    print()
    print("1")
    compute(P, generate_k_stretchable_partitions(N, 1))
    print()
    print()
    print("2")
    compute(P, generate_k_stretchable_partitions(N, 2))

