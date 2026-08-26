"""
numeros = [133, 180, 150, 60, 55, 666, 899, 541]

max = 0
for scores in numeros:
    if scores > max:
        max = scores

print(max)
"""
# for loops and ranges
"""
for number in range (1, 11, 3): # genera un numero que empieza de 1 hasta 11 pero va de tres en tres
    print(number)
"""

"""
total = 0
for i in range (1, 101):
    total += i

print(total)
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)