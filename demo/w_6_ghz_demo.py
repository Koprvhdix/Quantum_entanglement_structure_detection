from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable

if __name__ == "__main__":
    N = 6
    # P = [['000000', '111111'], ['000001', '111111'], ['000010', '111111'], ['000100', '111111'], ['001000', '111111'],
    #      ['010000', '111111'], ['100000', '111111'], ['000010', '000001'], ['000100', '001000'], ['010000', '100000']]

    P = [['000000', '111111'], ['000001', '111111'], ['000010', '111111'], ['000010', '000001']]

    compute_all_stretchable(P, N)
    compute_all_producible(P, N)
    compute_all_partitionable(P, N)
