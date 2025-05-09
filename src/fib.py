import functools
import argparse
import textwrap
import time
from parser import parallel_args, parallel_choices
from parallelization import parallel_computing_recursive, fib_even, fib_odd

def fib_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be grater than 0")
    if n < 2:
        return n
    
    n0 = 0
    n1 = 1
    for _ in range(n):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return n0


def fib_matrix(n: int, parallel :bool = False, depth :int = 0):
    if n%2 == 0:
        return fib_even(n, parallel, depth)
    return fib_odd(n, parallel, depth)


def fib_recursive(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater than 0")
    if n < 2:
        return n
    if parallel and depth:
        return parallel_computing_recursive(fib_recursive, n, depth)
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


cache = {}

def fib_recursive_memoization(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    if parallel and depth:
        return parallel_computing_recursive(fib_recursive_memoization, n, depth)
    
    nth = fib_recursive_memoization(n - 1) + fib_recursive_memoization(n - 2)

    cache[n] = nth

    return nth


@functools.cache
def fib_recursive_cache(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    if parallel and depth:
        return parallel_computing_recursive(fib_recursive_cache, n, depth)
    return fib_recursive_cache(n - 1) + fib_recursive_cache(n - 2)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('nth', type=int, help='n-th fibonacci number')
    parser.add_argument('-f', '--func', choices=parallel_choices, help=textwrap.dedent('''\
        the fibonacci function to choose:
          i   - iterative
          m   - matrix exponentiation
          r   - recursive
          rm  - recursive with memoization
          rc  - recursive with cache
        '''), default='r', metavar='FUNC')
    parser.add_argument('-p','--parallel', help='use the function with parallelization', action="store_true")
    parser.add_argument('-d','--depth', type = int, help='how many cores to use in parallelization', default=2)

    args = parser.parse_args()

    if args.func == 'i':
        result = fib_iterative(args.nth)
    if args.func == 'm':
        result = parallel_args(fib_matrix, args.nth, args.parallel, args.depth)
    if args.func == 'r':
        result = fib_recursive(fib_matrix, args.nth, args.parallel, args.depth)
    if args.func == 'rm':
        result = fib_recursive_memoization(fib_matrix, args.nth, args.parallel, args.depth)
    if args.func == 'rc':
        result = parallel_args(fib_recursive_cache, args.nth, args.parallel, args.depth)

    