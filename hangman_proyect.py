import random

# lista de palabras
lista_palabras = ["aardvark", "baboon", "camel", "clock", "mirror", "tornado", "crab", "library"]

# selecciona una palabra aleatoria
chosen_word = random.choice(lista_palabras)
word_length = len(chosen_word)

# imprime la palabra aleatoria
#print(chosen_word)

# crea los "_"
placeholder = ""

for e in range(word_length):
    placeholder += "_"
print(placeholder)

# pregunta qué letra se adivina

guess = ""

while True:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"

    print(display)