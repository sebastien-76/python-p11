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

