import random
# JUEGO PIEDRA, PAPEL O TIJERAS
choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: ")

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

if desicion == choice:
    print("Choose Rock")
    print("Draw")
elif desicion < choice:
    print("Choose Paper")
    print("You lose")
elif desicion > choice:
    print("Choose Scissors")
    print("You won")

