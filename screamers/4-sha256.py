
from timeit import default_timer as timer
from hashlib import sha256
from random import choice

random_vals = [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
hash = lambda s: sha256(s.encode('utf-8')).hexdigest()
random = lambda amt: "".join([choice(random_vals) for _ in range(amt)])

start = timer()

for i in range(1000000):
    hash(random(10))

end = timer()

time_taken = (end - start)

print("it took", time_taken, "seconds to complete this task")
