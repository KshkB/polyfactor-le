from collections import defaultdict
# from collapse import collapse

## POLYNOMIALS f ARE DEFINED BY ARRAYS OF COEFFICIENTS
## They are evaluated at a particular value 
def PolyEval(f, val):
    curr_val = 0
    for i, c in enumerate(f):
        curr_val += c*(val**i)

    return curr_val

## POLYNOMIAL ADDITION
def PolyAdd(f, g):
    new_poly = {}
    l_f = len(f)
    l_g = len(g)

    if l_f < l_g:
        l = l_f
        for i in range(l):
            new_poly[i] = f[i] + g[i]

        for i in range(l, l_g):
            new_poly[i] = g[i]
    
    if l_g < l_f:
        l = l_g
        for i in range(l):
            new_poly[i] = f[i] + g[i]

        for i in range(l, l_f):
            new_poly[i] = f[i]

    if l_f == l_g:
        l = l_f
        for i in range(l):
            new_poly[i] = f[i] + g[i]
    
    new_poly_arr = [new_poly[key] for key in new_poly]
    return new_poly_arr

## POLYNOMIAL MULTIPLICATION 
def PolyMult(f, g):
    coeff_matrix = []
    for c in f:
        row = [c*d for d in g]
        coeff_matrix.append(row)

    new_coeffs = defaultdict(float)
    l = len(coeff_matrix)
    for i in range(l):
        row = coeff_matrix[i]
        for j in range(len(row)):
            new_coeffs[i+j] += coeff_matrix[i][j]
    new_coeffs_arr = [new_coeffs[key] for key in new_coeffs]
    return new_coeffs_arr

## SCALAR MULT
def PolyMultScalar(scalar, f):
    scalar_poly = [scalar]
    return PolyMult(scalar_poly, f)
