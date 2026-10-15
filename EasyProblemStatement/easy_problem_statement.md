# Easy Problem Statement

Alice and her friend, Bob, have happened upon a complicated machine with a few qubits sustained within. They want to play around with it(reasonably so) and so, after remembering something about the word 'Entanglement', want to try sending secret messages to each other. They decide to be a bit conservative with the machine, since they do not know how many qubits it can produce, and so decide to try sending each other a number between 0 and 3.

## Task Overview

Your task is to help Alice and Bob implement the required quantum algorithm. Using a provided entangled qubit pair, you need to encode a 2-bit integer into the quantum state using Clifford gates, perform measurements, and return the circuit.

## Function Signature & Requirements

* Function Name: IntSend(A, B)
* Parameters:
  * A: An integer belonging to the set {0, 1, 2, 3}.
  * B: A Qiskit Circuit object containing a quantum register of 2 qubits prepared in the ⎪𝝓⁺〉 state (at indices [0] and [1]).
* Return Value: A Qiskit Circuit object containing the circuit with measurements (qc.measure()) already applied.

## Implementation Guidelines

1. Binary Conversion: Convert the integer A into a 2-bit binary format.
2. Gate Operations: Apply a valid set of single-qubit or multi-qubit Clifford gates to the circuit, using the binary bits to control the operations.
3. Measurement: Include measurement instructions for the qubits. The grader treats index [0] as the MSB (Most Significant Bit) and index [1] as the LSB (Least Significant Bit).
4. Helper Functions: Additional helper functions are permitted, but they must be called directly or indirectly within IntSend(A, B).
5. Grading: The grader handles the simulation automatically; do not include simulation code inside your function.

Best of Luck on your endeavour to aid Alice and Bob.
