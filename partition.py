def format_partition(partition_list):
    new_partition_list = [sorted(current_part) for current_part in partition_list]
    return sorted(new_partition_list, key=lambda part: part[0])


def checkout_partition(partition_type_list, partite_number):
    number_count = 0
    for part in partition_type_list:
        if len(part) == 0:
            return False
        else:
            number_count += len(part)
    if number_count != partite_number:
        return False

    for number in range(1, partite_number + 1):
        is_contain = False
        for part in partition_type_list:
            if number in part:
                is_contain = True
        if not is_contain:
            return False
    return True


class Partition(object):
    def __init__(self, partition_type_list, partite_number):
        assert checkout_partition(partition_type_list, partite_number)
        self.partition_by_list = format_partition(partition_type_list)
        str_list = list()
        for part in self.partition_by_list:
            str_list.append(".".join([str(item) for item in part]))
        self.partition_by_str = "|".join(str_list)

        self.partition_by_set = [set(part) for part in self.partition_by_list]

        self.partitionable = len(self.partition_by_list)
        self.producible = max([len(part) for part in self.partition_by_list])
        self.stretchable = self.producible - self.partitionable

    def __le__(self, other):
        for part in self.partition_by_set:
            is_subset = False
            for part_other in other.partition_by_set:
                if part <= part_other:
                    is_subset = True
            if not is_subset:
                return False
        return True

    def __ge__(self, other):
        for part in other.partition_by_set:
            is_subset = False
            for part_self in self.partition_by_set:
                if part <= part_self:
                    is_subset = True
            if not is_subset:
                return False
        return True

    def __str__(self):
        return self.partition_by_str

    def __hash__(self):
        return hash(self.partition_by_str)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        else:
            return False


if __name__ == "__main__":
    # temp_partition = Partition([[1, 3], [3, 4]], 4)
    temp_partition = Partition([[2, 3], [1, 4]], 4)
    temp_partition_2 = Partition([[2, 3], [1, 4]], 4)
    temp_partition_3 = Partition([[2], [3], [1, 4]], 4)
    print(temp_partition.partition_by_str)
    print(temp_partition_2 >= temp_partition_3)
    print(temp_partition_3 <= temp_partition_2)

    partition_set = set()
    partition_set.add(temp_partition)
    partition_set.add(temp_partition_2)

    print(len(partition_set))
