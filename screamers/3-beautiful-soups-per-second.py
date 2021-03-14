
"""
Load 3-page into memory, then do 5,000 soups
parses. Tests how many soups can be parsed
per-second. Single-threaded
Works: Python 3.
"""

from timeit import default_timer as timer
from bs4 import BeautifulSoup

start = timer()

page = str(open("sources/3-page.html", "r", errors="ignore").read())
page = "".join([c for c in page if ord(c) < 128])
print("page length:", len(page))
parsed = [BeautifulSoup(page, "html.parser") for _ in range(5000)]

end = timer()

time_taken = (end - start)

sps = int(5000 / time_taken) # soups per-second

print("this machine can do", sps, "soups per-second, test took", time_taken, "seconds")
