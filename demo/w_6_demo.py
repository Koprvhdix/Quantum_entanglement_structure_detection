from tools import generate_k_stretchable_partitions, compute

if __name__ == "__main__":
    N = 6
    # P = [['000000', '000111'], ['000000', '110000'], ['000000', '110111'], ['000000', '001100'], ['000000', '001011'],
    #      ['000000', '111100'], ['000000', '111011'], ['000111', '110000'], ['000111', '110111'], ['000111', '001100'],
    #      ['000111', '001011'], ['000111', '111100'], ['000111', '111011'], ['110000', '110111'], ['110000', '001100'],
    #      ['110000', '001011'], ['110000', '111100'], ['110000', '111011'], ['110111', '001100'], ['110111', '001011'],
    #      ['110111', '111100'], ['110111', '111011'], ['001100', '001011'], ['001100', '111100'], ['001100', '111011'],
    #      ['001011', '111100'], ['001011', '111011'], ['111100', '111011']]

    P = [['000001', '000010'], ['000001', '000100'], ['000001', '001000'], ['000001', '010000'], ['000001', '100000'],
         ['000010', '000100'], ['000010', '001000'], ['000010', '010000'], ['000010', '100000'], ['000100', '001000'],
         ['000100', '010000'], ['000100', '100000'], ['001000', '010000'], ['001000', '100000'], ['010000', '100000']]

    for k in range(-(N - 1), (N - 1)):
        print(k)
        Gamma_stretchable = generate_k_stretchable_partitions(N, k)
        quantum_state_value_pair_dict = compute(P, Gamma_stretchable)
        print(str(quantum_state_value_pair_dict))