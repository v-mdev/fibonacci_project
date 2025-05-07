import pytest

from fib import (
    fibonacci_iterative,
    fibonacci_naive,
    fibonacci_recursive,
    fibonacci_recursive_cache,
    fibonacci_recursive_memoization,
    fib
)

fibonacci_functions = [
    fibonacci_iterative,
    fibonacci_naive,
    fibonacci_recursive,
    fibonacci_recursive_cache,
    fibonacci_recursive_memoization,
    fib
]

def test_fib_9_is_34():
    for function in fibonacci_functions:
        assert function(9) == 34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)


def test_fib_34_is_5702887():
    for function in fibonacci_functions:
        assert function(34) == 5702887
