import numpy


def compute_fidelity(PP, QQ):
    S, U = numpy.linalg.eig(PP)
    sqP = U * numpy.diag([s ** 0.5 for s in S]) * U.H  # Square root of P.
    S, U = numpy.linalg.eig(QQ)
    sqQ = U * numpy.diag([s ** 0.5 for s in S]) * U.H  # Square root of Q.
    Fnp = sum(numpy.linalg.svd(sqP * sqQ)[1])  # Trace-norm of sqrt(P)·sqrt(Q).

    print("Fidelity F(P,Q) computed by NumPy:", round(Fnp, 4))
