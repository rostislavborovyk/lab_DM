def basic_alg(a, b, c, u):
    d = (u - a) | ((u - a) | b) & ((u - a) | c) | (u - b) & ((b & c) | (b & (u - c)))
    return d

a = {1, 2, 3, 4, 5}
c = {1, 2}
b = {1, 2, 3, 4, 5, 6}
u = {i for i in range(10)}

#print(u)
#print(basic_alg(a, b, c, u))

