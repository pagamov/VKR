from time import time

def Factor(n, B):
    # color text!!!
    from color import color

    # some functions to support functionality (LOL)
    from lib import GCD,Q
    q = Q(n)

    # class generating Factor base
    from Primes import Primes
    primes = Primes(n,B,q)

    # func to suive until we have critical len of smooth numbers
    from Suive import suive

    t = time()
    smooth_numbers = suive(q,primes)
    print("time:",color(round(time() - t,4),"time"))

    print("Total number of smooth numberes:",color(len(smooth_numbers),'data'))
    print(color("All smooth numbers found",'strong')+'\n')

    # matrix solves
    print('Start making matrix\n')
    t = time()
    from Matrix_solver import Matrix_solver
    matrix = Matrix_solver(primes.p)

    # form matrix with given smooth
    for smooth in smooth_numbers:
        matrix.add(smooth[2])
    print("Matrix builded in:",color(round(time() - t,4),"time"))

    # possibe outcome [None,None] or if we LUCKY give ans as [gcd,n//gcd]
    solve = matrix.solve(smooth_numbers)

    return solve
