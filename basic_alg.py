def basic_alg(a, b, c, u):
    return (u-a) | ((u - a) | b) & ((u - a) | c) | (u - b) & ((b & c) | (b & (u - c)))
