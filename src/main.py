import argparse
import textwrap
from parser import parallel_choices, parallel_args, parallel_functions

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

    for p in parallel_choices:
        if args.func == p:
            fib_function = parallel_functions[parallel_choices.index(p)]
            result = parallel_args(fib_function, args.nth, args.parallel, args.depth)

    print(result) 