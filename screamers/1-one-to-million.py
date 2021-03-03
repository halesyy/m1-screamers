
"""
The simplest of tests, print from 1 -> 1,000,000.
Angles: stdout, compute, iterating.
Works: Python 2 & 3.
"""

from timeit import default_timer as timer

start = timer()

for i in range(1000000):
    print(i)

end = timer()

time_taken = (end - start)

print("seconded {}".format(time_taken))
