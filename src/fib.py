import functools
import argparse
import numpy as np
from numpy.linalg import matrix_power
import textwrap
import time
import threading
from multiprocessing import Process, Queue

from parallelization import parallel_computing_recursive, fibonacci_worker, fib_even, fib_odd


def fibonacci_recursive(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater than 0")
    if n < 2:
        return n
    if parallel and depth:
        return parallel_computing_recursive(fibonacci_recursive, n, depth)
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fib_matrix(n: int, parallel :bool = False, depth :int = 0):
    if n%2 == 0:
        return fib_even(n, parallel, depth)
    return fib_odd(n, parallel, depth)


def fibonacci_iterative(n: int) -> int:
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


cache = {}

def fibonacci_recursive_memoization(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    if parallel and depth:
        return parallel_computing_recursive(fibonacci_recursive_memoization, n, depth)
    
    nth = fibonacci_recursive_memoization(n - 1) + fibonacci_recursive_memoization(n - 2)

    cache[n] = nth

    return nth



@functools.cache
def fibonacci_recursive_cache(n: int, parallel :bool = False, depth :int = 0) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    if parallel and depth:
        return parallel_computing_recursive(fibonacci_recursive_cache, n, depth)
    return fibonacci_recursive_cache(n - 1) + fibonacci_recursive_cache(n - 2)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('nth', type=int, help='n-th fibonacci number')
    parser.add_argument('-f', '--func', choices=['n','m','i','r','rm','rc'], help=textwrap.dedent('''\
        the fibonacci function to choose:
          n   - naive
          m   - matrix exponentiation
          i   - iterative
          r   - recursive
          rm  - recursive with memoization
          rc  - recursive with cache
        '''), default='n', metavar='FUNC')
    parser.add_argument('-p','--parallel', help='use the function with parallelization', action="store_true")
    args = parser.parse_args()


    result = fibonacci_recursive_cache(args.nth)