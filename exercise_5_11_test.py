"""Tests for solution to Exercise 5.11."""

import numpy as np
import pytest

import cirq

from exercise_5_11 import generate_w_state_circuit


def get_w_state(n_qubits):
    state = np.zeros(2**n_qubits)
    for i in range(n_qubits):
        state[2**i] = n_qubits ** (-0.5)
    return state


@pytest.mark.parametrize('n_qubits', range(1, 10))
def test_w_state(n_qubits):
    qubits = cirq.LineQubit.range(n_qubits)

    ops = generate_w_state_circuit(qubits)
    circuit = cirq.Circuit.from_ops(ops)
    simulator = cirq.Simulator()
    result = simulator.simulate(circuit, qubit_order=qubits)
    w_state = get_w_state(n_qubits)
    assert np.isclose(result.final_state, w_state).all()


@pytest.mark.parametrize('n_qubits', range(1, 10))
def test_w_circuit_gate_locality(n_qubits):
    qubits = cirq.LineQubit.range(n_qubits)
    ops = generate_w_state_circuit(qubits)
    for op in cirq.flatten_op_tree(ops):
        assert len(op.qubits) <= 2
