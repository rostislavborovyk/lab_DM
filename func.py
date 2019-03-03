from random import randint
def rand(a):
    A={randint(0,20) for i in range(a)}
    return A


def universal(u):
    U = {i for i in range(u)}
    return U