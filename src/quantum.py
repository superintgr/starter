import ket, bra, tensor_product

# Two qubits are in a simultaneous eigenstate of their Z-hat observables
{ket(a), ket(b)} (a +- 1, b +- 1)
# These four states form an orthonormal basis in the Hilbert space of the combined system

# Pure state
rho-hat(t) = ket(psi(t)), bra(psi(t)) / bra(psi(t)), ket(psi(t))

class Heisenberg(Picture):
    Z(t + 1) = -Z(t)
    Y(t + 1) = +Y(t)
    X(t + 1) = -X(t)
    I(t + 1) = +I(t)

class Hadamard(Image):
    ket(+1) : (ket(+1) + ket(-1)) / root(2)
    ket(-1) : (ket(+1) - ket(-1)) / root(2)

class CNOT(Image):
    ket(x, y) = ket(x * y, y)
