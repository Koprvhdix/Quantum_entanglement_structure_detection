from tools import compute

from partition_tools import generate_k_stretchable_partitions, generate_k_producible_partitions

if __name__ == "__main__":
    N = 5
    P = [['00001', '00010'], ['00001', '00100'], ['00001', '01000'], ['00001', '10000'], ['00010', '00100'],
         ['00010', '01000'], ['00010', '10000'], ['00100', '01000'], ['00100', '10000'], ['01000', '10000']]

    # for k in range(- (N - 1), (N - 1)):
    #     Gamma_stretchable = generate_k_stretchable_partitions(N, k)
    #     best_qsv_list = compute(P, Gamma_stretchable)
    #     print(k)
    #     for qsv in best_qsv_list:
    #         print(str(qsv))
    #         print()

    # Gamma_stretchable = generate_k_stretchable_partitions(N, 0)
    # best_qsv_list = compute(P, Gamma_stretchable)
    # for qsv in best_qsv_list:
    #     print(str(qsv))
