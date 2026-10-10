import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from IntermediatePS import *


# Convert the String to integer list, sub helper func
def StringToInt(message: str) -> list[int]:
    integer_list = [ord(char) for char in message]
    return integer_list


# Auto fomrulates the intended solution from the message produced, returns long str with intended solution
def SolutionCreator(SecretMessage):
    ascii_ints = StringToInt(SecretMessage)
    bin_list = [format(code, "08b") for code in ascii_ints]
    pairwise_bin = [
        binary_str[j : j + 2] for binary_str in bin_list for j in range(0, 8, 2)
    ]
    print(f"No. Of sets required: {len(pairwise_bin)}")

    SolString = "".join(bit for bit in pairwise_bin)
    return SolString


# Converts the given Solution String into a message
def BinToMessage(SolStr):
    MsgLen = len(SolStr) // 8
    Message = []
    for Char in range(MsgLen):
        CharMap = ""
        for bit in range(8):
            CharMap += SolStr[8 * Char + bit]
        Message.append(CharMap)

    Sentence = "".join(chr(int(b, 2)) for b in Message)
    return Sentence


# Control Panel
# =========================================================
TestCases = 1
"""
MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "You Guys have no idea what they do in Labs - some cool proff",
    "Ye soya analytic hain - Vier",
    "Whoever shares a meal with hungry becomes an African - Darshik",
    "Aurat chahe kitni bhi badi ban jaye kabhi ek bada aadmi nahi ban sakti - Veir",
    "Sir ise fork kehte hai - Epic Nescafe Guy",
    "We are the most coordinated group of people who have never once been coordinated - Mythos",

]
"""
MessageList = ["Hello"]
# =========================================================
# Activation
Evaluation = True


# TestCase Runner tm :D
for i in range(TestCases):
    # Choose a Message as a TestCase
    SecretMessage = random.choice(MessageList)

    # Test and calculations (Temporary) REMOVE BEFORE ACTAULLY RUNNING IT YOU IDIOT >:C
    print(f"Test case {i + 1} Message: {SecretMessage}")
    ReqLen = len(SecretMessage) * 8
    print(f"Required Length of Qubits = {ReqLen}")

    # Defining the input register
    QReg = QuantumRegister(ReqLen, "Q")
    CReg = ClassicalRegister(ReqLen, "C")
    qc = QuantumCircuit(QReg, CReg)

    # Place the System into pairwise Entangled Bell states
    for i in range(ReqLen // 2):
        qc.h(2 * i)
        qc.cx(2 * i, 2 * i + 1)
        qc.barrier()

    # Calculate Intended Solution
    Solution = SolutionCreator(SecretMessage)

    # Call User Function for testing
    CheckCircuit = MessageSend(SecretMessage, qc)

    # Simulator shit
    simulator = AerSimulator(method="stabilizer")
    transpiled_circuit = transpile(CheckCircuit, simulator)
    job = simulator.run(transpiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts(transpiled_circuit)
    measured_result = list(counts.keys())[0]
    measured_result = list(counts.keys())[0][::-1]  # Reverses endianness if needed
    print(f"The Measrued result is: {measured_result}")

    # Temporary Testing code to ensure un-break. REMOVE BEFORE ACTAULLY RUNNING IT YOU IDIOT >:C
    print(f"Solution: {Solution}")
    SolutionDecoupled = BinToMessage(Solution)
    # print(f"Deciphered Message(Autochecker Side): {SolutionDecoupled}")
