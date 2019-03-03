import func as f


def simplified_alg(a, b, c, u):
    return (u - a) | (b & c)





a = {1, 2, 3, 4, 5}
c = {1, 2}
b = {1, 2, 3, 4, 5, 6}
u = {i for i in range(10)}

print(simplified_alg(a, b, c, u))
