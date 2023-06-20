# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
new_list = []
compteur_newliste = 0
for compteur in range(1,6,2):
    compteur2 = compteur - 1
    new_list = new_list + [my_list[compteur]]
    my_list[compteur] = my_list[compteur2]
    my_list[compteur2] = new_list[compteur_newliste]
    compteur_newliste +=1

#print(new_list)
print(my_list)

