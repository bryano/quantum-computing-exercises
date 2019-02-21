"""Solution to Exercise 5.10."""

from typing import Sequence

import numpy as np

import cirq


def generate_cat_state_circuit(qubits: Sequence[cirq.QubitId]) -> cirq.OP_TREE:
    """Returns operations that take the zero state to the cat state.
    
    Args:
        qubits: a sequence giving the qubits on which the operations are to
            act.
    Returns: The operations.
    
    Specifically, the circuit maps ⎢0⋯0⟩to (⎢0⋯0⟩ + ⎢1⋯1⟩)/sqrt(2).
    """
    pass # TODO: implement this
