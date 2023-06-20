# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

import random

# réponse 7.18
number = 0
compteur = 0
while number != 100:
    number = random.randint(1, 101)
    compteur += 1
print(f"{compteur} essai(s) ont été nécessaire(s) pour avoir {number}")
