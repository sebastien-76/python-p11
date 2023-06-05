#nombre entier, integer
number1 = 123
number1 = 42
print(number1)

# nombre a virgule floattante, float
number2 = 3.14
number2 = 2.71
print(number2)

# chaîne de caracteres, string
text1 = 'foo bar baz'
print (text1)

text2 = "foo bar baz"
print(text2)

#booléen, boolean
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

#valeur nulle, null
user_accepeted_terms = None
print(user_accepeted_terms)

#type de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_cool))
print(type(user_accepeted_terms))

#vérification du type de données
print(type(number1) is int)
print(type(number1)is str)

#  todo : interroger le type des autres variables

#transtypage int str
print(type(str(number1)))
print(str(number1))

#transtypage int bool
print(type(bool(number1)))
print(bool(number1))

#convertie en booleen, la valeur 0 donne false
number3 = 0
print(bool(number3))

#transtypage str int
#print(type(int(text1)))

#il ne peut pas y avoir chose qu'un nombre dans la chaine de caratctere si l'on veut convertir en int
text3 = "123456789"
print(type(int(text3)))

#les fonctions de transtypage
#str() converti string
#int() converti vers integer
#bool() converti vers un booleen
#float() converti vers un float
