from fractions import Fraction

from tools import generate_k_stretchable_partitions, compute, generate_k_producible_partitions, \
    generate_k_partitionable_partitions
from quantum_state_value_pair import QuantumStateValuePairDict

if __name__ == "__main__":
    N = 4
    P = [['0001', '0010'], ['0001', '0100'], ['0001', '1000'],
         ['0010', '0100'], ['0010', '1000'], ['0100', '1000']]
    k = 3

    Gamma_1 = generate_k_partitionable_partitions(N, k)
    compute(P, Gamma_1)
    quantum_state_value_pair_dict = compute(P, Gamma_1)
    print(str(quantum_state_value_pair_dict))





