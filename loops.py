import random

#while c'est comme un if mais qui est répété
#while False:
#    print("Ce message ne s'affiche pas")
    
# while True:
#    #continue permet de reprendre au début de la boucle suivante
#    continue
#    print("Ce message est affiché en boucle")
#    #break permet de sortir d'une boucle à tout moment
#    break

dice = random.randint(1, 6)
while dice != 6:
    print(f"Je n'ai pas tiré un 6, mais un {dice} je recommence")
    dice = random.randint(1, 6)

print(f"{dice},J'ai tiré un 6")

#recréation de la for classique avec la boucle while
i = 0
while i < 10:
    print(f'{i = }')
    i += 1

#boucle for classique en python
#0 est inclus, 10 est exclu
for i in range(0, 10):
        print(f'{i = }')

# boucle à rebours
for i in range(10, 0, -1):
        print(f'{i = }')

users = ['foo', 'bar', 'baz']

for user in users:
      print(user)

for i, user in enumerate(users):
      print(f"{i=}, {user=}")
z

#boucle for
for i in range(0, len(users)):
      user = users[i]
      print(f"{i =}, {user =}")

#accumulateur
accumulateur = 0
for i in range(1, 11):
    accumulateur += i
    print(f"{i = }")
    print(f"{accumulateur= }")
print()
print(f"{accumulateur = }")

#Liste 2D
players = [
      [42000, 46400, 32103],
      [16700, 44667, 57987]
]
line = 0
col = 0
print(players[line][col])

for line_index in range(0, len(players)):
      line = players[line_index]
      for col_index in range(0, len(line)):
            score = line[col_index]
            print(score)

#utiliser la valeur précedente dans une boucle
numbers = [123, 42, 1000, 3.14]
#au le 1er tour, il n'y a pas de valeur précédente
previous = None

for number in numbers:
      #on affiche la valeur du tour actuel
      print(number)
      #on affiche la valeur du tour précédent
      print(previous)
      #on sauvegarde la valeur du tour actuel pour le tour suivant
      #cette valeur deviendra la valeur du tour précédent
      previous = number

