import copy
from itertools import combinations

from partition import Partition


def max_partition_set(partitions_set):
    remove_list = list()
    for partition_1 in partitions_set:
        for partition_2 in partitions_set:
            if partition_1 <= partition_2 and partition_1 != partition_2:
                remove_list.append(partition_1)
                break

    for partition in remove_list:
        partitions_set.remove(partition)


def recursion_generate_partitions(filter_func):
    def inner(partitions_set, part_index_of_item, current_partite, partite_number, k):
        if current_partite == partite_number:
            current_partition = list()
            for part_index in range(partite_number):
                # the max number of parts is partite_number
                temp_part = list()
                for partite in range(partite_number):
                    # get the part index of every partite
                    if part_index_of_item[partite] == part_index:
                        temp_part.append(partite + 1)
                if len(temp_part) != 0:
                    current_partition.append(temp_part)

            current_partition = Partition(current_partition, partite_number)
            if current_partite in partitions_set:
                return

            filter_func(partitions_set, current_partition, k)
            return

        for i in range(current_partite + 1):
            part_index_of_item[current_partite] = i
            inner(partitions_set, part_index_of_item, current_partite + 1, partite_number, k)

    return inner


def generate_k_stretchable_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_stretchable_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    max_partition_set(partitions_set)
    return partitions_set


@recursion_generate_partitions
def filter_k_stretchable_partitions(partitions_set, current_partition, k):
    if current_partition.stretchable > k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)


def generate_k_producible_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_producible_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    return partitions_set


@recursion_generate_partitions
def filter_k_producible_partitions(partitions_set, current_partition, k):
    if current_partition.producible > k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)


def generate_k_partitionable_partitions(partite_number, k):
    partitions_set = set()
    part_index_of_item = [0 for i in range(partite_number)]
    filter_k_partitionable_partitions(partitions_set, part_index_of_item, 0, partite_number, k)
    return partitions_set


@recursion_generate_partitions
def filter_k_partitionable_partitions(partitions_set, current_partition, k):
    if current_partition.partitionable < k:
        return
    else:
        partitions_set.add(current_partition)
        max_partition_set(partitions_set)
