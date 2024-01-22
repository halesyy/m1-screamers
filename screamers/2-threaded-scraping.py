
"""
A simple scrape-and-BSOUP parse on my own website.
Angles: compute, single-core threading.
Works: Python 3.
"""

from timeit import default_timer as timer
from concurrent.futures import ThreadPoolExecutor

"""
Make request to jackhales.com, print out response + page len
and use BeautifulSoup to compute into a class.
"""
def just_a_request(id):
    from requests import get
    from bs4 import BeautifulSoup
    page = get("https://jackhales.com")
    soup = BeautifulSoup(page.text, "html.parser")
    print("finished id:", id, "with page len:", len(page.text))
    return True

if __name__ == "__main__":

    start = timer()

    with ThreadPoolExecutor(50) as handler:
        results = handler.map(just_a_request, range(50))

    end = timer()

    if True: # set to false if you dont want extra compute
        worked = len([True for t in results if t == True])
        not_worked = len([False for t in results if t == None]) # t == None if excepts in-thread
        print("out of all req,", worked, "worked and", not_worked, "didn't")

    time_taken = (end - start)

    print("seconded {}".format(time_taken))
