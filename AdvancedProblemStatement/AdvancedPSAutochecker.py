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
                ok, note = False, "keys differ (Eve got through)"
            except Exception as e:
                ok, note = False, f"bad output ({type(e).__name__})"

        score += ok
        print(f"Test {t+1}: {'PASS' if ok else 'FAIL'} | Eve present: {_EvePresent} | {note}")
    print(f"Score: {score}/{TestCases}")
    return score

