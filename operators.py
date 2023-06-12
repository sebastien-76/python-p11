#import du module ramdom
import random


#arithmétiques
#égalité
a = 123 + 42
b = 123 - 42
c = 123 * 42
d = 123 / 42

print("abc" == "def")

password = "abc"
user_input = "def"
print(password == user_input)

#division entiere
a = 123 // 42
print(a)

#modulo ou reste de la division euclidienne
a = 53
print(a % 2)
#s'il y a un reste, le nombre n'est pas divisible par 2, donc, il n'est pas pair

a = 74
print( a % 2)
#s'il y a un reste, le nombre n'est pas divisible par 2, donc, il n'est pas pair

#puissance, exponentiation
# deux puissance trois
a = 2 ** 3

#Opérateurs de comparaison
#égalité
print(123 == 123)

#plus grand que
print(123 > 42)

#plus grand ou égal
print(123 >= 42)
print(42 >= 42)

#plus petit ou égal
print(42 <= 42)

#différent de 
print(123 != 42)

#strictement plus petit
print(123 < 42)

# incrementation
b = 0
b += 1
b += 1
print(b)

# decrementation
b = 0
b -= 1
print(b)

# multiplication
c = 3
# c = c * 2
c *= 2
print(c)

# division
d = 10
# d = d / 3
d /= 3
print(d)

# division entiere
e = 10
# e = 10 // 3
e //= 3
print(e)

# operateur d'inclusion
text1 = "Lorem ipsum"
print("e" in text1)
print("Lorem" in text1)
print("lorem" in text1)

list1 = ["Lorem","ipsum"]
print("e" in list1)
print("ipsum" in list1)
#recherche l'element "e"  ( faux ) ou "ipsum" ( vrai )

#comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0, 100)

print(f'{e= }')
print(f'{f= }')


result = e == f
print(result)

# est une expression
# 1 +1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> 2 > 306 -> False
# random.randint(0,100) -> 100

# pas une expression
# print(100)