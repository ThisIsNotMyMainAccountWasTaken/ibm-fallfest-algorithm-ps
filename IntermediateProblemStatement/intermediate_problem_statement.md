# Intermediate Problem Statement

Amazing News, Alice and Bob can now send each other Integers reliably. But now that we know that is possible, it is time to extend this to a new level. Gone are the times of sending Integers, it is time to send over entire encoded messages. And just like the last time, you (YES YOU AGAIN), are Alice and Bob's ~~Unpaid Servant ~~Helper in this process. This time, your purpose in life is to extend the previous strategy to send over encoded text messages.

## Task Overview

Your task is to help Alice and Bob implement the required quantum algorithm. You are provided with exactly the required amount of entangled pairs of qubit. Convert the text provided into simplified ASCII(8-bit to make it simpler), encode in a similar way pairwise, and use a similar algorithm with only Clifford gates, perform measurements, and return the circuit.

## Function Signature & Requirements

* Function Name: MessageSend(A, B)
* Parameters:
  * A: A String: the message
  * B: A Qiskit Circuit object containing a quantum register of 8N qubits prepared in the ⎪𝝓⁺〉 state (at indices [0] and [1] pairwise, so [2], [3]. And so on). N is the number of characters in A.
* Return Value: A Qiskit Circuit object containing the circuit with measurements (qc.measure()) already applied.

## Implementation Guidelines

1. ASCII Conversion: Convert the String A into simplified 8-bit ASCII, and split into sets of 2.
2. Gate Operations: Apply a valid set of single-qubit or multi-qubit Clifford gates to the circuit, using the binary bits to control the operations.
3. Measurement: Include measurement instructions for the qubits. The grader treats index [0] as the MSB (Most Significant Bit) and index [8N] as the LSB (Least Significant Bit).
4. Helper Functions: Additional helper functions are permitted, but they must be called directly or indirectly within MessageSend(A, B).
5. Grading: The grader handles the simulation automatically; do not include simulation code inside your function.

Another day for them, another unpaid internship for you. Enjoy :)
