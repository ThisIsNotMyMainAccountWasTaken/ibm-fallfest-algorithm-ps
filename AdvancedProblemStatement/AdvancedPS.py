from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import random
from qiskit import QuantumCircuit
from qiskit.transpiler.passes.analysis import num_qubits
from AdvancedPSAutochecker import InitialTransfer, StarterFunct

def PrepareEncodeQubits(KeyArr, BasisArr, qc, N):
    InKey = N
    for i in range(InKey):
        if KeyArr[i] == 0:
            if BasisArr[i] == 'D':
                qc.h(i)
            elif BasisArr[i] == 'O':
                continue
        elif KeyArr[i] == 1:
            if BasisArr[i] == 'D':
                qc.x(i)
                qc.h(i)
            elif BasisArr[i] == 'O':
                qc.x(i)
    return qc

def AliceJob(Message, num_qubits):
    KeyArr = []
    for i in range(InKey):
        Bit = random.randint(0,1)
        KeyArr.append(Bit)

    BasisArr = ""
    for i in range(num_qubits):
        Basis = random.choice(['D', 'O'])
        BasisArr = BasisArr + Basis

    qc = StarterFunct()
    qc = PrepareEncodeQubits(KeyArr, BasisArr, qc, 1024)

    TransferredCircuit = InitialTransfer(qc)