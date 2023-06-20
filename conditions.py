import random

#block if1
if True:
        print("Ce message s'affichera toujours")

if False:
        print("Ce message ne s'affichera jamais")

#block if2

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(number1)
print(number2)

if number1 < number2:
        print("La variable number1 est plus petite que la variable number2")

if number1 < number2:
        print("La variable number1 est plus petite que la variable number2")
else:
        print("La variable number1 est plus grande que la variable number2")


#block if3
if number1 < number2:
        print("La variable number1 est plus petite que la variable number2")
elif number1 > number2:
        print("La variable number1 est plus grande que la variable number2")
else:
        print("Les variables sont égales")


#opérateurs boolééns
print(not True)
print(not False)

#opérateur de négation
#Table de vérité
#A      not A
#True   False
#False  True

#OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#table de vérité de l'opérateur OU logigue
#A          B           A ou B
#True       True        True
#True       False       True
#False      True        True
#False      False       False

#ET logique
print('ET logique')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#table de vérité de l'opérateur OU logigue
#A          B           A ou B
#True       True        True
#True       False       False
#False      True        False
#False      False       False

#opérateur NAND ( not and)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#table de vérité de l'opérateur OU logigue
#A          B           not ( A and B )
#True       True        False
#True       False       True
#False      True        True
#False      False       True

#utilisation de l'opérateur AND pour voir si une variable est dans interval de valeurs
#age >= 12 and age <= 25
#est equivalent (en python uniquement ) 12 <= age <= 25

#OU exclusif
#A               B               XOR             OR
#True            True            False           True
#True            False           True            True
#False           True            True            True
#False           False           False           False

print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# exo course operateur OU logique
# affichez :
# je peux aller faire les courses si j'ai un moyen de paiement
# je ne peux pas aller faire mes courses si je n'ai aaucun moyen de paiement

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))
print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash or has_cb :
        print('Je peux aller faire mes courses')
else: print('Je ne peux pas aller faire mes courses')

# exo course operateur ET logique
# affichez :
# je peux aller faire les courses si j'ai un moyen de paiement
# je ne peux pas aller faire mes courses si je n'ai aaucun moyen de paiement
print('Exercice courses ET')
has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))
print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash == False and has_cb == False:
        print('Je ne peux pas aller faire mes courses')
else: print('Je peux aller faire mes courses')

if not has_cash and not has_cb:
        print('Je ne peux pas aller faire mes courses')
else: print('Je peux aller faire mes courses')

#Combinaison d'opérateur AND et OR

#user_level = 2
#user_score = 143
#user_credit = 0

#if user_level <= 3 and user score >= 100 or user_credit >=10
#        print("Le joueur peut acheter du matériel")
#else print("Le joueur ne peut pas acheter du matériel")

#exo carte de reduction
#determiner la carte de réduction à laquelle le voyager a droit
#entre 0 et 11 ans inclus, le voyager a le droit à la gratuité
#entre 12 et 25 ans inclus, le voyager a le droit à une réduction de 50%
#entre 26+ et 64 ans inclus, le voyager a le droit à une reduction de 10%
#au delà de 65 ans inclus, le voyager a le droit à une réduction de 50%
age = random.randint(0, 99)
print(age)
if age <= 11:
        print("le voyageur voyage gratuitement")
elif age <= 25:
        print("le voyageur a le droit à 50% de réduction")
elif age <= 64: print("le voyageur a le droit à 10% de réduction")
else: print("le voyageur a le droit à 50% de réduction")



