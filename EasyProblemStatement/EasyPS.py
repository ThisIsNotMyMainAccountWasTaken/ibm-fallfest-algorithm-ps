from qiskit import QuantumCircuit


def IntSend(In, qc):
    input = bin(In)[2:].zfill(2)

    Input = str(input)
    c = Input[0]
    d = Input[1]

    if d == "1":
        qc.z(0)
    if c == "1":
        qc.x(0)

    qc.cx(0, 1)
    qc.h(0)

    qc.measure(0, 0)
    qc.measure(1, 1)

    return qc
