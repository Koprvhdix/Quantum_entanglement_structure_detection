from inside_polytope_demo.compute import generate_dicke_state, compute_all_4_qubit, compute_all_5_qubit

if __name__ == "__main__":
    rho = generate_dicke_state(5, 2)
    compute_all_5_qubit(rho)