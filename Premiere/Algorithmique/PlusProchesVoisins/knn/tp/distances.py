def minkowski(x: tuple, y: tuple, q: int)->float:
    """
    :param x: (iterable) an n-uple
    :param y: (iterable) an n-uple
    :param q: (int) 
    :return: (float) distance between x and y
    """
    return sum(abs(x[i]-y[i])**q for i in range(len(x))) ** (1/q)


def euclidian(x, y):
    """
    :param x: (iterable) an n-uple
    :param y: (iterable) an n-uple
    :return: (float) distance between x and y

    >>> abs(euclidian((0,0), (1,1)) - 2**.5) < 0.001
    True
    """
    return minkowski(x, y, 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
