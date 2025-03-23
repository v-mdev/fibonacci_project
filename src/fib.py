import functools
import argparse

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be grater than 0")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(9))




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

print(functools.__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nth", type=int, help="Nth Fibonacci number.")
    args = parser.parse_args()

    result = fibonacci_recursive(args.nth)
    print(result)