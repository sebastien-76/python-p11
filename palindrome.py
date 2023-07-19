compteur = 0
n = 1
while n <= 1000000:
    n_str = str(n)
    n_str_inverse=""
    i = len(n_str) - 1
    while i >= 0:
        n_str_inverse = n_str_inverse + n_str[i]
        i -= 1
    if n_str_inverse == n_str:
        compteur += 1
    n +=1
print(compteur)
