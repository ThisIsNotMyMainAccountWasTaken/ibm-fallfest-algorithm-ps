# Advanced Problem Statement (ongoing)

Hello there. So you managed to do the previous job that was assigned to Alice and Bob huh? That's great, amazing even. Now, it seems Alice and Bob have moved to farther places, and would prefer that their messages be encrypted. Furthermore, we are now having a large lack of qubits from the machine, due to the sheer amount of ~~shitposting~~ Intellectual conversations that take place between them. And so logically, they have recruited you, this time as a paid Entrepreneur to help them. You have grown much since the last time this has occurred, you are now a self-proclaimed expert at Quantum Communications. Now, help them send encrypted messages over a public line, while avoiding an eavesdropper who tries to listen in. And, as common sense might say, the name of the eavesdropper is Eve (Short for Evenika Luthenborg Van Fitzgerald Margaret Riccardo Agnes Louis Warwick Bob the First)

## Task Overview

Your task is to help Alice and Bob implement the required quantum algorithm. There are too many characters to be sent over to fit in the amount of qubits that the machine has been found to produce, and so now, you must implement a slightly simplified version of the BB84 Algorithm (Yes, that's how bad this one is gonna be. I am telling you the name of the algorithm this time. Fear me, mortal mind). You are provided with 1024 Qubits, and will be using them to send arbitrarily long messages in an encrypted fashion. The Detailed Explanation on how to do so is attached

## Function Signature & Requirements (TBD NOT DONE AT ALL)

* Function Name: MessageSend(A, B)
* Parameters:
  * A: A String: the message
  * B: A Qiskit Circuit object containing a quantum register of 8N qubits prepared in the ⎪𝝓⁺〉 state (at indices [0] and [1] pairwise, so [2], [3]. And so on). N is the number of characters in A.
* Return Value: A Qiskit Circuit object containing the circuit with measurements (qc.measure()) already applied.

## Implementation Guidelines

1. Base + Key Choice: For Alice, Randomly choose a 1024 long string of 0s or 1s. Randomly choose another 1024 long string of either Diagonal (D) or Rectilinear(R). (It is suggested to study what the BB84 encoding is).
2. Polarization: Follow these rules to encode them into qubits, and then send them over to Bob from Alice. Use the aforementioned function to send this. At this point, there might be an eavesdropper, or there might not be one. We do not know
3. Scan over Public Channel: Bob randomly guesses and reads out the qubits with random basis. Alice and Bob discuss used basis over public channel, You receive a list of indices at which Bob guessed correctly.
4. Sift through the key: Now that we know the correctly guessed bits, we should have roughly half of them survive, so we use the 512 bits that we have. We will read out 100 of these by a predefined algorithm, and see if they match.
5. Using the Params provided: Decide if there was an Eve, if yes, return "Compromised" to signify Eve's Existence.
6. Uncipher the Message: In case there is no eve, return the Uncovered unencrypted text. To do so follow the following steps
   1. Decide the Key: Choose the first 256 of the remaining bits and define that as the Key. Both Alice and Bob know to use the first 256 as the ones they require.
   2. Encrypt: Encrypt your message with the aforementioned function, before sending it over to Bob
   3. Decipher: Send the encrypted text over a public channel, where Bob will retrieve it and decipher the message on their own end with the key which they already know.

Good job, you are now in possession of the power to participate in capitalism. You are rich with a whole ($0.05) to your name. Do the only logical thing and gamble it, multiply your money, and buy a pet Goose :D. Or you can be boring and invest it, but whatever. K Bye, go do the other Tracks now :P
