from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def MessageSend(Message, qc):
    # Converting message into 8-bt ASCII Format
    ASCIIBin = [format(ord(code), "08b") for code in Message]
    print(ASCIIBin)

    # Take the ASCII Binary and teh, uhh..... convert it into pairwise for superdense
    PairwiseBin = [
        binary_str[j : j + 2] for binary_str in ASCIIBin for j in range(0, 8, 2)
    ]
    SetsNum = len(PairwiseBin)

    # Apply Alice Side of Superdense extended to all sets
    for i in range(SetsNum):
        c = PairwiseBin[i][0]
        d = PairwiseBin[i][1]
        if c == "1":
            qc.x(2 * i + 1)  # Target qubit
        if d == "1":
            qc.z(2 * i + 1)  # Target qubit

    qc.barrier()

    # Apply Bob Side of Superdense extended to all sets
    for i in range(SetsNum):
        qc.cx(2 * i, 2 * i + 1)
        qc.h(2 * i)

    qc.barrier()

    # Apply the Measurements and save to Classical Register
    for i in range(2 * SetsNum):
        qc.measure(i, 2 * SetsNum - 1 - i)

    return qc
