# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a: float, b: float) -> int:
    if a > b:
        return 1
    elif a < b: 
        return -1
    else: return 0

resultat = compare(3.14, 10.1 )
print(resultat)

resultat2 = compare(10.1, 3.14)
print(resultat2)

resulat3 = compare(3.14, 3.14)
print(resulat3)

