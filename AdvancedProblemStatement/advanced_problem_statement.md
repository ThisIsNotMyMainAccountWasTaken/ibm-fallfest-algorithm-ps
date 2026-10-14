# Advanced: Alice, Bob and the Goose Fund

Hello there. So you managed to do the previous job that was assigned to Alice and Bob? Amazing, even.

Now Alice and Bob have moved to farther places, and would prefer that their messages be **encrypted**. Qubits are scarce: the machine only produces **1024 per round**, thanks to the sheer volume of intellectual conversations between them. They have recruited you, this time as a paid Entrepreneur, to help them talk over a **public line** while an eavesdropper tries to listen in.

The eavesdropper is Eve (short for Evenika Luthenborg Van Fitzgerald Margaret Riccardo Agnes Louis Warwick Bob the First).

You are now a self-proclaimed expert in Quantum Communications. This time, we will even tell you the name of the algorithm: **BB84**. Fear it, mortal mind.

Your payment is a whole **$0.05**. Gamble it and buy a pet goose.

---

## Task

Implement a simplified BB84 pipeline:

1. Alice encodes random bits into 1024 qubits using random bases.
2. The qubits travel to Bob. **Eve may or may not have intercepted them. You do not know.**
3. Bob measures every qubit in a random basis.
4. Over the public channel they compare bases and keep only the positions where the bases matched (the *sifted* positions).
5. Part of the sifted key is sacrificed to test for Eve. If Eve is detected, give up on the round.
6. If the channel is clean, the next 256 sifted bits become a shared secret key, which is used to encrypt the message with a one-time pad.

You do **not** need to write the simulator, Eve, or the public channel. The autochecker provides them. You implement five functions.

---

## BB84 reference (everything you need)

| Basis | Bit 0 | Bit 1 |
|-------|-------|-------|
| `R` (rectilinear / Z) | \|0⟩ | \|1⟩ |
| `D` (diagonal / X)    | \|+⟩ | \|−⟩ |

Measuring in the same basis the qubit was prepared in returns the encoded bit with certainty. Measuring in the other basis returns a uniformly random bit.

---

## Functions to implement

Submit a single Python file defining exactly these functions. Qiskit is the only quantum library allowed.

### 1. `alice_prepare(n, rng) -> (QuantumCircuit, bits, bases)`

- `n` is the number of qubits (always 1024). `rng` is a `numpy.random.Generator`. **All randomness must come from `rng`.**
- Return a circuit on `n` qubits, with **no classical bits**, that prepares Alice's states, along with:
  - `bits`: list of `n` ints in `{0, 1}`
  - `bases`: list of `n` strings in `{'R', 'D'}`
- Only these gates are allowed: `id, x, y, z, h, s, sdg, barrier`.
- Bits and bases must be uniformly random.

### 2. `bob_measure(circuit, rng) -> (QuantumCircuit, bases)`

- `circuit` is the circuit that arrives at Bob. It may have been tampered with by Eve.
- Append Bob's basis changes and measurements to a **copy** of `circuit`. Do not modify or rebuild the incoming gates.
- Add **one** classical register of `n` bits. Qubit `i` must be measured exactly once into classical bit `i`.
- Return the final circuit and the list of Bob's bases (`'R'` or `'D'`, chosen randomly using `rng`).

### 3. `process_keys(a_bits, a_bases, b_bits, b_bases) -> (compromised, key_alice, key_bob)`

All four arguments are lists of length 1024. `b_bits` is the measurement result from Bob's circuit (index `i` is classical bit `i`).

1. **Sift:** let `S` be the ordered list of indices `i` where `a_bases[i] == b_bases[i]`.
2. **Test:** use the **first 100** indices of `S`. If Alice's and Bob's bits differ at **any** of them, return `(True, [], [])`.
3. **Key:** otherwise, take the **next 256** indices of `S` (that is, `S[100:356]`). Return `(False, key_alice, key_bob)`, where each key is the list of that party's own bits at those positions.

### 4. `encrypt(message, key) -> str`

- Convert `message` to bits using 8-bit ASCII, MSB first, character by character.
- XOR with the first `8 * len(message)` bits of `key`.
- Return the ciphertext as a string of `'0'`/`'1'` characters.

### 5. `decrypt(cipher, key) -> str`

Inverse of `encrypt`. Returns the plaintext message.

---

## Messages longer than 32 characters

A 256-bit key can encrypt exactly 32 ASCII characters. For longer messages, the autochecker runs **one fresh BB84 round per 32-character block**, with a new set of 1024 qubits and a new key each time. If **any** round reports `compromised`, the whole transmission is reported as `"Compromised"`.

Your functions only ever see a single round at a time.

---

## Grading (100 points)

| Section | Check | Points |
|---|---|---|
| Alice | Format, circuit really encodes the claimed bits and bases, randomness | 15 |
| Bob | Format, incoming circuit preserved, correct measurement physics | 15 |
| Keys | Correct keys and no false alarm when no Eve is present | 8 |
| Keys | Eve is flagged when she intercepts | 7 |
| Crypto | `encrypt` matches the spec, `decrypt` inverts it, edge cases | 15 |
| End-to-end | 6 full scenarios: 1-char message, exactly 32 chars, 100 chars (4 rounds), and 3 Eve attacks (full intercept in a random basis, full intercept in a fixed basis, and 50% intercept) | 40 |

Everything is simulated noiselessly, so a clean channel must produce a perfect result. A false alarm counts as a failure.

---

## Notes and warnings

- Eve may intercept **all** qubits or only some. Your test must be able to catch a partial attack.
- Bob must **not** use a fixed basis, and Alice must **not** use constant bits.
- Do not simulate the circuit yourself inside your functions. The autochecker does that.
- Submissions are time-limited. A reference solution runs the whole suite in about 5 seconds.

---

## Skeleton

```python
from qiskit import QuantumCircuit, ClassicalRegister

def alice_prepare(n, rng):
    ...
    return qc, bits, bases

def bob_measure(circuit, rng):
    ...
    return qc, bases

def process_keys(a_bits, a_bases, b_bits, b_bases):
    ...
    return compromised, key_alice, key_bob

def encrypt(message, key): ...
def decrypt(cipher, key): ...
```

Test locally with the provided autochecker:

```
python autochecker_advanced.py my_submission.py
```

Good luck. Capitalism awaits.
