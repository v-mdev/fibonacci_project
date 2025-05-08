from multiprocessing import Process, Queue


def fibonacci_worker(func :function, n :int, q: Queue, depth :int):
    q.put(func(n, depth))


def parallel_computing(func :function, n: int, depth :int):
    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=fibonacci_worker, args=(func, n - 1, q1, depth-1))
    p2 = Process(target=fibonacci_worker, args=(func, n - 2, q2, depth-1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    result1 = q1.get()
    result2 = q2.get()

    return result1 + result2