import polyoperations as op
import random

def generate(degree):
    d1 = random.randint(2, degree-1)
    d2 = degree - d1

    factor1 = []
    for i in range(d1):
        factor1.append(random.randint(0, 3))
    factor1.append(1)

    factor2 = []
    for i in range(d2):
        factor2.append(random.randint(0, 3))
    factor2.append(1)

    product_poly = op.PolyMult(factor1, factor2)
    product_poly = [int(num) for num in product_poly]
    return factor1, factor2, product_poly

def generate2(degree):
    d = degree - 1

    factor = []
    for i in range(d):
        factor.append(random.randint(0, 5))

    factor.append(1)

    factor2 = [random.randint(0, 5), 1]

    product = op.PolyMult(factor, factor2)
    product = [int(num) for num in product]
    return factor, factor2, product



