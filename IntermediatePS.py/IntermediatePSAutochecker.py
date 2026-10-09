import random

MessageList = [
    "Abhimanyu is Doraemon - well known fact",
    "You Guys have no idea what they do in Labs - some cool proff",
    "Ye soya analytic hain - Vier",
    "Whoever shares a meal with hungry becomes an African - Darshik",
    "Aurat chahe kitni bhi badi ban jaye kabhi ek bada aadmi nahi ban sakti - Veir",
    "Sir ise fork kehte hai - Epic Nescafe Guy",
    "We are the most coordinated group of people who have never once been coordinated - Mythos",
    "Welcome to Hungry African Children",
]
SecretMessage = random.choice(MessageList)


print(SecretMessage)
print(len(SecretMessage))
ReqLen = len(SecretMessage) * 8
print(f"Required Length of Qubits = {ReqLen}")
