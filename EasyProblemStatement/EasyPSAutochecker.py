from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

# Control Panel
# =========================================================
InputList = [0, 1, 2, 3]
TestCases = 3
# =========================================================


def RunTests(IntSend):
    Passed = True

    for i in range(TestCases):
        # Choose an Integer and Create the Base Circuit
        ChosenInteger = random.choice(InputList)
        qc = QuantumCircuit(2, 2)
        # Maximally Entangle the state
        qc.h(0)
        qc.cx(0, 1)
        qc.barrier()

        CorrectInteger = bin(ChosenInteger)[2:].zfill(2)

        try:
            # Query the User Function to get resultant
            CheckCircuit = IntSend(ChosenInteger, qc)

            simulator = AerSimulator(method="stabilizer")
            transpiled_circuit = transpile(CheckCircuit, simulator)
            result = simulator.run(transpiled_circuit, shots=1).result()
            counts = result.get_counts(transpiled_circuit)
            measured_result = list(counts.keys())[0]
        except Exception as e:
            print(f"Test Case {i+1} crashed: {type(e).__name__}: {e}")
            Passed = False
            break

        if measured_result == CorrectInteger:
            print(f"Test Case {i+1} Passed")
        else:
            print(f"Failed on Test Case {i+1}, Input Integer {ChosenInteger}")
            Passed = False
            break

    if Passed:
        print("Problem Statement Successful, You may move on")
    else:
        print("Error in Solution, Try again.")
    return Passed