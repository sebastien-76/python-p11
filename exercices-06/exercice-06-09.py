# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
somme = 0
for compteur in range(len(my_list)):
    somme += int(my_list[compteur])
print(somme)
