from tools import compute

from partition_tools import generate_k_stretchable_partitions

if __name__ == "__main__":
    N = 5

    P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
         ['10011', '11100']]

    # for k in range(-(N - 3), (N - 1)):
    #     Gamma_stretchable = generate_k_stretchable_partitions(N, k)
    #     best_qsv_list = compute(P, Gamma_stretchable)
    #     print(k)
    #     for qsv in best_qsv_list:
    #         print(str(qsv))

    Gamma_stretchable = generate_k_stretchable_partitions(N, -1)
    best_qsv_list = compute(P, Gamma_stretchable)