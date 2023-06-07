from tools import compute

from fractions import Fraction

from partition_tools import generate_k_stretchable_partitions, generate_k_producible_partitions

if __name__ == "__main__":
    N = 5
    P = [['00001', '00010'], ['00001', '00100'], ['00001', '01000'], ['00001', '10000'], ['00010', '00100'],
         ['00010', '01000'], ['00010', '10000'], ['00100', '01000'], ['00100', '10000'], ['01000', '10000']]

    print("-4")
    compute(P, generate_k_stretchable_partitions(N, -4))
    print()
    print()
    print("-2")
    compute(P, generate_k_stretchable_partitions(N, -2))
    print()
    print()
    print("-1")
    compute(P, generate_k_stretchable_partitions(N, -1))
    print()
    print()
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

