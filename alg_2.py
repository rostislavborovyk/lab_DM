from random import randint

def alg_2(x, y):

    x = tuple(x)
    y = tuple(y)
    c = []
    k=0
    for j in range(len(x)):
        for i in range(len(y)):
            if x[j] == y[i]:
                c.append(x[j])
                k += 1
    return set(c)









