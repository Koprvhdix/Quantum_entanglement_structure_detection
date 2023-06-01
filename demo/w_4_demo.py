from tools import compute
from partition_tools import generate_k_stretchable_partitions

if __name__ == "__main__":
    N = 4
    P = [['0001', '0010'], ['0001', '0100'], ['0001', '1000'],
         ['0010', '0100'], ['0010', '1000'], ['0100', '1000']]

    # for k in range(-(N - 1), (N - 1)):
    #     Gamma_stretchable = generate_k_stretchable_partitions(N, k)
    #     best_qsv_list = compute(P, Gamma_stretchable)
    #     print(k)
    #     for qsv in best_qsv_list:
    #         print(str(qsv))
    #
    # Gamma_stretchable = generate_k_stretchable_partitions(N, 0)
    # best_qsv_list = compute(P, Gamma_stretchable)
    # for qsv in best_qsv_list:
    #     print(str(qsv))
