from inside_polytope_demo.compute import generate_dicke_state, compute_all_4_qubit

if __name__ == "__main__":
    rho = generate_dicke_state(4, 2)
    compute_all_4_qubit(rho)