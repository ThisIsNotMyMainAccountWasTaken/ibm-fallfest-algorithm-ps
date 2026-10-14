import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# Control Panel
# =========================================================
TestCases = 5
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