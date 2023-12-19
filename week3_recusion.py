def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    iteration = exp-1
    total = base

    if iteration <= 0:
        total = 1
        return total
    else:
        while iteration > 0:
            iteration -= 1
            total *= base
        return total


print round(iterPower(-4.74,5), 4)