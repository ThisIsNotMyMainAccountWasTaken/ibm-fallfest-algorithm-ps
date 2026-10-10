from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

"""
def text_to_bits(phrase: str) -> str:
        ASCII, 8 bits per character.
    return "".join(format(ord(c), "08b") for c in phrase)


def bits_to_text(bits: str) -> str:
    return "".join(chr(int(bits[i : i + 8], 2)) for i in range(0, len(bits), 8))


def build_circuit(phrase: str) -> QuantumCircuit:

    Superdense coding: each shared e-bit lets Alice send 2 classical bits
    by transmitting just 1 qubit. 8 bits/char -> 4 e-bits per character.
    Pair i carries bits[2i] (-> Z) and bits[2i+1] (-> X).
    Classical register: c[2i], c[2i+1] hold the pair's two bits in order.

    bits = text_to_bits(phrase)
    if len(bits) % 2:
        bits += "0"
    n = len(bits) // 2  # number of e-bits / transmitted qubits

    alice = QuantumRegister(n, "alice")
    bob = QuantumRegister(n, "bob")
    c = ClassicalRegister(2 * n, "c")
    qc = QuantumCircuit(alice, bob, c)

    # 1. Share n Bell pairs
    for i in range(n):
        qc.h(alice[i])
        qc.cx(alice[i], bob[i])
    qc.barrier()

    # 2. Alice encodes two bits on her half of each pair
    for i in range(n):
        z_bit, x_bit = bits[2 * i], bits[2 * i + 1]
        if x_bit == "1":
            qc.x(alice[i])
        if z_bit == "1":
            qc.z(alice[i])
    qc.barrier()  # Alice's qubits are now "sent" to Bob

    # 3. Bob does a Bell measurement on each pair
    for i in range(n):
        qc.cx(alice[i], bob[i])
        qc.h(alice[i])
    for i in range(n):
        qc.measure(alice[i], c[2 * i])  # z bit
        qc.measure(bob[i], c[2 * i + 1])  # x bit
    return qc


def decode_counts(counts: dict) -> str:
Autograder-side: take most frequent outcome, undo Qiskit's little-endian order    key = max(counts, key=counts.get).replace(" ", "")
    return bits_to_text(key[::-1])


from qiskit_aer import AerSimulator

sim = AerSimulator()
for phrase in ["Hi", "Quantum!", "IIT Indore 2026"]:
    qc = build_circuit(phrase)
    counts = sim.run(qc, shots=100).result().get_counts()
    out = decode_counts(counts)
    print(f"{phrase!r} -> {out!r}  qubits={qc.num_qubits}  ok={out == phrase}")


SecretMessage = "Hello, there"

"""
def string_to_int(message: str) -> list[int]:
    integer_list = [ord(char) for char in message]
    return integer_list


# 1. Convert string characters to ASCII integers
ascii_ints = string_to_int(SecretMessage)
print("ASCII Ints:", ascii_ints)

# 2. Convert each ASCII integer to an 8-bit binary string
bin_list = [format(code, "08b") for code in ascii_ints]
print("8-bit Binary Strings:", bin_list)

# 3. Split all binary strings into 2-bit pairs
pairwise_bin = [
    binary_str[j : j + 2] for binary_str in bin_list for j in range(0, 8, 2)
]
print("2-bit Pairwise List:", pairwise_bin)

def MessageSend(Message, qc):
    #Converting message into 8-bt ASCII Format
    ASCIIBin = [format(code, "08b") for code in ascii_ints]
    print ASCIIBin

    #Take the ASCII Binary and teh, uhh..... convert it into pairwise for superdense
    PairwiseBin = [
        binary_str[j : j + 2] for binary_str in bin_list for j in range(0, 8, 2)
    ]
    SetsNum = len(PairwiseBin)

