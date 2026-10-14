import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# Control Panel
# =========================================================
TestCases = 5
Num_Qubits = 1024 #Initial Key Length
EavesdropProb = 0.3 #Probability that eve is listening in in the first place
ChoiceProb = 0.2 #Probability that eve listens to a specific qubit out of a state
MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "You Guys have no idea what they do in Labs - some cool proff",
    "Ye soya analytic hain - Vier",
    "Whoever shares a meal with hungry becomes an African - Darshik",
    "Aurat chahe kitni bhi badi ban jaye kabhi ek bada aadmi nahi ban sakti - Veir",
    "Sir ise fork kehte hai - Epic Nescafe Guy",
    "We are the most coordinated group of people who have never once been coordinated - Mythos",
    "Life Sucks- Monsieur Power",

]
# =========================================================
# Activation
Evaluation = True
# =========================================================

def StarterFunct():
    qr = QuantumRegister(Num_Qubits, name="qubit")
    cr_eve = ClassicalRegister(Num_Qubits, name="eve_read")
    cr_bob = ClassicalRegister(Num_Qubits, name="bob_read")
    qc = QuantumCircuit(qr, cr_eve, cr_bob)
    return qc

def InitialTransfer(qc):
    Eavesdrop = random.choices([0, 1], weights=[1 - EavesdropProb, EavesdropProb], k=1)[0]
    if Eavesdrop == 1 :
        for i in range(Num_Qubits):
            Choice = random.choices([0, 1], weights=[1 - ChoiceProb, ChoiceProb], k=1)[0]
            if Choice == 1:
                eve_temp_basis = random.choice(['+', 'X'])
                if eve_temp_basis == 'X':
                    qc.h(qr[i])
                    qc.measure(qr[i], cr_eve[i])

                elif eve_temp_basis == '+':
                    qc.measure(qr[i], cr_eve[i])

                if qc.switch(cr_eve[i]) == 0:
                    qc.id(qr[i])
                elif qc.switch(cr_eve[i]) == 1:
                    qc.x(qr[i])

                if eve_temp_basis == 'X':
                    qc.h(qr[i])


            else:
                continue

        return qc

    else:
        return qc

def BobRead(qc):
    BobBasis = ""
    for i in range(Num_Qubits):
        Basis = random.choice(['D', 'O'])
        BobBasis = BobBasis + Basis

    

from AdvancedPS import *
