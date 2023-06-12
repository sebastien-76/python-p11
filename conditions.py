import random

if True:
        print("Ce message s'affichera toujours")

if False:
        print("Ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(number1)
print(number2)

if number1 < number2:
        print("La variable number1 est plaus petite que la variable number2")