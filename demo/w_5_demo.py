from tools import generate_k_stretchable_partitions, compute, generate_k_producible_partitions

if __name__ == "__main__":
    N = 5
    P = [['00001', '00010'], ['00001', '00100'], ['00001', '01000'], ['00001', '10000'], ['00010', '00100'],
         ['00010', '01000'], ['00010', '10000'], ['00100', '01000'], ['00100', '10000'], ['01000', '10000']]

    # P = [['00000', '01111'], ['00000', '10011'], ['00000', '11100'], ['01111', '10011'], ['01111', '11100'],
    #      ['10011', '11100']]

    for k in range(-(N - 1), (N - 1)):
        Gamma_stretchable = generate_k_stretchable_partitions(N, k)
        best_qsv_list = compute(P, Gamma_stretchable)
        print(k)
        for qsv in best_qsv_list:
            print(str(qsv))

