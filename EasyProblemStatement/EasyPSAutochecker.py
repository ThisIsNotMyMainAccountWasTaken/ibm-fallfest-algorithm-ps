from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random
from EasyPS import *

InputList = [0, 1, 2, 3]
TestCases = 3

Evaluation = True

for i in range(TestCases):
    # Choose an Integer and Create the Base Circuit
    ChosenInteger = random.choice(InputList)
    qc = QuantumCircuit(2, 2)
    # Maximally Entangle the state
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()

    # Query the User Function to get resultant
    CheckCircuit = IntSend(ChosenInteger, qc)
    CorrectInteger = bin(ChosenInteger)[2:].zfill(2)

    simulator = AerSimulator(method="stabilizer")
    transpiled_circuit = transpile(CheckCircuit, simulator)

    job = simulator.run(transpiled_circuit, shots=1)
    result = job.result()

    counts = result.get_counts(transpiled_circuit)
    measured_result = list(counts.keys())[0]

    if measured_result == CorrectInteger:
        print(f"Test Case {i+1} Passed")
        continue
    else:
        print(f"Failed on Test Case {i}, Input Integer {ChosenInteger}")
        Evaluation = False
        break

if Evaluation == True:
    print("Problem Statement Successful, You may move on")
else:
    print("Error in Solution, Try again.")


from qiskit_aer import AerSimulator

