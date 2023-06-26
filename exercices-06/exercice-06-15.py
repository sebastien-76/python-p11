# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
# liste2=[]
# for compteur in range(len(my_list)):
#     liste2 = liste2 + [len(my_list[compteur])]
# longueur = 0max(liste2)
#print(index, valeur, longueur)

# for compteur2 in range(len(liste2)):
#     if liste2[compteur2] == longueur:
#         index = compteur2
# valeur = my_list[index]
# print(liste2)
# print(index, valeur,longueur)
index = 0
longueur = 0
valeur = ''

for i, element in enumerate(my_list):
    #print(i, element, len(element))
    if len(element) >= len(valeur):
        longueur = len(element)
        valeur = element
        index = i
        
print(index, valeur, longueur)







