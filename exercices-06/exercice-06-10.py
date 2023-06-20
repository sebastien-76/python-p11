# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
somme = 0
for compteur in range(len(my_list)):
    somme += my_list[compteur]
moyenne = somme / len(my_list)
print(moyenne)
