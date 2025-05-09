import pytest

from fib import (
    fib_iterative,
    fib_recursive,
    fib_recursive_cache,
    fib_recursive_memoization,
    fib_matrix,
)

fibonacci_functions = [
    fib_iterative,
    fib_recursive,
    fib_recursive_cache,
    fib_recursive_memoization,
    fib_matrix,
]

def test_fib_9_is_34():
    for function in fibonacci_functions:
        assert function(9) == 34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fib_iterative(-1)


def test_fib_34_is_5702887():
    for function in fibonacci_functions:
        assert function(34) == 5702887
