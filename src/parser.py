parallel_choices = [
    'i',
    'm',
    'r',
    'rm',
    'rc'
    ]

def parallel_args(func: function, n: int, parallel: bool = False, depth: int = 0):
    if parallel:
        return func(n, parallel, depth)
    else:
        return func(n)