

def solve_quadratic(a,b,c):

    solution1 = (-(1 * b) + (b**2 - 4*a*c) ** (1/2)) / (2*a)
    solution2 = (-(1 * b) - (b**2 - 4*a*c) ** (1/2)) / (2*a)

    if (b**2 - 4*a*c) < 0:
        return

    elif solution1 == solution2:
        return int(solution1)

    else:
        return int(solution1), int(solution2)

print(solve_quadratic(1,-5,6))
print(solve_quadratic(1,4,4))
print(solve_quadratic(1,0,1))
