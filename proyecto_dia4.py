import random
# JUEGO PIEDRA, PAPEL O TIJERAS
choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: ")

tool_1 = "rock"
tool_2 = "paper" 
tool_3 = "scissors" 

if choice == "0":
    print("Rock")

elif choice == "1":
    print("Paper")

elif choice == "2":
    print("Scissors")

#Computer's choice
print("Computer choice:")

opciones = ["Rock", "Paper", "Scissors"]
desicion = opciones[random.randint(0,2)]

if desicion == tool_1:
    print("Choose Rock")
    print("Draw")
    if desicion == tool_2:
        print("Choose Paper")
        print("You loose")
    if desicion == tool_3:
        print("Choose Scissors")
        print("You Win")

if desicion == tool_2:
    print("Choose Paper")
    print("Draw")
    if desicion == tool_1
        print("Choose Paper")
        print("Draw")


elif desicion > choice:
    print("Choose Scissors")
    print("You won")

