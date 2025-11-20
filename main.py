#### Fonction secondaire
"""
Exercice permettant de savoir si un nombre est premier ou non 

Modules:
isprime(p)
main()
"""
def isprime(p):
    """
    Args:
    p: une chaine de caractères

    Returns:
    un booléen, true si le nombre est premier, false sinon
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(p**0.5) + 1, 2):
        if p % i == 0:
            return False
    return True

#### Fonction principale

def main():
    """
    Permet d'effectuer des tests pour des entiers de 0 à 100
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
