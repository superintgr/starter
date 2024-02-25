import ket, bra, tensor_product

# Two qubits are in a simultaneous eigenstate of their Z-hat observables
{ket(a), ket(b)} (a +- 1, b +- 1)
# These four states form an orthonormal basis in the Hilbert space of the combined system

# Pure state
rho-hat(t) = ket(psi(t)), bra(psi(t)) / bra(psi(t)), ket(psi(t))
