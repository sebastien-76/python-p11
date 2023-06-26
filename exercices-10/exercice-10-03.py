# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoie une valeur booléenne
# - renvoie `oui` si le paramètre est égal à True
# - renvoie `non` si le paramètre est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3
def oui_non(value: bool) -> bool:
    if value:
        return 'oui'
    else:
        return 'non'
    
resultat = oui_non(True)
print(resultat)

resultat = oui_non(False)
print(resultat)



