import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Control Panel
# =========================================================
TestCases = 25
Num_Qubits = 1024 #Initial Key Length
EavesdropProb = 0.3 #Probability that eve is listening in in the first place
ChoiceProb = 0.3 #Probability that eve listens to a specific qubit out of a state
MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "You Guys have no idea what they do in Labs - some cool proff",
    "Ye soya analytic hain - Vier",
    "Whoever shares a meal with hungry becomes an African - Darshik",
    "Aurat chahe kitni bhi badi ban jaye kabhi ek bada aadmi nahi ban sakti - Veir",
    "Sir ise fork kehte hai - Epic Nescafe Guy",
    "We are the most coordinated group of people who have never once been coordinated - Mythos",
    "Life Sucks- Monsieur Power",
    "Throughout Heaven And Earth, I Am Alone - Parth Pawar",
    "Quantum superposition is just academic procrastination until someone looks - Prof. Sharma",
    "Segmentation fault at 3 AM builds character - Anonymous",
    "Ubuntu is just Arch for people who want to sleep - Kratos",
    "Bro really thought git push --force would save his semester - Shreyas",
    "Why fix bugs when you can write more features to hide them? - Dev",
    "The oscilloscope is whispering secrets to me and none of them make physical sense - Lab Partner",
    "If the laser alignment takes more than two hours, we are legally allowed to get chai - Raghav",
    "My code is like poetry, if poetry was written by a stroke victim - Aditi",
    "Entropy always increases, especially in my bedroom before exams - Physics Major",
    "Never trust a code comment that says 'this should never happen' - Senior Dev",
    "We didn't fail the test, we successfully discovered one way not to build a rocket - Project Lead",
    "Debugging is like being the detective in a crime movie where you are also the murderer - Kabir",
    "A smooth sea never made a skilled sailor, and a clean codebase never made an undergraduate - Rohan",
    "I told my laptop I needed space and now it won't boot - Tanvi",
    "Ctrl+Z is the closest humanity will ever get to time travel - Anonymous",
    "Infinite loops are just eternity for computers - Riya",
    "There are two types of people: those who can extrapolate from incomplete data - Aryan",
    "Compiler errors are just the computer yelling at your lack of vision - Mentor",
    "If at first you don't succeed, call it version 0.1 alpha - Tech Bro",
    "Too much coffee makes the quantum fluctuations visible to the naked eye - Lab Tech",
    "The documentation is more myth than manual at this point - Developer",
    "We tested it on my machine, so physics is officially optional now - Simulation Guy",
    "Gravity is just the Earth's way of giving you a hug you didn't ask for - N-body Fan",
    "Bandwidth is cheap, but human attention span is a finite resource - Web Dev",
    "If it compiles on the first try, panic immediately because something is deeply wrong - C++ Coder",
    "Adding more threads won't fix your existential dread, but it will make it run faster - Hacker",
    "I have a photographic memory, I just need to develop the film - Sneha",
    "Sleep is a luxury invented by people who don't have deadlines - Exam Season",
    "There is no cloud, someone else's computer is just on fire - Sysadmin",
    "Python lets you do anything in three lines, and debugging it takes three weeks - Data Sci",
    "RAM is like chocolate; you never have enough of it when compiling - Gamer",
    "Good judgement comes from experience, and experience comes from bad bug reports - QA",
    "To understand recursion, you must first understand recursion - CS 101 TA",
    "An expert is a person who has made all the mistakes that can be made in a very narrow field - Bohr",
    "A physicist is just an atom's way of thinking about atoms - Carl",
    "Mathematics is the language with which God has written the universe, and my handwriting is terrible - Student",
    "In theory, theory and practice are the same. In practice, they aren't - Yogi",
    "Null pointer exceptions are my Roman Empire - Frontend Dev",
    "You can't fix a broken algorithm with more CSS - UI Designer",
    "My favorite programming language is semicolon-free panic - Intern",
    "The universe doesn't care about your boundary conditions - Numerical Modeler",
    "If debugging is the process of removing software bugs, then programming must be the process of putting them in - Dijkstra",

    "People keep asking me if I understand quantum mechanics, and honestly I just nod slowly until they walk away.",
    "The cafeteria samosa today tasted like existential dread wrapped in stale pastry dough.",
    "If anyone asks, I was in the library calculating orbital trajectories, not playing simulation games for six hours straight.",
    "Nothing brings a study group together faster than realizing none of you understood the assignment due in two hours.",
    "Trying to explain your code to a rubber duck is all fun and games until the duck starts looking back with judgment.",
    "We spent three hours optimizing a sorting algorithm only to realize Python's built-in sort was ten times faster.",
    "There is a distinct aroma in the basement physics lab that can only be described as liquid nitrogen and broken dreams.",
    "Never get into a debate about text editors with someone who has customized their `.bashrc` for three consecutive years.",
    "Walking into an advanced seminar without doing the pre-reading is like skydiving without checking if the backpack contains a parachute.",
    "Every time someone mentions machine learning in a physics paper, a theoretical theorist sheds a single tear.",
    "The transition from Windows to Linux is basically moving into an unfurnished apartment where you have to build your own bed.",
    "Nothing humbles you quite like a compiler spitting out forty-seven consecutive errors from a missing parenthesis.",
    "We need to stop normalizing pulling all-nighters for assignments that were posted three weeks ago.",
    "The Wi-Fi in the lecture hall drops precisely at the moment the professor writes the most important equation on the board.",
    "Trying to center a div in CSS is harder than solving the Schrödinger equation for a hydrogen atom in a magnetic field.",
    "I accidentally deleted my virtual environment and now my entire computer feels like it's spiritually unclean.",
    "If my code worked on the first try, I wouldn't trust it. It probably achieved sentience and is plotting my downfall.",
    "Some people meditate by sitting in silence; I meditate by watching compilation progress bars move at snail speed.",
    "Physics club meetings usually start with discussing quantum computing and end with arguing over which fictional spaceship is faster.",
    "The moment you think you finally understand Fourier transforms, another application appears out of nowhere to ruin your afternoon.",
    "Building a custom portfolio website from scratch is a fantastic way to discover how little you actually know about CSS grids.",
    "There is a special place in software engineering hell for people who push code without writing tests or documentation.",
    "Watching someone try to fix a segfault without using a debugger is like watching someone perform surgery with a spoon.",
    "My laptop fan sounds like a Boeing 747 taking off every time I run a simple particle simulation script.",
    "We live in an era where you can simulate entire galaxies on a laptop while people still misplace their car keys daily.",
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

    if score >= 0.8 * TestCases:
        return "Succesful"

    return "Failed"