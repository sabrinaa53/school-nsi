# Créé par mitan, le 01/10/2025 en Python 3.7
def triangle_pascal(n):
    ligne = [1]

    for i in range(n):
        print(ligne)

        ligne_nouvelle = [1]
        for j in range(len(ligne)-1):
            ligne_nouvelle.append(ligne[j] + ligne[j+1])
        ligne_nouvelle.append(1)


        ligne = ligne_nouvelle

triangle_pascal(3)


