"""Tests for solution to Exercise 5.10."""

import numpy as np
import pytest

import cirq

from exercise_5_10 import generate_cat_state_circuit


@pytest.mark.parametrize('n_qubits', range(1, 10))
def test_cat_state(n_qubits):
    qubits = cirq.LineQubit.range(n_qubits)

    ops = generate_cat_state_circuit(qubits)
    circuit = cirq.Circuit.from_ops(ops)
    simulator = cirq.Simulator()
    result = simulator.simulate(circuit, qubit_order=qubits)
    dim = 2 ** n_qubits
    cat_state = (2 ** (-0.5)) * (np.eye(1, dim) + np.eye(1, dim, dim - 1))
    assert np.isclose(result.final_state, cat_state).all()


@pytest.mark.parametrize('n_qubits', range(1, 10))
def test_cat_circuit_gate_locality(n_qubits):
    qubits = cirq.LineQubit.range(n_qubits)
    ops = generate_cat_state_circuit(qubits)
    for op in cirq.flatten_op_tree(ops):
        assert len(op.qubits) <= 2
