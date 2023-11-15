import numpy as np

def swap_chars(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

matrix_23 = np.zeros([16, 16])
matrix_423 = np.zeros([16, 16])

for number in range(16):
    number_str = f"{number:04b}"
    number_str = swap_chars(number_str, 1, 2)
    number_23 = int(number_str, 2)
    matrix_23[number, number_23] = 1

    number_str_2 = f"{number:04b}"
    number_str_2 = swap_chars(number_str_2, 1, 3)
    number_str_2 = swap_chars(number_str_2, 2, 3)

    number_423 = int(number_str_2, 2)
    matrix_423[number, number_423] = 1

# print(matrix_23)
print(matrix_423)

# rho = np.zeros([16, 16])
# for i in [1,2,4,8]:
#     for j in [1,2,4,8]:
#         rho[i, j] = 0.25
#
# print(rho)

kron_list = list()
for i in range(300):
    print("rho_" + str(i) + "_1 = Semidefinite(4)")
    print("rho_" + str(i) + "_2 = Semidefinite(4)")
    print("rho_" + str(i) + "_3 = Semidefinite(4)")
    print("X = rand(4, 4); A = X * X'; rho_" + str(i) + "_a = A / tr(A)")
    print("X = rand(4, 4); B = X * X'; rho_" + str(i) + "_b = B / tr(B)")
    print("X = rand(4, 4); C = X * X'; rho_" + str(i) + "_c = C / tr(C)")
    kron_list.append("kron(rho_" + str(i) + "_1, rho_" + str(i) + "_a)")
    kron_list.append("exchange_1 * kron(rho_" + str(i) + "_2, rho_" + str(i) + "_b) * exchange_1")
    kron_list.append("exchange_2 * kron(rho_" + str(i) + "_3, rho_" + str(i) + "_c) * exchange_2")

print("rho_next = " + "+".join(kron_list))





