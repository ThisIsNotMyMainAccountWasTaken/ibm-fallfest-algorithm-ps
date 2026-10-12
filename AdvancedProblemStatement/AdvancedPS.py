from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def PrepareEncodeQubits(KeyArr, BasisArr, qc):
    for i in range(1024):
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

def AliceJob(Message):
    KeyArr = []
for i in range(1024):
    Bit = random.randint(0,1)
    KeyArr.append(Bit)

BasisArr = ""
for i in range(1024):
    Basis = random.choice(['D', 'O'])
    BasisArr = BasisArr + Basis

qc = QuantumCircuit(1024