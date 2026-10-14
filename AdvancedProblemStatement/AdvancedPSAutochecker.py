import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Control Panel
# =========================================================
TestCases = 20
Num_Qubits = 1024 #Initial Key Length
EavesdropProb = 0.5 #Probability that eve is listening in in the first place
ChoiceProb = 0.2 #Probability that eve listens to a specific qubit out of a state
MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "I'm Sorry, idk what variables are, I dont have a CS background - CS101 PhD TA",
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
    "Quantum superposition is just academic procrastination until someone looks - Prof. Sharma",
    "Segmentation fault at 3 AM builds character - Anonymous",
    "Ubuntu is just Arch for people who want to sleep - Kratos",
    "Bro really thought git push --force would save his semester - Shreyas",
    "Why fix bugs when you can write more features to hide them? - Dev",
    "The oscilloscope is whispering secrets to me and none of them make physical sense - Lab Partner",
    "Python lets you do anything in three lines, and debugging it takes three weeks - Data Sci",
    "To understand recursion, you must first understand recursion t can be made in a very narrow field - Bohr",
    "A physicist is just an atom's way of thinking about atoms - Carl"
    "The transition from Windows to Linux is basically moving into an unfurnished apartment where you have to build your own bed.",
    "My laptop fan sounds like a Boeing 747 taking off every time I run a simple particle simulation script.",
    """
    Chapter 1: Introduction to Computational Chaos
    Numerical simulations are an essential pillar of modern scientific inquiry, bridging the gap 
    between analytical intractability and empirical observation. When analytical solutions fail 
    due to non-linearity or high dimensionality, discrete approximation methods take over. 
    However, discretization introduces its own perils, including truncation errors, round-off 
    accumulations, and numerical instability. Understanding the delicate balance between grid 
    resolution and computational efficiency remains one of the greatest challenges for modern 
    researchers developing high-performance fluid dynamics and particle physics frameworks.
    """,
    """
    Project Specification Document: Autonomous Quantum Comparator
    
    1. Objective: Design and implement a robust quantum comparator circuit using Qiskit 
       to evaluate relative magnitudes of superposition states without collapsing the wave function prematurely.
    2. Constraints: Execution time must remain polynomial with respect to qubit count. Ancilla qubits 
       should be minimized to prevent noise accumulation on NISQ hardware architectures.
    3. Deliverables: Fully tested Python modules, automated autochecker scripts, and comprehensive 
       benchmark reports detailing gate fidelity across simulated backend environments.
    """,
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore 
    eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
    in culpa qui officia deserunt mollit anim id est laborum.

    Section 2: The Evolution of Text
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots 
    in a piece of classical Latin literature from 45 BC, making it over 2000 years 
    old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, 
    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum 
    passage, and going through the cites of the word in classical literature, 
    discovered the undoubtable source. 

    Section 3: The Canonical Source
    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum 
    et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This 
    book is a treatise on the theory of ethics, very popular during the Renaissance. 
    The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a 
    line in section 1.10.32. The standard chunk of Lorem Ipsum used since the 1500s 
    is reproduced below for those interested. 

    Section 4: Modern Integration
    It is a long established fact that a reader will be distracted by the readable 
    content of a page when looking at its layout. The point of using Lorem Ipsum 
    is that it has a more-or-less normal distribution of letters, as opposed to 
    using 'Content here, content here', making it look like readable English. Many 
    desktop publishing packages and web page editors now use Lorem Ipsum as their 
    default model text, and a search for 'lorem ipsum' will uncover many web sites 
    still in their infancy. Various versions have evolved over the years, sometimes 
    by accident, sometimes on purpose (injected humour and the like).
    """,
    """
    Appendix B: Notes on Linux Terminal Environment Setup
    Configuring a personalized development workspace on Ubuntu requires patience and precision. 
    By crafting custom bash wrapper scripts placed within `~/.local/bin`, users can streamline repetitive 
    workflows, manage virtual environments efficiently, and integrate Git SSH authentication seamlessly. 
    Additionally, fine-tuning GTK dark themes and custom keybindings ensures maximum comfort during 
    late-night coding and physics problem-solving sessions.
    """
]
# =========================================================
# Activation
Evaluation = True
# =========================================================

_BobBits = []
_BaseMatches = []
_EvePresent = False

# =========================================================

def StarterFunct():
    qr = QuantumRegister(Num_Qubits, name="qubit")
    cr_eve = ClassicalRegister(Num_Qubits, name="eve_read")
    cr_bob = ClassicalRegister(Num_Qubits, name="bob_read")
    qc = QuantumCircuit(qr, cr_eve, cr_bob)
    return qc

def InitialTransfer(qc):
    global _EvePresent

    qr = qc.qregs[0]
    cr_eve, cr_bob = qc.cregs

    Eavesdrop = random.choices([0, 1], weights=[1 - EavesdropProb, EavesdropProb], k=1)[0]
    _EvePresent = bool(Eavesdrop)

    if Eavesdrop == 1 :
        for i in range(Num_Qubits):
            Choice = random.choices([0, 1], weights=[1 - ChoiceProb, ChoiceProb], k=1)[0]
            if Choice == 1:
                eve_temp_basis = random.choice(['O', 'D'])
                if eve_temp_basis == 'D':
                    qc.h(qr[i])
                    qc.measure(qr[i], cr_eve[i])

                elif eve_temp_basis == 'O':
                    qc.measure(qr[i], cr_eve[i])

                if eve_temp_basis == 'D':
                    qc.h(qr[i])

            else:
                continue

        return qc

    else:
        return qc

def BobRead(qc, AliceBasis):

    qr = qc.qregs[0]
    cr_eve, cr_bob = qc.cregs
    global _BobBits, _BaseMatches


    BobBasis = ""
    for i in range(Num_Qubits):
        Basis = random.choice(['D', 'O'])
        BobBasis = BobBasis + Basis

    for i in range(Num_Qubits):
        if BobBasis[i] == 'D':
            qc.h(qr[i])
            qc.measure(qr[i], cr_bob[i])
        elif BobBasis[i] == 'O':
            qc.measure(qr[i], cr_bob[i])

    simulator = AerSimulator(method="stabilizer")
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()
    raw_result_str = list(counts.keys())[0]
    bob_str, _ = raw_result_str.split(" ")
    _BobBits = [int(b) for b in bob_str[::-1]]

    _BaseMatches = []

    for i in range(Num_Qubits):
        if AliceBasis[i] == BobBasis[i]:
            _BaseMatches.append(i)

    return _BaseMatches

def BobRecheck(EveSharedKey):
    Errors = 0
    n = len(EveSharedKey)
    for i in range(n):
        if EveSharedKey[i] != _BobBits[_BaseMatches[i]]:
            Errors += 1

    return Errors / n


def BitsToBytes(bits):
    # 256 bits -> 32 bytes
    assert len(bits) == 256, "Key must be exactly 256 bits"
    return int("".join(map(str, bits)), 2).to_bytes(len(bits) // 8, "big")

def EncryptMessage(Message, KeyBits):
    key = BitsToBytes(KeyBits) 
    nonce = os.urandom(12) 
    ciphertext = AESGCM(key).encrypt(nonce, Message.encode("utf-8"), None)
    return nonce + ciphertext 

def DecryptMessage(Packet, KeyBits):
    key = BitsToBytes(KeyBits)
    nonce, ciphertext = Packet[:12], Packet[12:]
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)  # raises InvalidTag if key is wrong
    return plaintext.decode("utf-8")


from cryptography.exceptions import InvalidTag

def BobDecrypt(Packet):
    BobKey = [_BobBits[i] for i in _BaseMatches[100:356]]
    return DecryptMessage(Packet, BobKey)


#Test Case Running Begins

def RunTests(AliceJob):
    score = 0
    for t in range(TestCases):
        msg = random.choice(MessageList)
        try:
            out = AliceJob(msg, Num_Qubits)
        except Exception as e:
            print(f"Test {t+1}: FAIL (crashed: {type(e).__name__}: {e})")
            continue

        if out == "Compromised":
            ok, note = _EvePresent, "Compromised"
            if not ok:
                note = "false alarm (no Eve)"
        else:
            try:
                ok = (BobDecrypt(out) == msg)
                note = "decrypted" if ok else "wrong message"
            except InvalidTag:
                ok, note = False, "keys differ (Eve not noticed)"
            except Exception as e:
                ok, note = False, f"bad output ({type(e).__name__})"

        score += ok
        print(f"Test {t+1}: {'PASS' if ok else 'FAIL'} ")
    print(f"Score: {score}/{TestCases}")

    if score >= (4 * TestCases) // 5:
        return "Problem Statement Successful, You may move on"

    return "Error in Solution, Try again."