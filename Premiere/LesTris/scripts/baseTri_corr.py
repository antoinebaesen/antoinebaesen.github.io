def triParInsertion(tab):
    """ Trie le tableau tab par insertion """
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j - 1] > x:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = x

tableau = [1, 5, 2, 4, 3]
triParInsertion(tableau)
print(tableau)  # On veut [1, 2, 3, 4, 5]