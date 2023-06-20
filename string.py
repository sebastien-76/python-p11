text1 = "lorem"
text2 = "ipsum"

#concatenation
text3 = text1 + " "+ text2
print(text3)

#interpolation avec une f-string
text3 = f"{text1} {text2}"
print(text3)


# attention la concaténation ne fonctionne qu'avec des str
# il faut convertir les autres types en string
mails = 52
text4 = "Vous avez " + str(mails) + " non lus"
print(text4)

# Répétition de texte
text5 = "foo" * 3
print(text5)

# Affichage de valeurs arrondies sans arrondir la variable
number1 = 10 / 3
text6 = f"10 / 3 est à peu près égal {number1:.2f}"
print(text6)

# Les fonctions associées aux str
#longueur du chaine de caractères 
text7 = "foo bar baz foo"
print(len(text7))

#nb d'occurence
print(text7.count('foo'))

#retrouve l'emplacement d'un mot
position = text7.find('foo')
print(position)

#pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position +1))

#si le mot est absent, la fonction renvoie -1
position = text7.find('lorem')
print(position)

#remplacement de mots

print(text7.replace('foo', 'lorem'))
print(text7)

text7 = text7.replace('foo', 'lorem')
print(text7)

#split & join
list1 = text7.split(' ')
print(list1)
text8 = "+".join(list1)
print(text8)

#Documenter ue fonction


def ouiNon(value):

    """cette fonction renvoie 
    oui si parametre passé est True
    non si False
    ""dans les autres cas

    value bool  valeur qui sera transformée en oui ou non
    return str"""
    
    if value == True:
        return "oui"
    elif value == False:
        return "non"

    return ""
help(ouiNon)
# ou print(ouiNon.__doc__)