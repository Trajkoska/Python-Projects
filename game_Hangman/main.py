import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 

| |
| |                   
| ' \ /  | '_ \ / _ | ' `  \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (| | | | |
|| ||_,|| ||_, || || ||_,|| ||
                    / |
                   |/    '''
cities = ["Chicago", "Houston", "London", "Tokyo", "Paris", "Sydney", "Toronto", "Mumbai"]
a = random.choice(cities)
a = a.lower()
lista = []

for i in range(len(a)):
    lista.append("_")
print(lista)
print("Guess the city")
zivoti = 6
print(stages[zivoti])
while "_" in lista and zivoti != 0:
    b = input("Insert letter: ")
    if b in lista:
        print("This letter was inserted, try again! ")
    else:
        greska = 1
        for i in range(len(a)):
            if b == a[i]:
                lista[i] = b
                greska = 0
            else:
                pass
        if greska == 1:
            zivoti -= 1
            os.system('cls')
            print(stages[zivoti])
        print(lista)
input("Click enter")
