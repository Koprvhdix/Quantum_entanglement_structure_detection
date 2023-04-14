from fractions import Fraction

from quantum_state_value_pair import QuantumStateValuePairDict
from tools import optimize_qsv_list

if __name__ == "__main__":
    quantum_state_value_pair = QuantumStateValuePairDict()
    quantum_state_value_pair.add_pair("00", Fraction(1, 2))
    quantum_state_value_pair.add_pair("01", Fraction(4, 1))

    quantum_state_value_pair_2 = QuantumStateValuePairDict()
    quantum_state_value_pair_2.add_pair("00", Fraction(1, 2))
    quantum_state_value_pair_2.add_pair("01", Fraction(4, 1))

    print(quantum_state_value_pair == quantum_state_value_pair_2)

    test_list = [quantum_state_value_pair, quantum_state_value_pair_2]
    optimize_qsv_list(test_list)
    print(len(test_list))
