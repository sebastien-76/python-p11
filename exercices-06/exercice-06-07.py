# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
#
# ATTENTION : Dans l'énoncé, quand il est écrit Xème position, cela correspond à l'index X-1

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
remplacement = my_list[1]
my_list[1] = my_list[3]
my_list[3] = remplacement
print(my_list)