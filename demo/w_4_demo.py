from tools import compute_all_stretchable, compute_all_producible, compute_all_partitionable

if __name__ == "__main__":
    N = 4
    P = [['0001', '0010'], ['0001', '0100'], ['0001', '1000'],
         ['0010', '0100'], ['0010', '1000'], ['0100', '1000']]

    # compute_all_stretchable(P, N)
    # compute_all_producible(P, N)
    compute_all_partitionable(P, N)
