import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# Control Panel
# =========================================================
TestCases = 5
#You may thank the kind people at "Hungry African Children" for these quotes
MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "You Guys have no idea what they do in Labs - some cool proff",
    "Ye soya analytic hain - Veer",
    "Whoever shares a meal with hungry becomes an African - Darshik",
    "Aurat chahe kitni bhi badi ban jaye kabhi ek bada aadmi nahi ban sakti - Veir",
    "Sir ise fork kehte hai - Epic Nescafe Guy",
    "We are the most coordinated group of people who have never once been coordinated - Mythos",
    "Life Sucks- Monsieur Power",
    "Throughout Heaven And Earth, I Am Alone - Parth Pawar",
    "👍 - Abhay",
    "12th - Shubham Sharma",
    "some telegu nonsense - AK",
    "Ubuntu is just Arch for people who want to sleep - Kratos",
    "Bro really thought git push --force would save his semester - Shreyas",
    "The longer you don't pee, the longer you pee",
    "It's better to pee in shower than to shower in pee",
    "Uhh... Ummmmm,... - My Friend when i asked him to say something to go in the Fallfest Test Case Bank"
    "I hope you understand sir - lord tejasva",
    "Ye Kalyug nhi, Kaale logo ka yug hain - Abhay",
    "Mujhe Kya, mein toh Pattagobi hun",
    "kuch theek nhi hoga bhai, tension lete reh",
    "I am your luke, Father - Professional Larper",
    "R u a complan boy - My First Grade Teacher",
    "A man who doesnt blow up his claude credits atleast once a day needs to find a purpose in life",
    "Every 60 Seconds in Africa a minute Passes",
    "Together, we cannot stop this",
    "We can defeat the demon king, with the power of friendship and this Rocket Launcher that I found",
    "Consider this as some epic statement",
    "You do not need to memorize the formulas, just know them by-heart - My Classical Mechanics Proffesor",
    "https://www.youtube.com/watch?v=xvFZjo5PgG0",
    "Haan Bhai, chinta mat kr- mein kr lunga... - My Teammate who was supposed to help me make these PSs",
    "Me, Petting my cat after realising the Nuclear Bomb wasn't my fault. Thank you for everything Whiskers, i will now let you go - The first suggested text in my Pinterest"
]
# =========================================================
# Activation
Evaluation = True
# =========================================================


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


# TestCase Runner (tm) :D
def RunTests(MessageSend, Debug=False):
    Passed = True

    for i in range(TestCases):
        # Choose a Message as a TestCase
        SecretMessage = random.choice(MessageList)
        ReqLen = len(SecretMessage) * 8

        # Defining the input register
        QReg = QuantumRegister(ReqLen, "Q")
        CReg = ClassicalRegister(ReqLen, "C")
        qc = QuantumCircuit(QReg, CReg)

        # Place the System into pairwise Entangled Bell states
        for j in range(ReqLen // 2):
            qc.h(2 * j)
            qc.cx(2 * j, 2 * j + 1)
            qc.barrier()

        try:
            # Call User Function for testing
            CheckCircuit = MessageSend(SecretMessage, qc)

            simulator = AerSimulator(method="stabilizer")
            transpiled_circuit = transpile(CheckCircuit, simulator)
            result = simulator.run(transpiled_circuit, shots=1).result()
            counts = result.get_counts(transpiled_circuit)
            # Reverse endianness because qiskit is little-endian
            measured_result = list(counts.keys())[0][::-1]
            SolutionDecoupled = BinToMessage(measured_result)
        except Exception as e:
            print(f"Test Case {i+1} crashed: {type(e).__name__}: {e}")
            Passed = False
            break

        if Debug:
            print(f"Deciphered Message: {SolutionDecoupled}")

        if SolutionDecoupled == SecretMessage:
            print(f"Test Case {i+1} Passed")
        else:
            print(f"Failed on Test Case {i+1}, Input Message: {SecretMessage}")
            Passed = False
            break

    if Passed:
        print("Problem Statement Successful, You may move on")
    else:
        print("Error in Solution, Try again.")
    return Passed