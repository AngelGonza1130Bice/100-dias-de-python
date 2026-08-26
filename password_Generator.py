import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input("How many symbols would you like?\n"))

nr_numbers = int(input("How many numbers would you like?\n"))

letras = nr_letters
symbolos = nr_symbols
numeros = nr_numbers

password = []

for i in range(letras):
    password.append(random.choice(letters))

for e in range(symbolos):
    password.append(random.choice(symbols))

for o in range(numeros):
    password.append(random.choice(numbers))

# Join es utilizado para unir elementos de una lista y las commilas para decir que no quiero espacios
New_password = ''.join(password)

print(f"Your temporary password is '{New_password}'.")