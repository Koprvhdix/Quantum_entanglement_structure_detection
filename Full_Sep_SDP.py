import itertools
from collections import deque

import numpy as np
import picos as pic
import torch

from GD_SDP import swap_chars, bubble_sort_steps


def generate_init_point():
    Z = np.matrix([[1, 0], [0, -1]])
    X = np.matrix([[0, 1], [1, 0]])
    Y = np.matrix([[0, -1j], [1j, 0]])

    basis = [0.5 * (np.eye(2) + Z), 0.5 * (np.eye(2) - Z), 0.5 * (np.eye(2) + X), 0.5 * (np.eye(2) - X),
             0.5 * (np.eye(2) + Y), 0.5 * (np.eye(2) - Y)]
    return basis


class FullSepSDP(object):
    def __init__(self, N, rho, partition_list):
        self.N = N
        self.rho = rho
        self.partition_list = partition_list

        self.exchange_matrix = list()
        self.exchange_matrix_np = list()
        for num1 in range(self.N):
            temp_matrix_list = list()
            temp_matrix_list_np = list()
            for num2 in range(num1 + 1, self.N):
                the_matrix = np.zeros([2 ** self.N, 2 ** self.N])
                for number in range(2 ** self.N):
                    number_str = format(number, '0{}b'.format(self.N))
                    number_str = swap_chars(number_str, num1, num2)
                    number_23 = int(number_str, 2)
                    the_matrix[number, number_23] = 1
                temp_matrix_list.append(torch.tensor(the_matrix, dtype=torch.complex128))
                temp_matrix_list_np.append(np.matrix(the_matrix))
            self.exchange_matrix.append(temp_matrix_list)
            self.exchange_matrix_np.append(temp_matrix_list_np)

        self.exchange_list = list()
        self.partition_max_part_info_list = list()
        for partition in self.partition_list:
            concatenated_list = [element for sublist in partition.partition_by_list for element in sublist]
            self.exchange_list.append(bubble_sort_steps(concatenated_list))
            info = dict()
            info['len'] = partition.producible
            for index in range(len(partition.partition_by_list)):
                if len(partition.partition_by_list[index]) == partition.producible:
                    info['part'] = partition.partition_by_list[index]
                    info['index'] = index
            self.partition_max_part_info_list.append(info)

        self.data_queue = deque(maxlen=1)
        init_point_list = list()
        for partition_index in range(len(self.partition_list)):
            temp_point_list = list()
            for index in range(len(self.partition_list[partition_index].partition_by_list)):
                part = self.partition_list[partition_index].partition_by_list[index]
                temp_n = 2 ** len(part)
                if self.partition_max_part_info_list[partition_index]['index'] == index:
                    matrix_list = [np.eye(temp_n) / temp_n]
                else:
                    matrix_list = generate_init_point()
                temp_point_list.append(matrix_list)
            cartesian_product = list(itertools.product(*temp_point_list))
            init_point_list.append([list(item) for item in cartesian_product])
        self.data_queue.append(init_point_list)

    def sdp(self):
        x_list = self.data_queue[0]

        prob = pic.Problem()
        rho_list = list()
        for i in range(len(self.partition_list)):
            rho_list.append([])

        p = pic.RealVariable("p", 1)

        for partition_index in range(len(self.partition_list)):
            info = self.partition_max_part_info_list[partition_index]
            for point_index in range(len(x_list[partition_index])):
                sdp_rho = pic.HermitianVariable('rho_' + str(partition_index) + '_' + str(point_index),
                                                2 ** info['len'])
                rho_list[partition_index].append(sdp_rho)
                prob.add_constraint(sdp_rho >> 0)

        rho_next = None
        for partition_index in range(len(self.partition_list)):
            info = self.partition_max_part_info_list[partition_index]
            for point_index in range(len(x_list[partition_index])):
                rho_left = None
                rho_right = None
                for part_index in range(len(self.partition_list[partition_index].partition_by_list)):
                    if part_index < info['index']:
                        if rho_left is None:
                            rho_left = x_list[partition_index][point_index][part_index]
                        else:
                            rho_left = np.kron(rho_left, x_list[partition_index][point_index][part_index])
                    elif part_index > info['index']:
                        if rho_right is None:
                            rho_right = x_list[partition_index][point_index][part_index]
                        else:
                            rho_right = np.kron(rho_right, x_list[partition_index][point_index][part_index])
                    else:
                        continue

                if rho_left is None:
                    current_rho = rho_list[partition_index][point_index]
                else:
                    current_rho = rho_left @ rho_list[partition_index][point_index]

                if rho_right is not None:
                    current_rho = current_rho @ rho_right

                for exchange_pair in self.exchange_list[partition_index]:
                    current_rho = self.exchange_matrix_np[exchange_pair[0]][
                                      exchange_pair[1] - exchange_pair[0] - 1] * current_rho * \
                                  self.exchange_matrix_np[exchange_pair[0]][exchange_pair[1] - exchange_pair[0] - 1]

                if rho_next is None:
                    rho_next = current_rho
                else:
                    rho_next += current_rho

        prob.add_constraint(rho_next == (p * self.rho + ((1 - p) / (2 ** self.N)) * np.eye(2 ** self.N)))
        prob.set_objective("max", p)
        prob.solve(solver="mosek", primals=True)

        return p.value
