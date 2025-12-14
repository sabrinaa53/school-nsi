# Créé par mitan, le 01/10/2025 en Python 3.7
from math import *
def est_premier(n):
    for x in range (2, int(sqrt(n)+1)) :
        reste = n % x
        if reste == 0 :
            return False

    return True
print(est_premier(12))