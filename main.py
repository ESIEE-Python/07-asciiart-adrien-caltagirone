''' module '''
#### Imports et définition des variables globales
from itertools import groupby

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    return [(i, len(list(j))) for i, j in groupby(s)]


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            break
    return [(char, count)] + artcode_r(s[count:])

#### Fonction principale
def main():
    '''main'''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
