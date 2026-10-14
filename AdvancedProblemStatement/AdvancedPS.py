from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import random
from qiskit import QuantumCircuit
from qiskit.transpiler.passes.analysis import num_qubits
import random
from qiskit import QuantumCircuit
from AdvancedPSAutochecker import (BobRead, BobRecheck, EncryptMessage,
                                   InitialTransfer, StarterFunct)


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
    KeyArr = [random.randint(0,1) for _ in range(num_qubits)]

    BasisArr = ""
    for i in range(num_qubits):
        Basis = random.choice(['D', 'O'])
        BasisArr = BasisArr + Basis

    qc = StarterFunct()
    qc = PrepareEncodeQubits(KeyArr, BasisArr, qc, num_qubits)

    TransferredCircuit = InitialTransfer(qc)

    Matches = BobRead(qc, BasisArr)

    CommonKey_Alleged = []
    for i in range(len(Matches)):
        CommonKey_Alleged.append(KeyArr[Matches[i]])

    CommonKeyCheck = []
    for i in range(100):
        CommonKeyCheck.append(CommonKey_Alleged[i])

    UnMatchRate = BobRecheck(CommonKeyCheck)

    if UnMatchRate >= 0.10:
        return "Compromised"

    else:
        TrueKey = []
        for i in range(256):
            TrueKey.append(CommonKey_Alleged[100 + i])

        EncryptedMsg = EncryptMessage(Message, TrueKey)

        return EncryptedMsg