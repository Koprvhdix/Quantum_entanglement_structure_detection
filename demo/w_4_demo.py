from tools import compute, generate_k_stretchable_partitions, generate_k_partitionable_partitions

if __name__ == "__main__":
    N = 4
    P = [['0001', '0010'], ['0001', '0100'], ['0001', '1000'],
         ['0010', '0100'], ['0010', '1000'], ['0100', '1000']]

    for k in range(-(N - 1), (N - 1)):
        # Gamma_partitionable = generate_k_partitionable_partitions(N, k)
        Gamma_stretchable = generate_k_stretchable_partitions(N, k)
        quantum_state_value_pair_dict = compute(P, Gamma_stretchable)
        print(k, str(quantum_state_value_pair_dict))

    Gamma_partitionable = generate_k_partitionable_partitions(N, 3)
    quantum_state_value_pair_dict_partitionable = compute(P, Gamma_partitionable)
    print(str(quantum_state_value_pair_dict_partitionable))
