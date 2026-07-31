import random
#random es una generacion de texto de manera aleatoria *

"""
Import random = es una funcion para generar datos aleatorios
random.int(a, b) = genera numeros aleatorios, a y b es el rango de los datos pero no los toma
random.random() = este genera float numeros de 0 a 1
random.uniform(a,b) = genera float numeros pero toma en cuenta a y b
random.choice() selecciona de manera aleatoria items de una lista
"""
"""
# ejercicio cara o cruz
coin = random.randint(0,1)
if coin == 0:
    print("cara")

elif coin == 1:
    print("cruz")

"""
#**************************************************************************************
#LISTAS DE PYTHON
"""
 variable = [item1, item2]
 para acceder a los items se empieza de 0  y para el ultimo objeto es -n
 se pueden cambiar valores accediento a la lista 
 lista[posicion] = "nuevo item"


para añadir nuevos valores a la lista se utiliza .append()
lista.append("item a agrega")
""" 

#EJERCICIO DE LISTAS
"
"""
amigos = ["Angel", "Pedro", "John", "Martin", "Lucas"]
selector = amigos[random.randint(0,4)]
print(selector)
"""    

# NESTED LISTS
"""
lista = [lista1, lista2]
"""