"""Solution to Exercise 5.11."""

from typing import Sequence

import numpy as np

import cirq


def generate_w_state_circuit(qubits: Sequence[cirq.QubitId]) -> cirq.OP_TREE:
    """Returns operations that take the zero state to the W state.
    
    Args:
        qubits: a sequence giving the qubits on which the operations are to
            act.
    Returns: The operations.
    
    Specifically, the circuit maps ⎢0⋯0⟩ to 
    
        (⎢10⋯00⟩ + ⎢01⋯00⟩ + ⋯ + ⎢00⋯01⟩)/sqrt(n),

    where n is the number of qubits.
    """
    pass # TODO: implement this
