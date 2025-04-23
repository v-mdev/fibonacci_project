import functools
import argparse
import numpy as np
from numpy.linalg import matrix_power

iterations = 0
def fibonacci_naive(n: int) -> int:
    global iterations
    if n < 0:
        raise ValueError("n must be grater than 0")
    elif n==0:
        return 0
    elif n==1:
        iterations+=1
        return 1
    else:
        iterations+=1
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)


def fibmat(n):
    i = np.array([[0, 1], [1, 1]])
    return np.matmul(matrix_power(i, n), np.array([1, 0]))[1]


def fib(n):
    if n%2 == 0:#even
        return fib_even(n)
    return fib_odd(n)

def fib_odd(N):
    n = int((N+1)/2)
    Fn = fibmat(n) 
    Fn1 = fibmat(n-1)
    return Fn1**2 + Fn**2

def fib_even(N):
    n = int(N/2)
    Fn = fibmat(n) 
    Fn1 = fibmat(n-1)
    return Fn * (2*Fn1 + Fn)


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


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be grater than 0")
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


cache = {}

def fibonacci_recursive_memoization(n: int) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    
    nth = fibonacci_recursive_memoization(n - 1) + fibonacci_recursive_memoization(n - 2)

    cache[n] = nth

    return nth


@functools.cache
def fibonacci_recursive_cache(n: int) -> int:
    if n < 0:
        raise ValueError("n must be grater or equal to zero.")
    if n < 2:
        return n
    return fibonacci_recursive_cache(n - 1) + fibonacci_recursive_cache(n - 2)

fibonacci_naive(38)
fibonacci_iterative(38)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nth", type=int, help="n-th Fibonacci number")
    args = parser.parse_args()

    result = fibonacci_naive(args.nth)
    print(result)