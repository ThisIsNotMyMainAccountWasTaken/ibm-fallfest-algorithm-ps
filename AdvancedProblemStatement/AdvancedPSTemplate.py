
# =========================================================
#Leave these imports alone. You do not need to worry about these
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import random
from qiskit import QuantumCircuit
from AdvancedPSAutochecker import (BobRead, BobRecheck, EncryptMessage,
                                   InitialTransfer, StarterFunct)
# =========================================================

def AliceJob(Message, num_qubits):
    # =========================================================
    #Generate a random Array of 0 or 1 of length num_qubits, and a String of randomly generated string (ex: DODDO for D: Diagonal, O: Orthogonal)
    #Use D and O itself, not any other letters


    # =========================================================

    qc = StarterFunct() #This gives you the pre-prepared circuit as said in the PS

    # =========================================================
    #Implement the Encoding of the Qubits according to the Given Rules


    # =========================================================

    TransferredCircuit = InitialTransfer(qc) #This produces the state right before it is sent over to Bob. This might or might not produce an Eavesdropper :)

    # =========================================================
    #Utilize the BobRead() Function to simulate Bob reading the qubits, then comparing with yours to get matches indices
    #Feed in Circuit,Array, where Array is the Basis you used to feed into BobRead()
    #BobRead() returns a list of indices where basis measurements match
    #Use this to form a Primary Matching Key
    #Obtain a Array of first 100 matching bits, say CommonKey



    # =========================================================

    UnMatchRate = BobRecheck(CommonKey) #This gives you the %error in matching post sending

    # =========================================================
    #Using this Unmatch rate, decide a unmatchrate above which we can say that the line is compromised
    #If compromised, return "Compromised"
    #If not, form a true key, using the next 256 indices of the Common Key




    # =========================================================

    #Once you have the Key, you can encrypt the Message using the following function:
    #EncryptedMessage = EncryptMessage(Message, TrueKey)

    #return this Encrypted Message from the AliceJob Function



#You may utilize helper functions whenever needed, at your own risk :D
#Best of luck at implementing this basic algorithm used for QKD