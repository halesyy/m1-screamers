
"""
Simply stuff the CPU with threading jobs
to complete, which will take some time...
Seeing the CPUs ability to multitask.
"""

from timeit import default_timer as timer

def high_compute(x):
    lots = [i for i in range(10000000)]
    lots = [i/5.2125 for i in lots]
    return len(lots)

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    start = timer()

    with ThreadPoolExecutor(50) as handler:
        results = handler.map(high_compute, range(50))

    end = timer()

    time_taken = (end - start)

    print("took", time_taken, "seconds")
