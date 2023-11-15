import numpy as np

def swap_chars(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


# rho = np.zeros([8, 8])
# for i in [1,2,4]:
#     for j in [1,2,4]:
#         rho[i, j] = 0.25
#
# print(rho)

np.set_printoptions(threshold=np.inf)

for num1 in range(4):
    for num2 in range(num1 + 1, 5):
        the_matrix = np.zeros([32, 32])
        print(num1, num2)
        for number in range(32):
            number_str = f"{number:05b}"
            # print(number_str)
            number_str = swap_chars(number_str, num1, num2)
            # print(number_str)
            number_23 = int(number_str, 2)
            the_matrix[number, number_23] = 1
        print(the_matrix)

# kron_list = list()
# for i in range(1):
#     print("rho_" + str(i) + "_1 = Semidefinite(2)")
#     print("rho_" + str(i) + "_2 = Semidefinite(2)")
#     print("rho_" + str(i) + "_3 = Semidefinite(2)")
#     print("rho_" + str(i) + "_4 = Semidefinite(4)")
#     print("rho_" + str(i) + "_5 = Semidefinite(4)")
#     print("rho_" + str(i) + "_6 = Semidefinite(4)")
#     print("X = rand(4, 4); A = X * X'; rho_" + str(i) + "_a = A / tr(A)")
#     print("X = rand(4, 4); B = X * X'; rho_" + str(i) + "_b = B / tr(B)")
#     print("X = rand(4, 4); C = X * X'; rho_" + str(i) + "_c = C / tr(C)")
#     print("X = rand(2, 2); D = X * X'; rho_" + str(i) + "_d = D / tr(A)")
#     print("X = rand(2, 2); E = X * X'; rho_" + str(i) + "_e = E / tr(B)")
#     print("X = rand(2, 2); F = X * X'; rho_" + str(i) + "_f = F / tr(C)")
#     kron_list.append("kron(rho_" + str(i) + "_1, rho_" + str(i) + "_a)")
#     kron_list.append("kron(rho_" + str(i) + "_d, rho_" + str(i) + "_4)")
#     kron_list.append("exchange * kron(rho_" + str(i) + "_5, rho_" + str(i) + "_e) * exchange")
#     kron_list.append("exchange * kron(rho_" + str(i) + "_b, rho_" + str(i) + "_2) * exchange")
#     kron_list.append("kron(rho_" + str(i) + "_6, rho_" + str(i) + "_f)")
#     kron_list.append("kron(rho_" + str(i) + "_c, rho_" + str(i) + "_3)")
#
# print("rho_next = " + "+".join(kron_list))