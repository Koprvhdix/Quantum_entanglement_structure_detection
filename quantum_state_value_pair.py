from fractions import Fraction


class QuantumStateValuePairDict(object):
    def __init__(self):
        self.quantum_state_value_dict = dict()

    def add_pair(self, quantum_state, value):
        assert isinstance(quantum_state, str) and isinstance(value, Fraction)
        self.quantum_state_value_dict[quantum_state] = value

    def union_add(self, other):
        if isinstance(other, self.__class__):
            new_quantum_state_value_pair = QuantumStateValuePairDict()
            for key in self.quantum_state_value_dict:
                if key in other.quantum_state_value_dict:
                    new_quantum_state_value_pair.add_pair(key, self.quantum_state_value_dict[key] +
                                                          other.quantum_state_value_dict[key])
                else:
                    new_quantum_state_value_pair.add_pair(key, self.quantum_state_value_dict[key])
            for key in other.quantum_state_value_dict:
                if key not in self.quantum_state_value_dict:
                    new_quantum_state_value_pair.add_pair(key, other.quantum_state_value_dict[key])
            return new_quantum_state_value_pair
        else:
            return self

    def union_max(self, other):
        if isinstance(other, self.__class__):
            new_quantum_state_value_pair = QuantumStateValuePairDict()
            for key in self.quantum_state_value_dict:
                if key in other.quantum_state_value_dict and other.quantum_state_value_dict[key] > \
                        self.quantum_state_value_dict[key]:
                    new_quantum_state_value_pair.add_pair(key, other.quantum_state_value_dict[key])
                else:
                    new_quantum_state_value_pair.add_pair(key, self.quantum_state_value_dict[key])
            for key in other.quantum_state_value_dict:
                if key not in self.quantum_state_value_dict:
                    new_quantum_state_value_pair.add_pair(key, other.quantum_state_value_dict[key])
            return new_quantum_state_value_pair
        else:
            return self

    def __str__(self):
        str_list = list()
        new_key_list = sorted(self.quantum_state_value_dict.keys())
        # for key in new_key_list:
        #     str_list.append("<\\ket{" + key + "}," + str(self.quantum_state_value_dict[key]) + ">")
        # return "\\{" + ",".join(str_list) + "\\}"
        for key in new_key_list:
            str_list.append(key + ":" + str(self.quantum_state_value_dict[key]))
        return "\t".join(str_list)


if __name__ == "__main__":
    quantum_state_value_pair = QuantumStateValuePairDict()
    quantum_state_value_pair.add_pair("00", Fraction(1, 2))
    quantum_state_value_pair.add_pair("01", Fraction(4, 1))

    quantum_state_value_pair_2 = QuantumStateValuePairDict()
    quantum_state_value_pair_2.add_pair("00", Fraction(3, 1))
    quantum_state_value_pair_2.add_pair("10", Fraction(4, 1))

    print(str(quantum_state_value_pair.union_add(quantum_state_value_pair_2)))
    print(str(quantum_state_value_pair.union_max(quantum_state_value_pair_2)))
